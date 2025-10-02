# Copyright 2025 mydigifarm
# License mydigifarm
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL mydigifarm BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
# Except as contained in this notice, the name of mydigifarm shall not be used in advertising or otherwise to promote the sale, use or other dealings in this Software without prior written authorization from mydigifarm.
# mydigifarm.com
# EFFECTIVEDATE: 20250822
# VERSION: 1.0
# FILE: mydigifarm,1.0,testConnect.sh
# DESCRIPTION: Checks the connection to the MariaDB server.
# LASTMODIFIED: 20250822

#! .sh

## *|*|*|*|* Start Section 1 *|*|*|*|*
## Section 1 covers the basic setup of variables and library configurations. 
## This is used to set initial variables and prepare for setup or service runs.
## *|*|*|*|* Section 1 *|*|*|*|*

# Set up the script environment paths
scriptRoot=$(dirname $(realpath $0))
myDigiRoot=$(dirname $scriptRoot)
myDigiBin=$(dirname $myDigiRoot)

## *|*|*|*|* End Section 1 *|*|*|*|*

## *|*|*|*|* Start Section 2 *|*|*|*|*
## Section 2 covers setting up classes and functions. 
## ## Section 2 covers Function creation along with classes and other more complex objects. 
## Most functions are created here and used in the next section. 
## *|*|*|*|* Section 2 *|*|*|*|*

# Advanced functions are not needed for this simple connection test.

## *|*|*|*|* End Section 2 *|*|*|*|*

## *|*|*|*|* Start Section 3 *|*|*|*|*
## Section 3 Describes the Workflow of functions that were created in section two in a logical and linear order. 
## This is where the linear code section runs. 
## *|*|*|*|* Section 3 *|*|*|*|*

# Imports defaults
FILE=$scriptRoot/config.env
if test -f "$FILE"; then
    echo "$FILE exists."
    set -a
    source $scriptRoot/config.env
    set +a
else 
    echo "Getting started"
fi

# Test the connection to the MariaDB server/
FILE=$myDigiBin/RPi/mariadbConnect.py
if test -f "$FILE"; then
    echo "$FILE exists."
    python $myDigiBin/RPi/mariadbConnect.py
    echo "MYSQL Testing complete. Status is above."
else 
    echo "$FILE does not exist."   
fi

## *|*|*|*|* End Section 3 *|*|*|*|*

# -10959
# Copyright 2025 mydigifarm 
