# Copyright 2025 mydigifarm
# License mydigifarm
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL mydigifarm BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
# Except as contained in this notice, the name of mydigifarm shall not be used in advertising or otherwise to promote the sale, use or other dealings in this Software without prior written authorization from mydigifarm.
# mydigifarm.com
# EFFECTIVEDATE: 20240106
# VERSION: 1.0
# FILE: mydigifarm,1.0,vault_setup.py

# DESCRIPTION: Sets up the vault service for mydigifarm. This includes installing vault, setting up the config file, generating a self-signed cert, and running the vault service.
# LASTMODIFIED: 20250723

#! .py

## *|*|*|*|* Start Section 1 *|*|*|*|*
## Section 1 covers the basic setup of variables and library configurations. 
## This is used to set initial variables and prepare for setup or service runs.
## *|*|*|*|* Section 1 *|*|*|*|*

# Initial imports for the OS, time, parameters and subprocesses. 
import os
import time
import subprocess
import argparse
import re

# Defining the expected arguments accepted by the script. These are used to determine what type of actions will be performed later in the script. 
arg_parser = argparse.ArgumentParser()
arg_parser.add_argument('-i','--install',help='run the installer', action=argparse.BooleanOptionalAction)
arg_parser.add_argument('-s','--startup',help='start and unlock vault', action=argparse.BooleanOptionalAction)
arg_parser.add_argument('-c','--configure',help='used to set the config', action=argparse.BooleanOptionalAction)
arg_parser.add_argument('-r','--reconfigure',help='used to update certificate', action=argparse.BooleanOptionalAction)
arg_parser.add_argument('-k','--generate',help='generate token',action=argparse.BooleanOptionalAction)
parsed_args = arg_parser.parse_args()

# Setting a os param to tell vault to shut up. we know it's an alright cert.
os.environ['VAULT_SKIP_VERIFY'] = 'True'

# Defining a few paths that are expected to be needed while setting up or running this script. 
relative_path = os.path.dirname(__file__)
relative_user = os.path.dirname(os.path.dirname(__file__))
vault_base = f'{relative_path}'
base_key_path = f'{vault_base}/keys'
unseal_key_path = f'{base_key_path}/unseal_keys'
root_key_path = f'{base_key_path}/root_key'
cert_path = f'{relative_path}/cert'
cert_input_path = f'{relative_path}/config/ssl_input'
web_key_path = f'{relative_path}/web_key.txt'
template_path = f'{relative_path}/config/template.hcl'
config_path = f'{relative_path}/config/vault.server.hcl'

## *|*|*|*|* End Section 1 *|*|*|*|*

## *|*|*|*|* Start Section 2 *|*|*|*|*
## Section 2 covers setting up classes and functions. 
## This is where the functions are created that do all of the work for both setting up the vault as well as running the service on reboots. 
## Most functions are created here and used in the next section. 
## *|*|*|*|* Section 2 *|*|*|*|*
# This function runs the requests as a subprocess. 
def run_process(command_array, cap_out, use_shell):
    if cap_out:
        captured_output = subprocess.run(command_array, capture_output=True, shell=True)
        return captured_output
    if use_shell:
        subprocess.run(command_array, shell=True)
    else:
        subprocess.run(command_array)

# This function gets the current IP Address used for setting up vault. 
def get_ip_address():
    if_raw = subprocess.run('ip addr', capture_output=True, shell=True)
    output_lines = if_raw.stdout.decode('utf-8').split('\n')    
    for line in output_lines:
        if 'inet ' in line and not ('127.0.0.1' in line):
            ip = line.lstrip(' ').split(' ')[1].split('/')[0]
            return(ip)

# This outputs the demo keyfile. 
def output_keyfile(input, key_type):
    out_path = f'{base_key_path}/{key_type}'
    with open(out_path, 'w') as key_out:
        if input.__class__ == list:
            key_out.writelines(line+'\n' for line in input)
            return()
        key_out.writelines(input)

# This exports the token handed to the function.
def output_token(token_input, out_path):
    with open(out_path, 'w') as token_file:
        token_file.write(token_input)

# This function deals with ansi escapes in the command capture
def ansi_escape(input_text):
    ansi_escape = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')
    return ansi_escape.sub('',input_text)

# This function takes the stream input and outputs the bits we need.
def export_keys(init_output):
    unseal_keys = []
    decode_out = ansi_escape(input_text=str(init_output.stdout.decode('UTF-8')))
    for line in decode_out.split('\r\n'):
        if 'Unseal' in line:
            unseal_keys.append(str(line.split(':')[1]).strip(' ')) 
        if 'Root' in line:
            root_key = str(line.split(':')[1]).strip(' ')
            output_keyfile(input=root_key, key_type='root_key')
    output_keyfile(input=unseal_keys, key_type='unseal_keys')

# This function runs the commands for creating a self signed cert
def create_self_signed_cert(cert_commands):
    command = cert_commands[0]
    run_process(command_array=command, cap_out=False, use_shell=True)

# This function checks for input cert and key from our users it returns true or false depending on the finding
def check_input_cert(cert_input_path):
    keycheck = run_process(command_array=f'ls {cert_input_path}/*.key', cap_out=True, use_shell=True)
    certcheck = run_process(command_array=f'ls {cert_input_path}/*.crt', cap_out=True, use_shell=True)
    if keycheck.returncode == 0 and certcheck.returncode == 0:
        print(f'cert in check at {cert_input_path} was true')
        return True
    else:
        print(f'cert in check at {cert_input_path} was false')
        return False
        
# This interprets the return of check input and either copies the files or creates a self signed cert
def run_ssl_routine(input_cert_path, copy_input_cert_commands, self_signed_cert_commands):
    if check_input_cert(input_cert_path):
        print('should run commands')
        for command in copy_input_cert_commands:
            print(f'run command: {command}')
            run_process(command_array=command, cap_out=False, use_shell=True)
    else:
        create_self_signed_cert(cert_commands=self_signed_cert_commands)

# Wrapper to run the intall commands
def run_install(install_commands):
    for install_command in install_commands:
        run_process(command_array=install_command, cap_out=False, use_shell=True)

# Wrapper to run the launch commands
def run_launch(launch_commands):
    for launch_command in launch_commands:
        run_process(command_array=launch_command, cap_out=False, use_shell=True)
        time.sleep(5)

# Wrapper to run the init commands
def run_init(init_commands):
    for init_command in init_commands:
        time.sleep(2)
        ls_cap = run_process(command_array=init_command, cap_out=True, use_shell=True)
        export_keys(init_output=ls_cap)


# Read the key output and retun the data
def read_key_file(path):
    with open(path, 'r') as key_file:
        keys = key_file.read()
        print('Read key: '+keys)
        return keys
    
# Setup the KV stache 
def run_kv_setup(kv_setup_commands):
    for setup_command in kv_setup_commands:
        print(setup_command)
        run_process(command_array=setup_command, cap_out=False, use_shell=True)

# This unlocks the vault based on the previously output keys and tokens.
def run_unlock(unlock_commands, unseal_key_path):
    i = 0
    unseal_keys_return = read_key_file(path=unseal_key_path)
    unseal_keys = unseal_keys_return.split('\n')
    for key in unseal_keys:
        print(key)
        unlock_command = str(unlock_commands[0])+key+'"'
        print('unlock command str: '+unlock_command)
        run_process(command_array=unlock_command, cap_out=False, use_shell=True)
        i = i + 1
        if i == 3:
            return()

# This will generate a token. 
def run_generate_token(generate_token_commands, web_key_path):
    for generate_command in generate_token_commands:
        web_token = run_process(command_array=generate_command, cap_out=True, use_shell=True)
        web_token_for_export = web_token.stdout.decode('UTF-8')
        for line in web_token_for_export.split('\n'):
            if 'token ' in line:
                token = line.replace('token','').replace(' ','')
                print(token)
                output_token(token_input=token, out_path=web_key_path)

# This logins into vault so it can be used by the application. 
def run_login(login_commands, path):
    root_key = read_key_file(path=path)
    login_command = login_commands[0]+root_key+'"'
    print(login_command)
    run_process(command_array=login_command, cap_out=False, use_shell=True)

# If you can believe it, gets the ip address
ip_address = get_ip_address()

# Vault skip verify var. Used to tell vault to ignore the self signed cert
vault_skip_verify = "VAULT_SKIP_VERIFY=True"

# These are the expected commands the functions above use that are required to setup and run vault.
install_commands = [ 
            'sudo apt update',
            'sudo apt upgrade -y',
            'wget -O- https://apt.releases.hashicorp.com/gpg | sudo gpg --yes --dearmor -o /usr/share/keyrings/hashicorp-archive-keyring.gpg',
            'echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/hashicorp-archive-keyring.gpg] https://apt.releases.hashicorp.com $(lsb_release -cs) main" > /etc/apt/sources.list.d/hashicorp.list',
            'sudo apt update',
            'sudo apt install vault -y',
            f'mkdir {relative_path}/config',
            f'mkdir {relative_path}/data',
            f'mkdir {relative_path}/log',
            f'mkdir {relative_path}/cert',
            f'mkdir {relative_path}/keys',
]

launch_commands = [
        f'cd {relative_path} || exit; docker compose up -d'
        ]

init_commands = [
        f'docker exec -it mydigifarm-vault /bin/sh -c "{vault_skip_verify} vault operator init"'
        ]

unlock_commands = [
        f'docker exec -it mydigifarm-vault /bin/sh -c "{vault_skip_verify} vault operator unseal '
        ]

vault_login_commands = [
        f'{vault_skip_verify} vault login "'
        ]

kv_setup_commands = [
        'vault secrets enable -path=mydigifarm-kv kv',
        f'vault policy write mydigifarm-kv {relative_path}/config/mydigifarm-kv.hcl',
        'vault kv put mydigifarm-kv/system/webauth/database username=pi@localhost password=Potato123',
        'vault kv put mydigifarm-kv/web/example key1=value1 key2=value2'
        ]

generate_ssl_cert_commands = [
        'openssl req -x509 -sha256 '
        '-days 365 '
        '-nodes '
        '-newkey rsa:4096 '
        '-subj "/CN=mydigifarm/C=US/L=ME" '
        f'-addext "subjectAltName = DNS:{os.uname()[1]},DNS:localhost,IP.1:{ip_address},IP.2:127.0.0.1" '
        f'-keyout {cert_path}/vault.key '
        f'-out {cert_path}/vault.crt'
]

copy_input_cert_commands = [
        f'cp {cert_input_path}/*.key {cert_path}/vault.key',
        f'cp {cert_input_path}/*.crt {cert_path}/vault.crt'
        ]

generate_token_commands = [
        'vault token create -renewable -display-name="web-key" -policy="mydigifarm-kv"'
        ]

## *|*|*|*|* End Section 2 *|*|*|*|*

## *|*|*|*|* Start Section 3 *|*|*|*|*
## Section 3 The code below typically calls the functions created in section 2 in a logical order. 
## Based on the arguments presented to the script, one of the following if statements will run.
## *|*|*|*|* Section 3 *|*|*|*|*

# Used for do the initial installation and setup of vault. 
if parsed_args.install:
    run_install(install_commands=install_commands)
    run_ssl_routine(input_cert_path=cert_input_path, copy_input_cert_commands=copy_input_cert_commands, self_signed_cert_commands=generate_ssl_cert_commands )
    run_launch(launch_commands=launch_commands)
    run_init(init_commands=init_commands)
    run_unlock(unlock_commands=unlock_commands, unseal_key_path=unseal_key_path)

# Used to reconfigure the vault with new ssl certs
if parsed_args.reconfigure:
    run_ssl_routine(input_cert_path=cert_input_path, copy_input_cert_commands=copy_input_cert_commands, self_signed_cert_commands=generate_ssl_cert_commands )
    run_process(command_array=f'cd {relative_path} || exit; docker compose down', cap_out=False, use_shell=True)
    run_launch(launch_commands=launch_commands)
    run_unlock(unlock_commands=unlock_commands, unseal_key_path=unseal_key_path)

# Used to start the vault services. 
if parsed_args.startup:
    run_launch(launch_commands=launch_commands)
    run_unlock(unlock_commands=unlock_commands, unseal_key_path=unseal_key_path)

# Used to configure vault for mydigifarm usage. 
if parsed_args.configure:
    run_login(login_commands=vault_login_commands, path=root_key_path)
    run_kv_setup(kv_setup_commands=kv_setup_commands)
    run_generate_token(generate_token_commands=generate_token_commands, web_key_path=web_key_path)

# This will regenerate the webtoken if need be
if parsed_args.generate:
    run_generate_token(generate_token_commands=generate_token_commands, web_key_path=web_key_path)

## *|*|*|*|* End Section 3 *|*|*|*|*

# -10959
# Copyright 2025 mydigifarm
