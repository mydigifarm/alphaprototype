# Copyright 2025 mydigifarm
# License mydigifarm
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL mydigifarm BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
# Except as contained in this notice, the name of mydigifarm shall not be used in advertising or otherwise to promote the sale, use or other dealings in this Software without prior written authorization from mydigifarm.
# mydigifarm.com
# EFFECTIVEDATE: 20250515
# VERSION: 1.0
# FILE: mydigifarm,1.0,lite_cluster.py

# DESCRIPTION: This file gathers data from the light, temperature, humidity, and soil sensors. It is responsible for reading the sensors, parsing the data, and writing it to the database.
# LASTMODIFIED: 20250726

#! .py

# Import the necessary libraries
import serial
import time
import datetime
import sub_pseudo
import mariadb
import os
import sys

# Gather light data
def read_light():
    
    #print("beginning read_light function")
    
    #print("attempting database connection testing")

    # Test basic connectivity to the database mydigifarm. This will allow us to write to the database later. 
    try:
      conn = mariadb.connect(
      user=((os.environ.get('MDBuser'))),
      password=((os.environ.get('MDBpass'))),
      host=((os.environ.get('MDBhost'))),
      port=int((os.environ.get('MDBport'))),
      database="mydigifarm"
      )
      print("connection to database was successful")
    except mariadb.Error as e:
      print("error connecting to MariaDB Platform: {e}")
      sys.exit(1)
    print("database connection test complete")
    
    # function to add our light record
    def add_light(cur,raw_ts,pseudo_id,new_LDR):
        try:
            cur.execute("INSERT INTO mydigifarm.tlight(tlight_ts,tlight_cluster_no,tlight_light) VALUES (%s, %s, %s)",(raw_ts,pseudo_id,new_LDR))
        except mariadb.Error as e:
              print("Error: {e}")

    #print("function created add_light")

    #Set variables for iteration loop
    #print("setting initial variables")
    i=0
    print("i = " + str(i))
    max_clusters = 7
    print("max_clusters = " + str(max_clusters))
    pseudo_id = 24
    print("pseudo_id = " + str(pseudo_id))
    unique_id = "9BDE182F50C45E1D80"
    print("unique_id = " + str(unique_id))  
  
    try:
        # Primary loop through each of our sensor clusters
        while i < max_clusters:
            print("starting cluster loop")
            path = "/dev/ttyACM"+str(i)
            print("testing path"+str(path))
            isExists = os.path.exists(path)
            if isExists:
                # variables defined with default values
                print("path appears to exist")
                #print("setting variables")
                recIDL = "z"
                actIDL = "b'L'"
                loopBreakerL = 0
                # Setup communication port(s)
                ser=serial.Serial("/dev/ttyACM"+str(i),9600)
                ser.baudrate=9600
                # Read from Arduino serial port
                while (recIDL != actIDL) and (loopBreakerL < 8):
                    print("before arduino console read")
                    read_ser=ser.readline()
                    print("This is what I found from the arduino:")
                    print(str(read_ser))
                    print("after arduino console read")
                    recIDL = str(read_ser[24:25])
                    print("This is the recIDL: " + str(recIDL))
                    loopBreakerL+=1
                    print("loopBreakerl is currently: "+str(loopBreakerL))
                # If no light records found, we are done, e.g. nothing found = nothing stored
                    print("converting output to string for parsing") 
                    str_read_ser = str(read_ser)
                    print(str_read_ser)
      
                    # obtain the record length
                    recordLength = len(str_read_ser)
                    print(str(recordLength) + " characters on the variable recordLength") 
                if (loopBreakerL < 8) and (recordLength < 43):
                    print("found a light hit")
                    #####TODO#####
                    # sub_pseudo is used to assign a more readible and understood id
                    #if pseudo_id == 99:
                        #raw_ts = datetime.datetime.now()
                        #print(raw_ts)
                        #unique_id = str(read_ser[5:23])
                        # this subroutine will use the unique id to obtain a human understandable cluster id
                        # mariadb, cur, raw_ts, unique_id, pseudo_id = sub_pseudo.assignPseudoID(mariadb, cur, raw_ts, unique_id, pseudo_id)
                    #####TODO#####

                    # Reformat as a string
                    print("converting output to string for parsing") 
                    str_read_ser = str(read_ser)
                    print(str_read_ser)
      
                    # obtain the record length
                    recordLength = len(str_read_ser)
                    print(str(recordLength) + "recordLength")
    
                            # Extract light brightness
                    if recordLength == 38:
                        print("recordLength is 38")
                        new_LDR=int(str_read_ser[32:33])    
                    if recordLength == 39:
                        print("recordLength is 39")
                        new_LDR=int(str_read_ser[32:34])
                    if recordLength == 40:
                        print("recordLength is 40")
                        new_LDR=int(str_read_ser[32:35])
                    if recordLength == 41:
                        print("recordLength is 41")
                        new_LDR=int(str_read_ser[32:36])
                    if recordLength == 42:
                        print("recordLength is 42")
                        new_LDR=int(str_read_ser[32:37])
                    print("light value " + str(new_LDR))
            
                    # Obtain current time and format
                    raw_ts = datetime.datetime.now()
                    new_ts = raw_ts.strftime("%Y.%m.%d %I:%M %p")
                    print("setting up timestamps")
                    print(str(new_ts))

                    # we have what we need for this sensor cluster so store it
                    #print("writing what we know to the database")
                    print("new_ts = " + str(new_ts))
                    print("pseudo_id = " + str(pseudo_id))
                    print("new_LDR = " + str(new_LDR))
                    print("collecting cursor and adding data to database")
                    cur=conn.cursor()
                    add_light(cur,new_ts,pseudo_id,new_LDR)
                    #print("attempted database write complete")
                    #####TODO#####          
                    # we need to determine if the artificial lights are on/off and whether or not they need changed, also update the progress as needed
                    #            mariadb, cur, raw_ts, unique_id, pseudo_id = sub_light_monitor(mariadb, cur, raw_ts, unique_id, pseudo_id_light_status)
                    #####TODO#####
                    
                    # Commit the database
                    #print("attempting to commit this to the database and close the connection")
                    conn.commit()
                    #print("closing database connection") 
                    # Close Connection
                    conn.close()

                    # go on to the next sensor cluster
            print("COM " + str(i) + " has been evaluated")        
            i+=1 
        
    except mariadb.Error as e:
        print("The try catch read_light hit an error: {e}")   

# Gather soil moisture data       
def read_soil():
    
    #print("beginning read_soil function")
    
    #print("attempting database connection testing")

    # Test basic connectivity to the database mydigifarm. This will allow us to write to the database later. 
    try:
      conn = mariadb.connect(
      user=((os.environ.get('MDBuser'))),
      password=((os.environ.get('MDBpass'))),
      host=((os.environ.get('MDBhost'))),
      port=int((os.environ.get('MDBport'))),
      database="mydigifarm"
      )
      print("connection to database was successful")
    except mariadb.Error as e:
      print("error connecting to MariaDB Platform: {e}")
      sys.exit(1)
    #print("database connection test complete")

    # function to add our soil record
    def add_soil(cur,raw_ts,pseudo_id,new_soil):
        try:
            cur.execute("INSERT INTO mydigifarm.tmoisture(tmoisture_ts,tmoisture_cluster_no,tmoisture_saturation) VALUES (%s, %s, %s)",(raw_ts,pseudo_id,new_soil))
        except mariadb.Error as e:
              print("Error: {e}")

    print("function created add_soil")

    #Set variables for iteration loop
    print("setting initial variables")
    i=0
    print("i = " + str(i))
    max_clusters = 7
    print("max_clusters = " + str(max_clusters))
    pseudo_id = 24
    print("pseudo_id = " + str(pseudo_id))
    unique_id = "9BDE182F50C45E1D80"
    print("unique_id = " + str(unique_id))  
  
    try:
        # Primary loop through each of our sensor clusters
        while i < max_clusters:
            print("starting cluster loop")
            path = "/dev/ttyACM"+str(i)
            print("testing path"+str(path))
            isExists = os.path.exists(path)
            if isExists:
                # variables defined with default values
                print("path appears to exist")
                print("setting variables")
                recIDS = "z"
                actIDS = "b'S'"
                loopBreakerS = 0
                # Setup communication port(s)
                ser=serial.Serial("/dev/ttyACM"+str(i),9600)
                ser.baudrate=9600
                # Read from Arduino serial port
                while (recIDS != actIDS) and (loopBreakerS < 8):
                    #print("before arduino console read")
                    read_ser=ser.readline()
                    #print("This is what I found from the arduino:")
                    print(str(read_ser))
                    print("after arduino console read")
                    recIDS = str(read_ser[24:25])
                    print("This is the recIDS: " + str(recIDS))
                    loopBreakerS+=1
                    print("loopBreakerS is currently: "+str(loopBreakerS))

                    #print("converting output to string for parsing") 
                    str_read_ser = str(read_ser)
                    print(str_read_ser)
      
                    # obtain the record length
                    recordLength = len(str_read_ser)
                    print(str(recordLength) + " characters on the variable recordLength") 
                if (loopBreakerS < 8) and (recordLength < 43):
                    print("found a soil moisture hit")
                    #####TODO#####
                    # sub_pseudo is used to assign a more readible and understood id
                    #if pseudo_id == 99:
                        #raw_ts = datetime.datetime.now()
                        #print(raw_ts)
                        #unique_id = str(read_ser[5:23])
                        # this subroutine will use the unique id to obtain a human understandable cluster id
                        # mariadb, cur, raw_ts, unique_id, pseudo_id = sub_pseudo.assignPseudoID(mariadb, cur, raw_ts, unique_id, pseudo_id)
                    #####TODO#####

                    # Reformat as a string
                    #print("converting output to string for parsing") 
                    str_read_ser = str(read_ser)
                    print(str_read_ser)
      
                    # obtain the record length
                    recordLength = len(str_read_ser)
                    print(str(recordLength) + " recordLength")
    
                            # Extract light brightness
                    if recordLength == 39:
                        print("recordLength is 39")
                        new_soil=int(str_read_ser[32:34].replace("%",""))
                    if recordLength == 40:
                        print("recordLength is 40")
                        new_soil=int(str_read_ser[32:35].replace("%",""))
                    if recordLength == 41:
                        print("recordLength is 41")
                        new_soil=int(str_read_ser[32:36].replace("%",""))
                    if recordLength == 42:
                        print("recordLength is 42")
                        new_soil=int(str_read_ser[32:37].replace("%",""))
                    print("soil moisture value " + str(new_soil))
            
                    # Obtain current time and format
                    raw_ts = datetime.datetime.now()
                    new_ts = raw_ts.strftime("%Y.%m.%d %I:%M %p")
                    #print("setting up timestamps")
                    print(str(new_ts))

                    # we have what we need for this sensor cluster so store it
                    #print("writing what we know to the database")
                    print("new_ts = " + str(new_ts))
                    print("pseudo_id = " + str(pseudo_id))
                    print("new_soil = " + str(new_soil))
                    #print("collecting cursor and adding data to database")
                    cur=conn.cursor()
                    add_soil(cur,new_ts,pseudo_id,new_soil)
                    #print("attempted database write complete")
                    #####TODO#####          
                    # we need to determine if the artificial lights are on/off and whether or not they need changed, also update the progress as needed
                    #            mariadb, cur, raw_ts, unique_id, pseudo_id = sub_light_monitor(mariadb, cur, raw_ts, unique_id, pseudo_id_light_status)
                    #####TODO#####
                    
                    # Commit the database
                    #print("attempting to commit this to the database and close the connection")
                    conn.commit()
                    #print("closing database connection") 
                    # Close Connection
                    conn.close()

                    # go on to the next sensor cluster
            print("COM " + str(i) + " has been evaluated")        
            i+=1 
        
    except mariadb.Error as e:
        print("The try catch read_temperature hit an error: {e}")     
    
# Gather temperature data
def read_temperature():
    
    #print("beginning read_temperature function")
    
    #print("attempting database connection testing")

    # Test basic connectivity to the database mydigifarm. This will allow us to write to the database later. 
    try:
      conn = mariadb.connect(
      user=((os.environ.get('MDBuser'))),
      password=((os.environ.get('MDBpass'))),
      host=((os.environ.get('MDBhost'))),
      port=int((os.environ.get('MDBport'))),
      database="mydigifarm"
      )
      print("connection to database was successful")
    except mariadb.Error as e:
      print("error connecting to MariaDB Platform: {e}")
      sys.exit(1)
    #print("database connection test complete")
    
    # function to add our temperature record
    def add_temp(cur,raw_ts,pseudo_id,new_temp):
        try:
            cur.execute("INSERT INTO mydigifarm.ttemperature(ttemperature_ts,ttemperature_cluster_no,ttemperature_temperature) VALUES (%s, %s, %s)",(raw_ts,pseudo_id,new_temp))
        except mariadb.Error as e:
              print("Error: {e}")

    #print("function created add_temp")
    
    #Set variables for iteration loop
    #print("setting initial variables")
    i=0
    print("i = " + str(i))
    max_clusters = 7
    print("max_clusters = " + str(max_clusters))
    pseudo_id = 24
    print("pseudo_id = " + str(pseudo_id))
    unique_id = "9BDE182F50C45E1D80"
    print("unique_id = " + str(unique_id))  
  
    try:
        # Primary loop through each of our sensor clusters
        while i < max_clusters:
            print("starting cluster loop")
            path = "/dev/ttyACM"+str(i)
            print("testing path"+str(path))
            isExists = os.path.exists(path)
            if isExists:
                # variables defined with default values
                #print("path appears to exist")
                #print("setting variables")
                recIDT = "z"
                actIDT = "b'T'"
                loopBreakerT = 0
                # Setup communication port(s)
                ser=serial.Serial("/dev/ttyACM"+str(i),9600)
                ser.baudrate=9600
                # Read from Arduino serial port
                while (recIDT != actIDT) and (loopBreakerT < 120):
                    print("before arduino console read")
                    read_ser=ser.readline()
                    #print("This is what I found from the arduino:")
                    print(str(read_ser))
                    print("after arduino console read")
                    recIDT = str(read_ser[24:25])
                    print("This is the recIDT: " + str(recIDT))
                    loopBreakerT+=1
                    print("loopBreakerT is currently: " + str(loopBreakerT))
                # If no light records found, we are done, e.g. nothing found = nothing stored
                    #print("converting output to string for parsing") 
                    str_read_ser = str(read_ser)
                    print(str_read_ser)
      
                    # obtain the record length
                    recordLength = len(str_read_ser)
                    print(str(recordLength) + " characters on the variable recordLength") 
                if (loopBreakerT < 121) and (recordLength < 75):
                    #print("found a temperature hit")
                    #####TODO#####
                    # sub_pseudo is used to assign a more readible and understood id
                    #if pseudo_id == 99:
                        #raw_ts = datetime.datetime.now()
                        #print(raw_ts)
                        #unique_id = str(read_ser[5:23])
                        # this subroutine will use the unique id to obtain a human understandable cluster id
                        # mariadb, cur, raw_ts, unique_id, pseudo_id = sub_pseudo.assignPseudoID(mariadb, cur, raw_ts, unique_id, pseudo_id)
                    #####TODO#####

                    # Reformat as a string
                    #print("converting output to string for parsing") 
                    str_read_ser = str(read_ser)
                    print(str_read_ser)
      
                    # obtain the record length
                    recordLength = len(str_read_ser)
                    print(str(recordLength) + "recordLength")
    
                    #print("reading temperature value")
                    new_temp=int(str_read_ser[30:32])
                    print("current temperature value " + str(new_temp))
            
                    # Obtain current time and format
                    raw_ts = datetime.datetime.now()
                    new_ts = raw_ts.strftime("%Y.%m.%d %I:%M %p")
                    #print("setting up timestamps")
                    print(str(new_ts))

                    # we have what we need for this sensor cluster so store it
                    #print("writing what we know to the database")
                    print("new_ts = " + str(new_ts))
                    print("pseudo_id = " + str(pseudo_id))
                    print("new_temp = " + str(new_temp))
                    #print("collecting cursor and adding data to database")
                    cur=conn.cursor()
                    add_temp(cur,new_ts,pseudo_id,new_temp)
                    #print("attempted database write complete")
                    #####TODO#####          
                    # we need to determine if the artificial lights are on/off and whether or not they need changed, also update the progress as needed
                    #            mariadb, cur, raw_ts, unique_id, pseudo_id = sub_light_monitor(mariadb, cur, raw_ts, unique_id, pseudo_id_light_status)
                    #####TODO#####
                    
                    # Commit the database
                    #print("attempting to commit this to the database and close the connection")
                    conn.commit()
                    #print("closing database connection") 
                    # Close Connection
                    conn.close()

                    # go on to the next sensor cluster
            print("COM " + str(i) + " has been evaluated")        
            i+=1 
        
    except mariadb.Error as e:
        print("The try catch read_temperature hit an error: {e}")   
    
# Gather humidity data 
def read_humidity():

    #print("beginning read_humidity function")
    
    #print("attempting database connection testing")

    # Test basic connectivity to the database mydigifarm. This will allow us to write to the database later. 
    try:
      conn = mariadb.connect(
      user=((os.environ.get('MDBuser'))),
      password=((os.environ.get('MDBpass'))),
      host=((os.environ.get('MDBhost'))),
      port=int((os.environ.get('MDBport'))),
      database="mydigifarm"
      )
      print("connection to database was successful")
    except mariadb.Error as e:
      print("error connecting to MariaDB Platform: {e}")
      sys.exit(1)
    #print("database connection test complete")
    
    # function to add our humidity record
    def add_humi(cur,raw_ts,pseudo_id,new_humi):
        try:
            cur.execute("INSERT INTO mydigifarm.thumidity(thumidity_ts,thumidity_cluster_no,thumidity_humidity) VALUES (%s, %s, %s)",(raw_ts,pseudo_id,new_humi))
        except mariadb.Error as e:
              print("Error: {e}")

    print("function created add_humi")
    
    #Set variables for iteration loop
    #print("setting initial variables")
    i=0
    print("i = " + str(i))
    max_clusters = 7
    print("max_clusters = " + str(max_clusters))
    pseudo_id = 24
    print("pseudo_id = " + str(pseudo_id))
    unique_id = "9BDE182F50C45E1D80"
    print("unique_id = " + str(unique_id))  
  
    try:
        # Primary loop through each of our sensor clusters
        while i < max_clusters:
            #print("starting cluster loop")
            path = "/dev/ttyACM"+str(i)
            print("testing path"+str(path))
            isExists = os.path.exists(path)
            if isExists:
                # variables defined with default values
                #print("path appears to exist")
                #print("setting variables")
                recIDH = "z"
                actIDH = "b'H'"
                loopBreakerH = 0
                # Setup communication port(s)
                ser=serial.Serial("/dev/ttyACM"+str(i),9600)
                ser.baudrate=9600
                # Read from Arduino serial port
                while (recIDH != actIDH) and (loopBreakerH < 120):
                    print("before arduino console read")
                    read_ser=ser.readline()
                    print("This is what I found from the arduino:")
                    print(str(read_ser))
                    print("after arduino console read")
                    recIDH = str(read_ser[41:42])
                    print("This is the recIDH: " + str(recIDH))
                    loopBreakerH+=1
                    print("loopBreakerH is currently: "+str(loopBreakerH))
                # If no light records found, we are done, e.g. nothing found = nothing stored
                    print("converting output to string for parsing") 
                    str_read_ser = str(read_ser)
                    print(str_read_ser)
      
                    # obtain the record length
                    recordLength = len(str_read_ser)
                    print(str(recordLength) + " characters on the variable recordLength") 
                if (loopBreakerH < 121) and (recordLength < 75):
                    print("found a humidity hit")
                    #####TODO#####
                    # sub_pseudo is used to assign a more readible and understood id
                    #if pseudo_id == 99:
                        #raw_ts = datetime.datetime.now()
                        #print(raw_ts)
                        #unique_id = str(read_ser[5:23])
                        # this subroutine will use the unique id to obtain a human understandable cluster id
                        # mariadb, cur, raw_ts, unique_id, pseudo_id = sub_pseudo.assignPseudoID(mariadb, cur, raw_ts, unique_id, pseudo_id)
                    #####TODO#####

                    # Reformat as a string
                    #print("converting output to string for parsing") 
                    str_read_ser = str(read_ser)
                    print(str_read_ser)
      
                    # obtain the record length
                    recordLength = len(str_read_ser)
                    print(str(recordLength) + "recordLength")
    
                    #print("reading temperature value")
                    new_humi=int(str_read_ser[47:49])
                    print("humidity value " + str(new_humi))
            
                    # Obtain current time and format
                    raw_ts = datetime.datetime.now()
                    new_ts = raw_ts.strftime("%Y.%m.%d %I:%M %p")
                    print("setting up timestamps")
                    print(str(new_ts))

                    # we have what we need for this sensor cluster so store it
                    #print("writing what we know to the database")
                    print("new_ts = " + str(new_ts))
                    print("pseudo_id = " + str(pseudo_id))
                    print("new_humi = " + str(new_humi))
                    #print("collecting cursor and adding data to database")
                    cur=conn.cursor()
                    add_humi(cur,new_ts,pseudo_id,new_humi)
                    #print("attempted database write complete")
                    #####TODO#####          
                    # we need to determine if the artificial lights are on/off and whether or not they need changed, also update the progress as needed
                    #            mariadb, cur, raw_ts, unique_id, pseudo_id = sub_light_monitor(mariadb, cur, raw_ts, unique_id, pseudo_id_light_status)
                    #####TODO#####
                    
                    # Commit the database
                    #print("attempting to commit this to the database and close the connection")
                    conn.commit()
                    #print("closing database connection") 
                    # Close Connection
                    conn.close()

                    # go on to the next sensor cluster
            print("COM " + str(i) + " has been evaluated")        
            i+=1 
        
    except mariadb.Error as e:
        print("The try catch read_temperature hit an error: {e}")  
    
read_light()

read_soil()

read_temperature()

read_humidity()

# -10959
# Copyright 2025 mydigifarm
