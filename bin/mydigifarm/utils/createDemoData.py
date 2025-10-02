# Copyright 2025 mydigifarm
# License mydigifarm
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL mydigifarm BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
# Except as contained in this notice, the name of mydigifarm shall not be used in advertising or otherwise to promote the sale, use or other dealings in this Software without prior written authorization from mydigifarm.
# mydigifarm.com
# EFFECTIVEDATE: 20250821
# VERSION: 1.0
# FILE: mydigifarm,1.0,createDemoData.py
# DESCRIPTION: Generates synthetic data for the database to demo with.
# LASTMODIFIED: 20250821

#! .py

## *|*|*|*|* Start Section 1 *|*|*|*|*
## Section 1 covers the basic setup of variables and library configurations. 
## This is used to set initial variables and prepare for setup or service runs.
## *|*|*|*|* Section 1 *|*|*|*|*

# Import modules for system, datetime, random, dbWriter, and argparsing. 
import sys
sys.path.append('/home/pi/alphaprototype/bin/RPi/modules/')
import datetime
import random
import dbWriter
import argparse

argparser = argparse.ArgumentParser(description="A script used to generate demo data")
argparser.add_argument('-d','--days',help='input int param to specify number of days to generate data for')
argparser.add_argument('-c','--clusters',help="input int param to specify the number of clusters to generate data for")
inargs = argparser.parse_args()

## *|*|*|*|* End Section 1 *|*|*|*|*

## *|*|*|*|* Start Section 2 *|*|*|*|*
## Section 2 covers setting up classes and functions. 
## ## Section 2 covers Function creation along with classes and other more complex objects. 
## Most functions are created here and used in the next section. 
## *|*|*|*|* Section 2 *|*|*|*|*

# get random temp from range and return to call
def get_temp_data():
    temp = random.randrange(15, 33)
    return temp

# get random humidity from range and return to call
def get_humidity_data():
    humi = random.randrange(20, 60)
    return humi

# get random light from range based on time (day[8:20] night[20:8]) and return to call
def get_light_data(time_stamp):
    if int(time_stamp.split(' ')[1].split(':')[0]) > 8 and int(time_stamp.split(' ')[1].split(':')[0]) < 20:
        light = random.randrange(1000, 1100)
    else:
        light = random.randrange(800, 950)
    return light

# return random soil from range and return to call
def get_soil_moisture():
    moist = random.randrange(0, 70)
    return moist

# get the cluster number based on a coin flip and return to call
def get_cluster_number():
    if random.sample([0,1],1)[0] == 0:
        return 24
    else:
        return 99

def get_smooth_soil_data(soildata):
    if soildata <= 5:
        soildata = get_soil_moisture()
    else:
        soildata = soildata - random.randrange(1, 5)
    return soildata

# function that wraps a class constructor used to build the data object to insert into the database

def get_data_pill(time_stamp, cluster_number, smoothing):
    # call all the other functions to get the data
    class sensorData:
        # Store data values to object. 
        def __init__(self, eprom, temp, humi, light, soil):
            self.cluster_no = eprom
            self.temperature = float(temp)
            self.humidity = float(humi)
            self.light = int(light)
            self.saturation = int(soil)    

    # call and return the class constructor with all the properties calling the functions responsible for returning the synthetic data.
    # return sensorData( eprom=get_cluster_number(), temp=get_temp_data(), humi=get_humidity_data(), light=get_light_data(time_stamp=time_stamp), soil=get_soil_moisture())
    if not smoothing:
        smoothing = sensorData( eprom=cluster_number, temp=get_temp_data(), humi=get_humidity_data(), light=get_light_data(time_stamp=time_stamp), soil=get_soil_moisture())

    smooth_temp_data = ((int(smoothing.temperature) + int(get_temp_data()))/2)
    smooth_hum_data = ((int(smoothing.humidity) + int(get_humidity_data()))/2)
    smooth_light_data = ((int(smoothing.light) + int(get_light_data(time_stamp=time_stamp)))/2)
    smooth_soil_data = get_smooth_soil_data(soildata=smoothing.saturation)

    return sensorData( eprom=cluster_number, temp=smooth_temp_data, humi=smooth_hum_data, light=smooth_light_data, soil=smooth_soil_data)

# get date data based on a passed in number of minutes from the current time.  Translate the date data into timestamp and return to call
def get_time_stamp(minutes):
    time_stamp = datetime.datetime.now() - datetime.timedelta(minutes=minutes)
    return time_stamp.strftime("%Y.%m.%d %H:%M:%S")

# main processing function that takes the passed in number of days
#   the total number of minutes is then calculated for the number of days
#   for every 15 minutes in the number of minutes create a datapill and write that to the database
def create_data(days_of_data,number_of_clusters=None):
    minutes = days_of_data * 1440
    smoothing = [] 
    if number_of_clusters:
        clusters = list(range(1,number_of_clusters+1))
    else:
        clusters = [24,99]
    for minute in reversed(range(15, minutes, 15)):
        for i, cluster_number in enumerate(clusters):
            if i != 0:
                minute = minute + i
            time_stamp = get_time_stamp(minute)
            # if not smoothing:
            if next((x for x, obj in enumerate(smoothing) if obj.cluster_no == cluster_number), None) == None:
                demo_data_pill = get_data_pill(time_stamp, cluster_number=cluster_number, smoothing=None)
            else:
                object_index = next((x for x, obj in enumerate(smoothing) if obj.cluster_no == cluster_number), None)
                demo_data_pill = get_data_pill(time_stamp, cluster_number=cluster_number, smoothing=smoothing[object_index])
            # assign demo data from last run to the smoothing var
            smoothing.append(demo_data_pill)
            dbWriter.do_demo_write(database='mydigifarm', rowData=demo_data_pill, dataType='sensors', id=cluster_number, time_stamp=time_stamp)

        if len(smoothing) > number_of_clusters:
            del smoothing[0:(len(smoothing)-len(clusters))]

## *|*|*|*|* End Section 2 *|*|*|*|*

## *|*|*|*|* Start Section 3 *|*|*|*|*
## Section 3 executes the configuration logic based on user input.
## Prompts user through different environment settings and writes the config file.
## *|*|*|*|* Section 3 *|*|*|*|*

# check if this was the main script run.  
if __name__ == "__main__":
    if inargs.days:
        days_of_data = int(inargs.days)
    else:
        days_of_data = 15
    if inargs.clusters:
        number_of_clusters = int(inargs.clusters)
    else:
        number_of_clusters = 2
    
    create_data(days_of_data=days_of_data, number_of_clusters=number_of_clusters)

## *|*|*|*|* End Section 3 *|*|*|*|*

# -10959
# Copyright 2025 mydigifarm
