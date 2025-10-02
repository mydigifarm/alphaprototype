# Copyright 2025 mydigifarm
# License mydigifarm
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL mydigifarm BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
# Except as contained in this notice, the name of mydigifarm shall not be used in advertising or otherwise to promote the sale, use or other dealings in this Software without prior written authorization from mydigifarm.
# mydigifarm.com
# EFFECTIVEDATE: 20230220
# VERSION: 1.0
# FILE: mydigifarm,1.0,dbWriter.py

# DESCRIPTION: This file handles the database writes. This creates the data tables needed and writes to the appropriate table.
# LASTMODIFIED: 20250726

#! .py

# Import generic system modules. 
import datetime
import mariadb
import os
import sys
import time

# Creates database schema objects
def get_table_columnn_set(dataType):
    if dataType == "sensors":

        # Stores object value in tableAndColumns variable
        tableAndColumns = [["ttemperature",
                            "ttemperature_ts",
                            "ttemperature_cluster_no",
                            "ttemperature_temperature"
                            ],
                            ['thumidity',
                            'thumidity_ts',
                            'thumidity_cluster_no',
                            'thumidity_humidity'
                            ],
                            ['tmoisture',
                            'tmoisture_ts',
                            'tmoisture_cluster_no',
                            'tmoisture_saturation'
                            ],
                            ['tlight',
                            'tlight_ts',
                            'tlight_cluster_no',
                            'tlight_light'
                            ]
        ]
    elif dataType == "activity":

        # Stores object value in tableAndColumns variable
        tableAndColumns = ['tactivity',
                          'tactivity_ts',
                          'tactivity_site_no',
                          'tactivity_cluster_no',
                          'tactivity_resource',
                          'tactivity_status',
                          'tactivity_note'
        ]
    elif dataType == "newday":

        # Stores object value in tableAndColumns variable
        tableAndColumns = ['tuptime',
                          'tuptime_ts',
                          'tuptime_note'
        ]
    elif dataType == "reboot":

        # Stores object value in tableAndColumns variable
        tableAndColumns = ['tuptime',
                          'tuptime_ts',
                          'tuptime_note'
        ]
    elif dataType == "start":

        # Stores object value in tableAndColumns variable
        tableAndColumns = ['tuptime',
                          'tuptime_ts',
                          'tuptime_note'
        ]        

    # Return tableAndColumns variable
    return tableAndColumns

# Create connect_db function
def connect_db(database):

    # Create connection_param variable
    connection_params = {
        'user': str(os.environ.get('MDBuser')),
        'password': str(os.environ.get('MDBpass')),
        'host': str(os.environ.get('MDBsiteip')),
        'port': int(os.environ.get('MDBport')),
        'database': database
    }
    # Try to connect.
    dbCon = mariadb.connect(**connection_params)

    # Return database connection returns
    return dbCon

def write_data(dbCon, database, rowData, columnSet, id, time_stamp):
    #  X do the connection 
    #  X set the cursor
    # Write the data 
    # Validate (maybe even a read and compare)
    # Pass return val to main 
    dbCursor = dbCon.cursor()
    if time_stamp == "now":
        ts = datetime.datetime.now().strftime("%Y.%m.%d %H:%M:%S")
    else:
        ts = time_stamp
    if columnSet[0].__class__ == list:
        i = 0
        for cSet in columnSet:
            sqlStatement = "INSERT INTO "+database+"."+cSet[0]+" ("+cSet[1]+", "+cSet[2]+", "+cSet[3]+") VALUES(%s,%s,%s)"
            data = ts, getattr(rowData, 'cluster_no'), getattr(rowData, cSet[3].split('_')[1])
            dbCursor.execute(sqlStatement, data)
            i += 1
        dbCon.commit()
    else:
        sqlStatement = "INSERT INTO "
        data = ()
        counter = 0
        for column in columnSet:
            if counter == 0:
                sqlStatement = sqlStatement+database+'.'+column+" ("
            elif counter == len(columnSet)-1:
                sqlStatement = sqlStatement+column+") VALUES("
                data = data+(getattr(rowData, column),)
                for v in range(len(columnSet)):
                    if v == len(columnSet)-2:
                        sqlStatement = sqlStatement+"%s)"
                    elif v == len(columnSet)-1:
                        v = v + 1
                    else:
                        sqlStatement = sqlStatement+"%s,"
                    v = v + 1
            else:
                sqlStatement = sqlStatement+column+", "
                data = data+(getattr(rowData, column),)
            counter = counter + 1
        dbCursor.execute(sqlStatement, data)
    dbCon.commit()

# Create do_defined_write function
def do_defined_write(database, rowData, dataType, id):

    # Set the columns.
    columnSet = get_table_columnn_set(dataType)

    # Make the database connection.
    dbCon = connect_db(database)

    # Write the data.
    write_data(dbCon=dbCon, database=database, rowData=rowData, columnSet=columnSet, id=id, time_stamp="now")

def do_demo_write(database, rowData, dataType, id, time_stamp):

    # Set the columns.
    columnSet = get_table_columnn_set(dataType)

    # Make the database connection.
    dbCon = connect_db(database)

    # Write the data.
    write_data(dbCon=dbCon, database=database, rowData=rowData, columnSet=columnSet, id=id, time_stamp=time_stamp)

# Checking if script was run at console.
if __name__ == "__main__":

    # Get the sensor data from console.
    consoleReturn = "console"
    print(consoleReturn[0])

# -10959
# Copyright 2025 mydigifarm
