# Copyright 2025 mydigifarm
# License mydigifarm
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL mydigifarm BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
# Except as contained in this notice, the name of mydigifarm shall not be used in advertising or otherwise to promote the sale, use or other dealings in this Software without prior written authorization from mydigifarm.
# mydigifarm.com
# EFFECTIVEDATE: 20250929
# VERSION: 1.0
# FILE: mydigifarm,1.0,firstRun.py
# DESCRIPTION: This is the main installation file for mydigifarm.
# LASTMODIFIED: 20250929

#! .py

## *|*|*|*|* Start Section 1 *|*|*|*|*
## Section 1 covers the basic setup of variables and library configurations. 
## *|*|*|*|* Section 1 *|*|*|*|*

#print("Starting imports.")

import os
import logging
import socket
import subprocess
import shutil
import time
#import replace util
import utils.ReplaceText as replace_text
#import createDemoData rather than launch 
# moved into function call as we've a chicken eggy sort of situation here.  May want to split up firstRun into a couple scripts.
#from crontab import CronTab
#import mariadb

## *|*|*|*|* End Section 1 *|*|*|*|*

#print("Import is complete.")


mariaDbConfig = "/etc/mysql/mariadb.conf.d/50-server.cnf"
mariaBindAddress = '0.0.0.0'


apt_packages_for_install = " ".join((
    'libmariadb3',
    'libmariadb-dev',
    'nodejs',
    'npm',
    'default-libmysqlclient-dev',
    'pkg-config'
))

pip_packages_for_install = ' '.join((
    'mysql-connector-python',
    'mariadb',
    'pyserial',
    'python-crontab'
))

sqlFiles = (
    "config.sql",
    "light.sql",
    "temperature.sql",
    "moisture.sql",
    "humidity.sql",
    "sensor.sql",
    "uptime.sql",
    "controller.sql",
    "zone.sql",
    "site.sql",
    "cluster.sql",
    "activity.sql"
)

scriptRoot = os.path.dirname(os.path.realpath(__file__))
myDigiBin = os.path.dirname(scriptRoot)
myDigiAppRoot = os.path.dirname(myDigiBin)
myDigiMaria = myDigiBin+"/Database"
myDigiRoot = myDigiBin + '/mydigifarm'
myDigiRPi = myDigiBin + '/RPi'
myDigiVault = myDigiBin + '/Vault'
myDigiwww = myDigiRoot + '/www'
myDigiScripts = myDigiRoot + '/scripts'
#npmConfig = myDigiwww+"/webfront"

print("Printing relative paths: \n\tScriptRoot: "+scriptRoot+"\n\tmyDigiAppRoot: "+myDigiAppRoot+"\n\tmyDigiBin: "+myDigiBin+"\n\tmyDigiMaria: "+myDigiMaria+"\n\tmyDigiRoot: "+myDigiRoot+"\n\tmyDigiRPi: "+myDigiRPi+"\n\tmyDigiwww: "+myDigiwww+"\n\tmydigiScripts: "+myDigiScripts)

dbUser=((os.environ.get('MDBuser')))
dbHost=((os.environ.get('MDBhost')))
dbPort=int(((os.environ.get('MDBport'))))
dbIP=((os.environ.get('MDBsiteip')))
dbPass=((os.environ.get('MDBpass')))

# Set array of arguments for package installations used in this script
install_commands = ['sudo apt-get update',
                'sudo apt-get install -y '+apt_packages_for_install,
                'python -m pip install --upgrade pip',
                'python -m pip install -r '+myDigiRoot+'/requirements.txt --no-cache-dir',
                'python '+myDigiVault+'/vault_setup.py -i -c -k'
]

django_commands = ['python3 '+myDigiwww+'/webback/manage.py migrate',
                'nohup python3 '+myDigiwww+'/webback/manage.py runserver 0.0.0.0:8000 &'
]

create_data_command = 'python '+myDigiRPi+'/modules/createDemoData.py',


npm_commands = [ f"cd {myDigiwww}/webfront/ && npm install",
                 f"cd {myDigiwww}/webfront/ && nohup npm run dev > npm-nohup.txt 2>&1 &"
               ]

# update dicts for file updating 
mariaDB_update_dict = {"127.0.0.1": mariaBindAddress}
#npm_update_dict = {VITE_API_BASE_URL=http://localhost:8000}


django_update_dict = {
                      'MDFDATABASENAME': 'mydigifarm',
                      }
## removed from above dict
#'MDFDATABASEUSER': dbUser,
#'MDFDATABASEPASSWORD': ((os.environ.get('MDBpass'))),
#'MDFIPADDRESS': ((os.environ.get('RPIsiteip'))),

vue_update_dict = {'localhost': ((os.environ.get('RPIsiteip')))}


def run_sql_file(inFile, sqlCursor):
    with open(inFile, 'r') as sqlFileReader:
        sqlFile = sqlFileReader.read()
        
    sqlCommands = sqlFile.split(';')
    for command in sqlCommands:
        if not command.startswith('--'):
            try:
                sqlCursor.execute(command)
            except Exception as e:
                print('Command skipped: ')
                
def run_single_sql_commands(sqlCommand, sqlCursor):
    try:
        sqlCursor.execute(sqlCommand)
    except sqlCursor.Error as e:
        print("error {e}")


def run_cli_commands(command, use_shell):
    print(command)
    if(use_shell):
        proc = subprocess.Popen(command, shell=True)
    else:
        proc = subprocess.Popen(command.split())
    try:
        logging.info('Installing required package{}'.format(command))
        outs, errs = proc.communicate(timeout=1600)
    except subprocess.TimeoutExpired:
        proc.kill()
        outs, errs = proc.communicate()
        logging.exception(errs)


def update_config_file(updateDict, filePath):
    replace_text.replace_text(path=filePath, find_and_replace=updateDict)
    print('Updated file at '+filePath)


def connect_db(dbUser, dbHost, dbPort):
    import mariadb
    dbConnect = mariadb.connect(user=dbUser, host=dbHost, port=dbPort)
    return dbConnect


def set_cron_jobs(scriptPath):
    #import the module in the function
    #print("Setting up crontab.")

    from crontab import CronTab

    cron = CronTab(user='pi')

    job = cron.new(command='sleep 120 && bash ' +scriptPath+'/initialize.sh reboot &')
    job.every_reboot()

    job1 = cron.new(command='bash ' +scriptPath+'/initialize.sh newday')
    job1.setall("0 0 * * *")

    job2 = cron.new(command='bash '+scriptPath+'/initialize.sh sensors')
    job2.setall("*/15 * * * *")
    cron.write()


#print("Making MDFlogpath folder.")

# Check for logging directory and create it if it does not exist
try:
    os.mkdir(os.environ.get('MDFlogpath'))
except:
    logging.info("Folder {} already exists".format(os.environ.get('MDFlogpath')))
#print("Create log file.")
# Create log file and begin logging
logging.basicConfig(filename="{}/mydigifarm_setup.log".format(
    os.environ.get('MDFlogpath')), level=logging.INFO)
logging.info('Logging started.')

#print("Validating the config data.")
# Checks each of the input variables provided by the config file and gathers the inputs as necessary
if (os.environ.get('RPIuser') == ''):
    RPIuser = input("Enter RPi account username[pi]: ")
    if (os.environ.get('RPIuser') == ''):
        RPIuser = 'pi'
logging.info("Stored RPIuser value: {} variable".format(os.environ.get('RPIuser')))

# Checks each of the input variables provided by the config file and gathers the inputs as necessary
if (os.environ.get('RPIpass') == ''):
    RPIpass = input("Enter RPi account password[raspberry]: ")
    if (os.environ.get('RPIpass') == ''):
        RPIpass = 'raspberry'
logging.info("Stored RPIpass value: {} variable".format(os.environ.get('RPIpass')))

# Checks each of the input variables provided by the config file and gathers the inputs as necessary
if (os.environ.get('RPIsiteip') == ''):
    RPIsiteip = input("Enter RPi site IP[]: ")
    if (os.environ.get('RPIsiteip') == ''):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        RPIsiteip = s.getsockname()[0]
else:
    RPIsiteip = ((os.environ.get('RPIsiteip')))
logging.info("Stored RPIsiteip value: {} variable".format(os.environ.get('RPIsiteip')))

# Checks each of the input variables provided by the config file and gathers the inputs as necessary
if (os.environ.get('MDBuser') == ''):
    MDBuser = input("Enter MariaDB account username[root]: ")
    if (os.environ.get('MDBuser') == ''):
        MDBuser = 'root'
logging.info("Stored MDBuser value: {} variable".format(os.environ.get('MDBuser')))

# Checks each of the input variables provided by the config file and gathers the inputs as necessary
if (os.environ.get('MDBpass') == ''):
    MDBpass = input("Enter MariaDB account password[mydigifarm]: ")
    if (os.environ.get('MDBpass') == ''):
        MDBpass = 'mydigifarm'
logging.info("Stored MDBuser value: {} variable".format(os.environ.get('MDBpass')))

# Checks each of the input variables provided by the config file and gathers the inputs as necessary
if (os.environ.get('MDBport') == ''):
    MDBport = input("Enter MariaDB port[3306]: ")
    if (os.environ.get('MDBport') == ''):
        MDBport = '3306'
logging.info("Stored MDBport value: {} variable".format(os.environ.get('MDBport')))

# Checks each of the input variables provided by the config file and gathers the inputs as necessary
if (os.environ.get('VLTsvcact') == ''):
    VLTsvcact = input("Enter Vault service account[mydigifarm]: ")
    if (os.environ.get('VLTsvcact') == ''):
        VLTsvcact = 'mydigifarm'
logging.info("Stored VLTsvcact value: {} variable".format(os.environ.get('VLTsvcact')))

# Checks each of the input variables provided by the config file and gathers the inputs as necessary
if (os.environ.get('VLTsvcpass') == ''):
    VLTsvcpass = input("Enter Vault service account password[mydigifarm]: ")
    if (os.environ.get('VLTsvcpass') == ''):
        VLTsvcpass = 'mydigifarm'
logging.info("Stored VLTsvcpass value: {} variable".format(os.environ.get('VLTsvcpass')))
#print("Finished config validations.")

## I dont think this is needed
##this needs to return both if it's to be used
def import_modules_after_pip_install():
    #print("Importing cron")
    from crontab import CronTab
    #print("Importing maria.")
    import mariadb
    return mariadb, DemoData

###
##  Beggining of main processing block this should go in a if __name__ == '__main__'
###
# iterate over install commands and pass them to the command runner
for command in install_commands:
    run_cli_commands(command=command, use_shell=False)


## npm update broken out from the below comment block.  It was in with mariadb stuff
npmENVConfig = myDigiwww+"/webfront/.env"
npm_update_dict = {"DEFAULTIPADDRESS": ((os.environ.get('MDBsiteip')))}
update_config_file(filePath=npmENVConfig, updateDict=npm_update_dict)


#set cron jobs
set_cron_jobs(myDigiScripts)

## get config data and update config files
#  read vault token
with open(myDigiBin+'/Vault/web_key.txt', 'r') as vault_key_text:
    vault_key = vault_key_text.readline()

#update dict for django file
django_update_dict['MDFVAULTTOKEN'] = vault_key

#update files
update_config_file(filePath=myDigiwww+'/webback/mydigifarm_api/settings/base.py', updateDict=django_update_dict)
#update_config_file(filePath=myDigiwww+'/webfront/src/main.js', updateDict=vue_update_dict)

#make demo data go sql good
## moved to module import style 
#run_cli_commands(command=create_data_command, use_shell=True)
# trying import here the import after pip install is dead.  
if os.environ.get('DEMODATA'):
    import utils.createDemoData as DemoData
    if os.environ.get('DEMOCLUSTERS') != "Default":
        DemoData.create_data(days_of_data=15,number_of_clusters=int(os.environ.get('DEMOCLUSTERS')))
    else:
        DemoData.create_data(days_of_data=15,number_of_clusters=2)

#setup and start django 
for command in django_commands:
    run_cli_commands(command=command, use_shell=True)

for command in npm_commands:
    run_cli_commands(command=command, use_shell=True)

# -10959
# Copyright 2025 mydigifarm
