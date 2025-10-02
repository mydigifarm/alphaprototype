# Copyright 2025 mydigifarm
# License mydigifarm
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL mydigifarm BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
# Except as contained in this notice, the name of mydigifarm shall not be used in advertising or otherwise to promote the sale, use or other dealings in this Software without prior written authorization from mydigifarm.
# mydigifarm.com
# EFFECTIVEDATE: 20250726
# VERSION: 1.0
# FILE: mydigifarm,1.0,reboot.py

# DESCRIPTION: This file initializes the mydigifarm reboot procedures. It is responsible for initializing the services and notating the event.
# LASTMODIFIED: 20250726

#! .py

# import the necessary libraries generically
import time
import mariadb
import datetime
import os
import sys

#import activity as activity_logger
import modules.activityLogging as activity_logger

#import dbwriter as dbwriter
import modules.dbWriter as dbWriter

# Connect to MariaDB Platform
try:
        conn=mariadb.connect (
        user=((os.environ.get('MDBuser'))),
        password=((os.environ.get('MDBpass'))),
        host=((os.environ.get('MDBsiteip'))),
        port=int((os.environ.get('MDBport'))),
        database="mydigifarm"
        )
except mariadb.Error as e:
        print("Error connecting to MariaDB Platform: {e}")
        sys.exit(1)
   
#Write to activity log
if (os.environ.get('DEMOSITE') == 'True'):
    current_site_no='01'
    current_cluster_no = '01'
    current_resource = 'RPi'
    current_status = "Reboot detected"
    current_note = "detected a system reboot"
    #print("running log update \n")
#dbWriter.write_activity(current_site_no,current_cluster_no,current_resource,current_status,current_note)   
activity_logger.activity(resource=current_resource,status=current_status,note=current_note,cluster_number=current_cluster_no)
   
raw_ts = datetime.datetime.now()
new_ts = raw_ts.strftime("%Y.%m.%d %H:%M:%S")
new_note='reboot'

def build_uptime_object(current_ts, current_note):
    class uptime_data_object:
        def __init__(self, current_ts, current_note):
            self.tuptime_ts = current_ts
            self.tuptime_note = current_note

    # Write to console for admin.
    #print("returning uptime_data_object \n")
    # returning the uptime_data_object variable
    return uptime_data_object(current_ts, current_note)

#Build object from the data provided.    
input_object = build_uptime_object(new_ts,new_note)

#Write to the database
dbWriter.do_defined_write(database='mydigifarm', rowData=input_object, dataType='reboot', id=42)

#Write to activity log
current_status = "Reboot"
current_note = "documented a system reboot"
#print("running log update \n")
activity_logger.activity(resource=current_resource,status=current_status,note=current_note,cluster_number=current_cluster_no)

# -10959
# Copyright 2025 mydigifarm
