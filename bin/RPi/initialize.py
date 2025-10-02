# Copyright 2025 mydigifarm
# License mydigifarm
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL mydigifarm BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
# Except as contained in this notice, the name of mydigifarm shall not be used in advertising or otherwise to promote the sale, use or other dealings in this Software without prior written authorization from mydigifarm.
# mydigifarm.com
# EFFECTIVEDATE: 20230320
# VERSION: 1.0
# FILE: mydigifarm,1.0,initialize.py

# DESCRIPTION: This file notates the initialization of the mydigifarm services. 
# LASTMODIFIED: 20250726

#! .py

# Import the necessary libraries generically
import datetime
import os

# Import activity as activity_logger
import modules.activityLogging as activity_logger

# Import dbwriter as dbwriter
import modules.dbWriter as dbWriter

if (os.environ.get('DEMOSITE') == 'True'):
        activity_logger.activity(resource='RPi',status='Initializing',note='Demo site detected', cluster_number='43')

def build_uptime_object(current_ts, current_note):
    class uptime_data_object:
        def __init__(self, current_ts, current_note):
            self.tuptime_ts = current_ts
            self.tuptime_note = current_note
    return uptime_data_object(current_ts, current_note)       

# Defines data that needsto be provided
new_ts = datetime.datetime.now().strftime("%Y.%m.%d %H:%M:%S")
new_note='Start'

# Build object from the data provided    
input_object = build_uptime_object(new_ts,new_note)

# Write to the database
dbWriter.do_defined_write(database='mydigifarm', rowData=input_object, dataType='start', id=42)

# Write to activity log
current_status = "Site Started"
current_note = "Services launched successfully"
print("running log update \n")
activity_logger.activity(resource='RPi',status=current_status,note=current_note,cluster_number='42')

# -10959
# Copyright 2025 mydigifarm
