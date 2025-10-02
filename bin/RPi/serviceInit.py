# Copyright 2025 mydigifarm
# License mydigifarm
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL mydigifarm BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
# Except as contained in this notice, the name of mydigifarm shall not be used in advertising or otherwise to promote the sale, use or other dealings in this Software without prior written authorization from mydigifarm.
# mydigifarm.com
# EFFECTIVEDATE: 20250726
# VERSION: 1.0
# FILE: mydigifarm,1.0,serviceInit.py

# DESCRIPTION: This file initializes the mydigifarm services. It is responsible for initializing all services and notating the event.
# LASTMODIFIED: 20250726

#! .py

# import the necessary libraries generically
import time
import mariadb
import datetime
import os
import sys
import subprocess
import os

#import activity as activity_logger
import modules.activityLogging as activity_logger

#import dbwriter as dbwriter
import modules.dbWriter as dbWriter

#call cag file as subprocess
scriptRoot = os.path.dirname(os.path.realpath(__file__))
myDigiBin = os.path.dirname(scriptRoot)
myDigiRoot = myDigiBin+'/mydigifarm'
proc = subprocess.Popen(["python",myDigiRoot+"/cag.py"])

proc.wait()

# -10959
# Copyright 2025 mydigifarm
