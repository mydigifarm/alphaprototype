# Copyright 2025 mydigifarm
# License mydigifarm
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL mydigifarm BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
# Except as contained in this notice, the name of mydigifarm shall not be used in advertising or otherwise to promote the sale, use or other dealings in this Software without prior written authorization from mydigifarm.
# mydigifarm.com
# EFFECTIVEDATE: 20240802
# VERSION: 1.0
# FILE: mydigifarm,1.0,activityLogging.py

# DESCRIPTION: This file writes log activities for mydigifarm appcode. 
# LASTMODIFIED: 20250726

#! .py

# Import the required libraries
import datetime
import os

# Import custom mydigifarm modules. 
import modules.dbWriter as dbWriter

# Creating get_site_number function
def get_site_number():
    if os.environ.get('DEMOSITE') == 'True':

        # site_number is a variable that would get returned from another script to this variable. In the AlphaPrototype demo mode we set this to a default value.
        site_number = 42

    # Returning the site_number variable
    return site_number

# Creating build_activity_object function
def build_activity_object(current_time_stamp, current_site_number, current_cluster_number, current_resource, current_status, current_note):
    class activity_data_object:
        def __init__(self, current_time_stamp, current_site_number, current_cluster_number, current_resource, current_status, current_note):
            self.tactivity_ts = current_time_stamp
            self.tactivity_site_no = current_site_number
            self.tactivity_cluster_no = current_cluster_number
            self.tactivity_resource = current_resource
            self.tactivity_status = current_status
            self.tactivity_note = current_note

    # Returning the activity_data_object variable
    return activity_data_object(current_time_stamp, current_site_number, current_cluster_number, current_resource, current_status, current_note)        

# Creating write_activity function
def write_activity(input_object):

    # Call dbWriter to write to the database. 
    dbWriter.do_defined_write(database='mydigifarm', rowData=input_object, dataType='activity', id=42)

# Creating activity function
def activity(resource, status, note, cluster_number):
    # Check if cluster number exists.
    if os.environ.get('DEMOSITE') == 'True':

        # Cluster_number is a variable that would get returned from another script to this variable. In the AlphaPrototype demo mode we set this to a default value.
        cluster_number = 99
   
    # Get current timestamp.     
    timeStamp = datetime.datetime.now().strftime("%Y.%m.%d %H:%M:%S.%f")
    # Get site number from function. 
    site_number = get_site_number()

    # Create log object. 
    activity_object = build_activity_object(
                        current_time_stamp=timeStamp, 
                        current_resource=resource, 
                        current_site_number=site_number, 
                        current_cluster_number=cluster_number, 
                        current_status=status, current_note=note
                        )
    # Write to a log file.  
    write_activity(input_object=activity_object)

# Checking if script was run at console.
if __name__ == "__main__":

    # Get the sensor data from console.
    consoleReturn = "console"
    print(consoleReturn[0])    

# -10959
# Copyright 2025 mydigifarm
