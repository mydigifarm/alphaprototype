# Copyright 2025 mydigifarm
# License mydigifarm
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL mydigifarm BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
# Except as contained in this notice, the name of mydigifarm shall not be used in advertising or otherwise to promote the sale, use or other dealings in this Software without prior written authorization from mydigifarm.
# mydigifarm.com
# EFFECTIVEDATE: 20250726
# VERSION: 1.0
# FILE: mydigifarm,1.0,mariadbConnect.py

# DESCRIPTION: This file validates the connection to the MariaDB database. It is responsible for establishing the connection and reporting any errors.
# LASTMODIFIED: 20250726

#! .py

# Import the necessary libraries
import mariadb
import os
import sys

try:

    # Connect to MariaDB Platform
    conn = mariadb.connect(

            user=((os.environ.get('MDBuser'))),

            password=((os.environ.get('MDBpass'))),

            host=((os.environ.get('MDBhost'))),

            port=int((os.environ.get('MDBport'))),

            database="mydigifarm"

        )

    print("Connection was successful.")

except mariadb.Error as e:

    print("Error connecting to MariaDB Platform: {e}")

    sys.exit(1)

cur=conn.cursor()

# -10959
# Copyright 2025 mydigifarm
