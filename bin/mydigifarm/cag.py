# Copyright 2025 mydigifarm
# License mydigifarm
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL mydigifarm BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
# Except as contained in this notice, the name of mydigifarm shall not be used in advertising or otherwise to promote the sale, use or other dealings in this Software without prior written authorization from mydigifarm.
# mydigifarm.com
# EFFECTIVEDATE: 20250812
# VERSION: 1.0
# FILE: mydigifarm,1.0,cag.py
# DESCRIPTION: Determines if this is a cag. 
# LASTMODIFIED: 20250812

#! .py

## *|*|*|*|* Start Section 1 *|*|*|*|*
## Section 1 covers the basic setup of variables and library configurations. 
## This is used to set initial variables and prepare for setup or service runs.
## *|*|*|*|* Section 1 *|*|*|*|*

#Import OS and subprocess modules.
import time
import mariadb
import datetime
import os
import sys

## *|*|*|*|* End Section 1 *|*|*|*|*

## *|*|*|*|* Start Section 2 *|*|*|*|*
## Section 2 covers setting up classes and functions. 
## Most functions are created here and used in the next section. 
## *|*|*|*|* Section 2 *|*|*|*|*

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

raw_ts = datetime.datetime.now()
new_ts = raw_ts.strftime("%Y.%m.%d %H:%M:%S")
new_note='init'

def  service_init(cur,new_ts,tsite_site_name,tsite_site_no,tsite_site_id,tsite_site_add):
        try:
                cur.execute("INSERT INTO mydigifarm.tsite(tsite_ts,tsite_site_name,tsite_site_no,tsite_site_id,tsite_site_add) VALUES (%s,%s,%s,%s,%s)",(new_ts,tsite_site_name,tsite_site_no,tsite_site_id,tsite_site_add))
        except mariadb.Error as e:
                print("Error: {e}")

## *|*|*|*|* End Section 2 *|*|*|*|*

## *|*|*|*|* Start Section 3 *|*|*|*|*
## Section 3 The code below typically calls the functions created in section 2 in a logical order. 
## Based on the arguments presented to the script, one of the following if statements will run.
## *|*|*|*|* Section 3 *|*|*|*|*

if (os.environ.get('DEMOSITE') == 'True'):
    tsite_site_no='01'
    tsite_site_id = 'mydigifarm0001'
    tsite_site_name='mydigifarm demo site'
    tsite_site_add='0'
    #Get Cursor
    cur = conn.cursor()
    service_init(cur,new_ts,tsite_site_name,tsite_site_no,tsite_site_id,tsite_site_add)
    conn.commit()
    # Close Connection
    conn.close()

## *|*|*|*|* End Section 3 *|*|*|*|*

# -10959
# Copyright 2025 mydigifarm
