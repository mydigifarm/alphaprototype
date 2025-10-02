# Copyright 2025 mydigifarm
# License mydigifarm
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL mydigifarm BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
# Except as contained in this notice, the name of mydigifarm shall not be used in advertising or otherwise to promote the sale, use or other dealings in this Software without prior written authorization from mydigifarm.
# mydigifarm.com
# EFFECTIVEDATE: 20250821
# VERSION: 1.0
# FILE: mydigifarm,1.0,ReplaceText.py
# DESCRIPTION: Replaces text in a file based on a dictionary of find and replace pairs.
# LASTMODIFIED: 20250821

#! .py

## *|*|*|*|* Start Section 1 *|*|*|*|*
## Section 1 covers the basic setup of variables and library configurations. 
## This is used to set initial variables and prepare for setup or service runs.
## *|*|*|*|* Section 1 *|*|*|*|*

# No imports needed for this file. Atypical but it happens. 

## *|*|*|*|* End Section 1 *|*|*|*|*

## *|*|*|*|* Start Section 2 *|*|*|*|*
## Section 2 covers setting up classes and functions. 
## ## Section 2 covers Function creation along with classes and other more complex objects. 
## Most functions are created here and used in the next section. 
## *|*|*|*|* Section 2 *|*|*|*|*

def private_file_actions(path, find, replace):
    with open(path, 'r') as read_file:
        intext = read_file.read()
        out_text = intext.replace(find, replace)
        with open(path, 'w') as out_file:
            out_file.write(out_text)

def replace_text(path, find_and_replace):
    for find, replace in find_and_replace.items():
        private_file_actions(path=path, find=find, replace=replace)

## *|*|*|*|* End Section 2 *|*|*|*|*

# -10959
# Copyright 2025 mydigifarm
