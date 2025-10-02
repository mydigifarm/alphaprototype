# Copyright 2025 mydigifarm
# License mydigifarm
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL mydigifarm BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
# Except as contained in this notice, the name of mydigifarm shall not be used in advertising or otherwise to promote the sale, use or other dealings in this Software without prior written authorization from mydigifarm.
# mydigifarm.com
# EFFECTIVEDATE: 20250726
# VERSION: 1.0
# FILE: mydigifarm,1.0,newday.py

# DESCRIPTION: This file starts a new day. It kicks off archive, daily summary, and notates the information for future reference.
# LASTMODIFIED: 20250726

#! .py

# Import the necessary libraries
import time
import mariadb
import datetime
import os
import sys

# Import activity as activity_logger
import modules.activityLogging as activity_logger

# Import dbwriter as dbwriter
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

   
# Write to activity log
if (os.environ.get('DEMOSITE') == 'True'):
    current_site_no='01'
    current_cluster_no = '01'
    current_resource = 'RPi'
    current_status = "Newday detected"
    current_note = "detected the morning"
    activity_logger.activity(resource=current_resource,status=current_status,note=current_note,cluster_number=current_cluster_no)         
        
def build_uptime_object(current_ts, current_note):
    class uptime_data_object:
        def __init__(self, current_ts, current_note):
            self.tuptime_ts = current_ts
            self.tuptime_note = current_note
        
    # Returning the uptime_data_object variable
    return uptime_data_object(current_ts, current_note)

def  add_reboot(cur,new_ts,new_note):
        try:
                cur.execute("INSERT INTO mydigifarm.tuptime(tuptime_ts,tuptime_note) VALUES (%s,%s)",(new_ts,new_note))
        except mariadb.Error as e:
                print("Error: {e}")

# Variables for updtime_object
new_ts = datetime.datetime.now().strftime("%Y.%m.%d %H:%M:%S")
new_note='reboot'

# Create uptime object 
uptime_object = build_uptime_object(current_ts=new_ts, current_note=new_note)

# Write to the database
dbWriter.do_defined_write(database='mydigifarm', rowData=uptime_object, dataType='newday', id=42)

# Write to activity log
current_status = "newday documented"
current_note = "beginning of a newday"
activity_logger.activity(resource=current_resource,status=current_status,note=current_note,cluster_number=current_cluster_no)

# -10959
# Copyright 2025 mydigifarm
