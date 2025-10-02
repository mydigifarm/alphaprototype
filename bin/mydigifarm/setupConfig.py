# Copyright 2025 mydigifarm
# License mydigifarm
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL mydigifarm BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
# Except as contained in this notice, the name of mydigifarm shall not be used in advertising or otherwise to promote the sale, use or other dealings in this Software without prior written authorization from mydigifarm.
# mydigifarm.com
# EFFECTIVEDATE: 20250812
# VERSION: 1.0
# FILE: mydigifarm,1.0,setupConfig.py

# DESCRIPTION: Generates a configuration file for mydigifarm based on user input.
# LASTMODIFIED: 20250812

#! .py

## *|*|*|*|* Start Section 1 *|*|*|*|*
## Section 1 covers the basic setup of variables and library configurations. 
## This is used to set initial variables and prepare for setup or service runs.
## *|*|*|*|* Section 1 *|*|*|*|*


# Initial imports for the OS and utility functions.
import os
import shutil
from utils.ReplaceText import replace_text
from utils.getIpAddress import get_ip_address

# Define root paths for config files.
script_root = os.path.dirname(os.path.realpath(__file__))
config_base_dir = f'{script_root}/scripts'
config_template_path = f'{config_base_dir}/config.env.template'
demo_template_path = f'{config_base_dir}/config.env.demotemplate'
config_file_path = f'{config_base_dir}/config.env'

## *|*|*|*|* End Section 1 *|*|*|*|*

## *|*|*|*|* Start Section 2 *|*|*|*|*
## Section 2 covers Function creation along with classes and other more complex objects.  
## Most functions are created here and used in the next section. 
## *|*|*|*|* Section 2 *|*|*|*|*

# Read non-comment variables from a template file
def read_template_vars(file_path):
    with open(file_path, 'r') as template_file:
        file_content = template_file.read()
    config_vars = []
    for line in file_content.split('\n'):
        if not line.startswith('#') and line != '':
            config_vars.append(line)
    return config_vars

# Copy a template config file to the working config
def copy_config_file(template_path, config_path):
    shutil.copyfile(template_path, config_path)

# Prompt the user for input based on a given question
def ask_a_question(question_text, question_key):
    question_value = input(question_text)
    return {question_key: question_value}

# Replace values in the target config file
def run_replace_text(config_file_path, replace_dict):
    replace_text(path=config_file_path, find_and_replace=replace_dict)

# Ask if this is a demo run
def check_for_demo():
    def ask_demo_question():
        return ask_a_question(question_text="Is this a demo? <y|n>: ", question_key="demo_check")
        
    demo_check = {"demo_check": "UNSET"}

    while demo_check["demo_check"].lower() not in ['y', 'n']:
        if demo_check["demo_check"] != "UNSET":
            print(f"Only expecting <Y|N>. You provided: {demo_check['demo_check']}")
        demo_check = ask_demo_question()

    return demo_check["demo_check"].lower() == 'y'

## *|*|*|*|* End Section 2 *|*|*|*|*

## *|*|*|*|* Start Section 3 *|*|*|*|*
## Section 3 executes the configuration logic based on user input.
## Prompts user through different environment settings and writes the config file.
## *|*|*|*|* Section 3 *|*|*|*|*

if __name__ == "__main__":
    replace_dict_list = []

    if check_for_demo():
        copy_config_file(template_path=demo_template_path, config_path=config_file_path)
        hostIP = get_ip_address()
        hostname = os.uname()[1]

        replace_dict_list.append({'DEFAULTDEMOSTATUS': 'True'})

        check_host_ip = ask_a_question(
            question_text=f'Is this the IP of the PI <{hostIP}>? [y|n] <default:y>: ',
            question_key="demoIPAnswer"
        )
        if check_host_ip['demoIPAnswer'].lower() in ['y', '']:
            replace_dict_list.append({"DEFAULTIPADDRESS": hostIP})
        else:
            print(f'Unexpected response: {check_host_ip["demoIPAnswer"]}')

        check_hostname = ask_a_question(
            question_text=f'Is this the hostname of the Pi <{hostname}>? [y|n] <default:y>: ',
            question_key="hostnameAnswer"
        )
        if check_hostname['hostnameAnswer'].lower() in ['y', '']:
            replace_dict_list.append({'LOCALHOSTNAME': hostname})
        else:
            print(f'Unexpected response: {check_hostname["hostnameAnswer"]}')

        check_demo_data = ask_a_question(
            question_text='Do you want to load demo data? [y|n] <default:y>: ',
            question_key='loadDemoData'
        )
        if check_demo_data['loadDemoData'].lower() in ['y', '']:
            replace_dict_list.append({'DEMODATABOOL': 'True'})

        check_demo_clusters = ask_a_question(
            question_text='How many clusters should we set up? [1-5] <default:2>: ',
            question_key="numberOfClusters"
        )
        input_val = check_demo_clusters["numberOfClusters"]

        if input_val.isdigit() and 1 <= int(input_val) <= 5:
            replace_dict_list.append({'NUMBEROFCLUSTERS': input_val})
        else:
            print(f'Invalid cluster number "{input_val}". Setting to default.')
            replace_dict_list.append({'NUMBEROFCLUSTERS': 'DEFAULT'})
    else:
        copy_config_file(template_path=config_template_path, config_path=config_file_path)
        config_vars = read_template_vars(file_path=config_file_path)
        for var in config_vars:
            var_split = var.split('=')
            question_return = ask_a_question(
                question_text=f'{var_split[0]} [{var_split[1]}]: ',
                question_key=var_split[0]
            )
            replace_dict_list.append({var: f'{var_split[0]}={question_return[var_split[0]]}'})

    for replace_item in replace_dict_list:
        print(replace_item)
        run_replace_text(config_file_path=config_file_path, replace_dict=replace_item)

## *|*|*|*|* End Section 3 *|*|*|*|*

# -10959
# Copyright 2025 mydigifarm
