# Copyright 2025 mydigifarm
# License mydigifarm
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL mydigifarm BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
# Except as contained in this notice, the name of mydigifarm shall not be used in advertising or otherwise to promote the sale, use or other dealings in this Software without prior written authorization from mydigifarm.
# mydigifarm.com
# EFFECTIVEDATE: 20230220
# VERSION: 1.0
# FILE: mydigifarm,1.0,clusterLogging.py

# DESCRIPTION: This file measures the serial port of your assigned sensor clusters and writes it to the appropriate mydigifarm database tables with the helpd of some submodules. 
# LASTMODIFIED: 20250726

#! .py

# Import generic system modules. 
import os
import sys
import datetime

# Import custom mydigifarm modules. 
import modules.serialReader as serialReader
import modules.dbWriter as dbWriter
import modules.activityLogging as activity_logger
 
# Set local variables for use in the script.
databaseName = 'mydigifarm'

# Test whether or not this is a DEMOSITE. This determines a number of variable defaults if true or false. 
if os.environ.get('DEMOSITE') == 'True':

    # Pseudo_id is a variable that would get returned from another script to this variable. In the AlphaPrototype demo mode we set this to a default value.
    pseudo_id = 99

    # Make note of the DEMOSITE defaults in the logger. 
    activity_logger.activity(resource='MDFS',status='Info', note='Admin selected DEMOSITE true', cluster_number=pseudo_id)

# Test whether or not this is a DEMOSITE. This determines a number of variable defaults if true or false. 
if os.environ.get('DEMOSITE') == 'False':

    # Make note of the DEMOSITE defaults in the logger. 
    activity_logger.activity(resource='MDFS',status='Info', note='Admin selected DEMOSITE false. Cluster number pseudo_id provided.', cluster_number=pseudo_id)

# Log the activity.
activity_logger.activity(resource='MDFC',status="Read",note="Get sensor cluster data", cluster_number=pseudo_id)

# Gather the data pill from serial output using the submodule. 
sensorDataList = serialReader.get_sensor_data() 

# Log the activity.
activity_logger.activity(resource='MDFC',status="Read",note="Store sensor cluster data in database", cluster_number=pseudo_id)

# Writer to the database.
for sensorData in sensorDataList:

    # Write to console for admin.
    print(sensorData.__dict__)

    # Call database writer module. 
    dbReturn = dbWriter.do_defined_write( database=databaseName, rowData=sensorData, dataType="sensors", id=pseudo_id)

# -10959
# Copyright 2025 mydigifarm
