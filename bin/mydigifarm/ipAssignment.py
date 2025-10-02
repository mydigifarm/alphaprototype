# Copyright 2025 mydigifarm
# License mydigifarm
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL mydigifarm BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
# Except as contained in this notice, the name of mydigifarm shall not be used in advertising or otherwise to promote the sale, use or other dealings in this Software without prior written authorization from mydigifarm.
# mydigifarm.com
# EFFECTIVEDATE: 20250812
# VERSION: 1.0
# FILE: mydigifarm,1.0,ipAssignment.py

# DESCRIPTION: Defines the IP Address assignment for the mydigifarm services. 
# LASTMODIFIED: 20250812

#! .py

## *|*|*|*|* Start Section 1 *|*|*|*|*
## Section 1 covers the basic setup of variables and library configurations. 
## This is used to set initial variables and prepare for setup or service runs.
## *|*|*|*|* Section 1 *|*|*|*|*

#Import OS and subprocess modules.
import os
import subprocess
import socket

scriptRoot = os.path.dirname(os.path.realpath(__file__))
myDigiBin = os.path.dirname(scriptRoot)
myDigiRoot = myDigiBin + '/mydigifarm'
myDigiRPi = myDigiBin + '/RPi'
myDigiwww = myDigiRoot + '/www'
myDigiScripts = myDigiRoot + '/scripts'

## *|*|*|*|* End Section 1 *|*|*|*|*

## *|*|*|*|* Start Section 2 *|*|*|*|*
## Section 2 covers setting up classes and functions. 
## Most functions are created here and used in the next section. 
## *|*|*|*|* Section 2 *|*|*|*|*

# Check if this is a demo. 
demo_val = input("Is this a demo [n]?")

# Checks each of the input variables provided by the config file and gathers the inputs as necessary
if ((demo_val == 'y') or (demo_val == 'Y')):
    os.environ["DEMOSITE"] = 'True'
    host = socket.getfqdn()
    sample_var = input("Do you want to start with sample data? [n]")
    if ((sample_var == 'y') or (sample_var == 'Y')):
        os.environ["sampledata"] = "True"
    def get_ip_address():
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        return s.getsockname()[0]
    addr = get_ip_address()
    DEMO = input(f"Is this the IP: {addr} [n]?")
    if ((DEMO == 'y') or (DEMO == 'Y')):
        os.environ["MDBsiteip"] = addr
        os.environ["RPIsiteip"] = addr
        os.environ["VLTsiteip"] = addr
        os.environ["WEBsiteip"] = addr

# Checks each of the input variables provided by the config file and gathers the inputs as necessary
if (os.environ.get('MDBsiteip') == 'DEFAULTIPADDRESS'):
    os.environ["MDBsiteip"] = input("What is the Database IP?: ")
    if (os.environ.get('MDBsiteip') == ''):
        MDBsiteip = '192.168.1.125'

# Checks each of the input variables provided by the config file and gathers the inputs as necessary
if (os.environ.get('RPIsiteip') == 'DEFAULTIPADDRESS'):
    os.environ["RPIsiteip"] = input("What is the Raspberry Pi Site IP?: ")
    if (os.environ.get('RPIsiteip') == ''):
        RPIsiteip = '192.168.1.125'

# Checks each of the input variables provided by the config file and gathers the inputs as necessary
if (os.environ.get('VLTsiteip') == 'DEFAULTIPADDRESS'):
    os.environ["VLTsiteip"] = input("What is the Vault's IP?: ")
    if (os.environ.get('VLTsiteip') == ''):
        VLTsiteip = '192.168.1.125'

# Checks each of the input variables provided by the config file and gathers the inputs as necessary
if (os.environ.get('WEBsiteip') == 'DEFAULTIPADDRESS'):
    os.environ["WEBsiteip"] = input("What is the Webserver's ip IP?: ")
    if (os.environ.get('WEBsiteip') == ''):
        WEBsiteip = '192.168.1.125'

# Read in the file
with open(myDigiScripts+'/config.env', 'r') as file :
  filedata = file.read()

# Replace the target string
filedata = filedata.replace('DEFAULTIPADDRESS', os.environ["MDBsiteip"])
filedata = filedata.replace('DEFAULTDEMOSTATUS', os.environ["DEMOSITE"])

## *|*|*|*|* End Section 2 *|*|*|*|*

## *|*|*|*|* Start Section 3 *|*|*|*|*
## Section 3 The code below typically calls the functions created in section 2 in a logical order. 
## Based on the arguments presented to the script, one of the following if statements will run.
## *|*|*|*|* Section 3 *|*|*|*|*

# Write the file out again
with open(myDigiScripts+'/config.env', 'w') as file:
  file.write(filedata)

## *|*|*|*|* End Section 3 *|*|*|*|*

# -10959
# Copyright 2025 mydigifarm
