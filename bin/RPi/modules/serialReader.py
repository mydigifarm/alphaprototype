# Copyright 2025 mydigifarm
# License mydigifarm
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL mydigifarm BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
# Except as contained in this notice, the name of mydigifarm shall not be used in advertising or otherwise to promote the sale, use or other dealings in this Software without prior written authorization from mydigifarm.
# mydigifarm.com
# EFFECTIVEDATE: 20230220
# VERSION: 1.0
# FILE: mydigifarm,1.0,serialReader.py

# DESCRIPTION: This file reads the serial port from the sensor cluster.
# LASTMODIFIED: 20250726

#! .py

# Import generic system modules. 
import serial
import serial.tools.list_ports as serTools
import time
# ##### This is being commented out for now until we finish the GPIO build. 
#import RPi.GPIO as GPIO

# Gather serial ports. 
def get_serial_port():
    # Create variables.
    ports = serTools.comports()
    portReturn = []
    # Iterate through serial ports. 
    for port in ports:
        # Filter ports by USB data. 
        if 'USB Serial' in port.description or 'ttyACM' in port.description:
            portReturn.append(port)
    return portReturn

# Create data object. 
def build_sensor_object(eprom, temp, humi, light, soil):
    class sensorData:

        # Store data values to object. 
        def __init__(self, eprom, temp, humi, light, soil):
            self.cluster_no = eprom
            self.temperature = float(temp)
            self.humidity = float(humi)
            self.light = int(light)
            self.saturation = int(soil)    

    return sensorData( eprom, temp, humi, light, soil)

# Get data averages. 
def get_list_obj_avg(inputList):

    # Get averages for each sensor. 
    tempAvg = round(sum(element.temperature for element in inputList)/len(inputList), 2)
    humiAvg = round(sum(element.humidity for element in inputList)/len(inputList), 2)
    lightAvg = sum(element.light for element in inputList)/len(inputList)
    soilAvg = sum(element.saturation for element in inputList)/len(inputList)

    return build_sensor_object(inputList[0].cluster_no, tempAvg, humiAvg, lightAvg, soilAvg)


# Get GPIO pin data. 
def get_sensor_data():

    # Create arrays
    returnObjList = []
    sensorDataObjList = []
    # Setup GPIO pins.
    # ##### GPIO.setmode(GPIO.BOARD) <-- This will get modified with the GPIO module. 
    # ##### GPIO.setup(36, GPIO.OUT) <-- This will get modified with the GPIO module. 
    
    for serReadPort in get_serial_port(): 
        
        # create serial connection
        serialCon = serial.Serial(
            port=serReadPort.device,
            baudrate=9600,
            parity=serial.PARITY_NONE,
            stopbits=serial.STOPBITS_ONE,
            bytesize=serial.EIGHTBITS,
            timeout=0
        )

        # Set variable for iteration.
        i = 0
        while i < 6:
            # ##### Insert if statement to test if the connection is usb or GPIO and either trigger serial write or gpio low
            # ##### GPIO.output(36, GPIO.LOW)
            # Start gathering serial data. 
            serialCon.write('1'.encode())
            #time.sleep(1)
            thing = serialCon.readline().decode('utf-8')
            time.sleep(.3)
            stringThing = str(thing)
            if "|" in thing and "\r\n" in thing and ( 37 <= len(stringThing) <= 40) :
                # Found a match for line. 
                thingSplit = thing.split("|")
                sensorDataObjList.append(build_sensor_object(thingSplit[0],thingSplit[1],thingSplit[2],thingSplit[3],thingSplit[4].replace('\r\n','')))
                i += 1
            
        # ##### GPIO.output(36, GPIO.HIGH) <-- This will get modified with the if statement for GPIO vs. serial above. 
        # ##### GPIO.cleanup() <-- This will get modified with the if statement for GPIO vs. serial above. 

        # Close the serial connection
        serialCon.close()

        # Setting variables
        returnObjAvg = get_list_obj_avg(sensorDataObjList)
        returnObjList.append(returnObjAvg)

    # Returning variables
    return returnObjList

# Checking if script was run at console.
if __name__ == "__main__":

    # Get the sensor data from console.
    consoleReturn = get_sensor_data()
    print(consoleReturn[0])

# -10959
# Copyright 2025 mydigifarm
