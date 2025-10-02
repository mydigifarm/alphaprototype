# Copyright 2025 mydigifarm
# License mydigifarm
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL mydigifarm BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
# Except as contained in this notice, the name of mydigifarm shall not be used in advertising or otherwise to promote the sale, use or other dealings in this Software without prior written authorization from mydigifarm.
# mydigifarm.com
# EFFECTIVEDATE: 20250825
# VERSION: 1.0
# FILE: mydigifarm,1.0,initialize.sh
# DESCRIPTION: This file initializes the mydigifarm appcode libraries. It is responsible for initializing first time run and creating default variables.
# LASTMODIFIED: 20250825

#! .sh

## *|*|*|*|* Start Section 1 *|*|*|*|*
## Section 1 covers the basic setup of variables and library configurations.
## This is used to set initial variables and prepare for setup or service runs.
## *|*|*|*|* Section 1 *|*|*|*|*

# Write to console for admin.
echo "setting variables"
# Set local variables for use in the script.
ARGUMENTS=$1
scriptRoot=$(dirname $(realpath $0))
myDigiRoot=$(dirname $scriptRoot)
myDigiBin=$(dirname $myDigiRoot)
ENVIRONMENTCONFIGURATION="$scriptRoot/config.env"
IPASSIGNMENTSCRIPT="$myDigiRoot/ipAssignment.py"
SETUPSCRIPT="$myDigiRoot/setupConfig.py"
FIRSTRUNSCRIPT=$myDigiRoot/firstRun.py
INITIALIZESCRIPT=$myDigiBin/RPi/initialize.py
SERVICEINITIALIZESCRIPT=$myDigiBin/RPi/serviceInit.py
NEWDAYSCRIPT=$myDigiBin/RPi/newday.py
SERVICEINITIALIZESCRIPT=$myDigiBin/RPi/serviceInit.py
REBOOTSCRIPT=$myDigiBin/RPi/reboot.py
CLUSTERLOGGINSCRIPT=$myDigiBin/RPi/clusterLogging.py

# Temp user assignment (needs to move to config.env)
mdfUser='pi'

# Write to console for admin.
echo "setting current file"

## *|*|*|*|* End Section 1 *|*|*|*|*

## *|*|*|*|* Start Section 2 *|*|*|*|*
## Section 2 covers setting up classes and functions.
## ## Section 2 covers Function creation along with classes and other more complex objects.
## Most functions are created here and used in the next section.
## *|*|*|*|* Section 2 *|*|*|*|*

# Advanced functions are not needed for initialization script. Most workflows and their functions are initialized from here.

## *|*|*|*|* End Section 2 *|*|*|*|*

## *|*|*|*|* Start Section 3 *|*|*|*|*
## Section 3 Describes the Workflow of functions that were created in section two in a logical and linear order.
## This is where the linear code section begins.
## *|*|*|*|* Section 3 *|*|*|*|*

# Write to console for admin.
echo "test if file exists"
# Test if the path exists.
if test -f "$ENVIRONMENTCONFIGURATION"; then
  # Write to console for admin.
  echo "the file exists at the path"
  # print to the console.
  echo "$ENVIRONMENTCONFIGURATION exists"
  # Set environment variables based on FILE
  set -a
  source $ENVIRONMENTCONFIGURATION
  set +a
else
  # Write to console for admin.
  echo "Getting started"
  # Write to console for admin.
  echo "The starting parameters don't match the required parameters. Please investigate."
fi

# Write to console for admin.
echo "checking if firstrun applies"
if [ "$ARGUMENTS" == "firstrun" ]; then
  # New script launch
  ## this will copy a template and prompt the user about
  ## demo configuration or prompt for config file answers
  echo "copying config and prompting for user selections"
  # launch the file
  python $SETUPSCRIPT
  # end new script section
  # source env file we just created
  set -a
  source $ENVIRONMENTCONFIGURATION
  set +a
  # Test if the DEMOSITE env var is demostie and setup docker container if so
  if [ $DEMOSITE == 'True' ]; then
    /bin/bash $scriptRoot/createSwap.sh
    # Run docker installer
    /bin/bash $scriptRoot/install-docker.sh
    # Start docker db container
    (
      cd $myDigiBin/Database/mydigifarm-db-docker/ || exit
      docker compose up -d
    )
    # Write to console for admin.
  fi

  echo "firstrun parameter supplied, beginning build"

  # Write to console for admin.
  echo "located firstRun files"
  # Write to console for admin.
  echo "installing rust"
  su $mdfUser -c "curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y"
  echo "setting up venv"
  python -m venv $myDigiRoot/mydigivenv
  echo "starting venv"
  source $myDigiRoot/mydigivenv/bin/activate
  echo "initializing firstRun"
  python $FIRSTRUNSCRIPT
  $FIRSTRUNSCRIPT=$null
  ARGUMENTS=$null

  # Write to console for admin.
  echo "running initialize"
  python $INITIALIZESCRIPT
  INITIALIZESCRIPT=$null
  ARGUMENTS=$null
  # Write to console for admin.
  echo "running serviceInit"

  python $SERVICEINITIALIZESCRIPT
  SERVICEINITIALIZESCRIPT=$null
  echo setting permissions on install
  #chown -R $mdfUser:$mdfUser $myDigiBin/*
  find $myDigiBin/* -not -path "*/db-data/*" -exec chown $mdfUser:$mdfUser {} \;
elif [ "$ARGUMENTS" == "newday" ]; then
  echo "starting venv"
  # Set up venv for python scripts
  source $myDigiRoot/mydigivenv/bin/activate
  # Write to console for admin.
  echo "newday parameter supplied"

  # Write to console for admin.
  echo "running newday"
  python $NEWDAYSCRIPT
  NEWDAYSCRIPT=$null
  ARGUMENTS=$null
  # Write to console for admin.
  echo "running serviceInit"

  python $SERVICEINITIALIZESCRIPT
  SERVICEINITIALIZESCRIPT=$null
elif [ "$ARGUMENTS" == "reboot" ]; then
  # Set up venv for python scripts
  echo "starting venv"
  # Set up venv for python scripts
  source $myDigiRoot/mydigivenv/bin/activate
  # Write to console for admin.
  echo "reboot parameter supplied"

  echo "starting and unlocking vault"
  PYTHONFILE="$myDigiBin/Vault/vault_setup.py -s"
  python $PYTHONFILE
  # Write to console for admin.
  echo "running reboot"
  python $REBOOTSCRIPT
  REBOOTSCRIPT=$null
  ARGUMENTS=$null
  # Write to console for admin.
  echo "running serviceInit"
  python $SERVICEINITIALIZESCRIPT
  SERVICEINITIALIZESCRIPT=$null
  nohup python3 $myDigiRoot/www/webback/manage.py runserver 0.0.0.0:8000 >$myDigiRoot/www/webback/nohup.txt 2>&1 &
  sleep 2
  cd $myDigiRoot/www/webfront && nohup npm run serve >npm-nohup.txt 2>&1 &
elif [ "$ARGUMENTS" == "sensors" ]; then
  # Set up venv for python scripts
  echo "starting venv"
  source $myDigiRoot/mydigivenv/bin/activate
  # Write to console for admin.
  echo "sensor parameter supplied"
  python $REBOOTSCRIPT
  REBOOTSCRIPT=$null
  # Write to console for admin.
  echo "running sensor gathering"
  python $CLUSTERLOGGINSCRIPT
  ARGUMENTS=$null
  CLUSTERLOGGINSCRIPT=$null
  # Write to console for admin.
  echo "running serviceInit"
  python $SERVICEINITIALIZESCRIPT
  SERVICEINITIALIZESCRIPT=$null
elif [ "$ARGUMENTS" == "servicestart" ]; then
  # Set up venv for python scripts
  echo "starting venv"
  # Set up venv for python scripts
  source $myDigiRoot/mydigivenv/bin/activate
  # Write to console for admin.
  echo "servicestart parameter supplied"
  # Write to console for admin.
  echo "running serviceInit"
  python $SERVICEINITIALIZESCRIPT
  ARGUMENTS=$null
  SERVICEINITIALIZESCRIPT=$null
fi

## *|*|*|*|* End Section 3 *|*|*|*|*

# -10959
# Copyright 2025 mydigifarm
