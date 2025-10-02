### Copyright 2025 mydigifarm
#### License mydigifarm
#### Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
#### The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
#### THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL mydigifarm BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#### Except as contained in this notice, the name of mydigifarm shall not be used in advertising or otherwise to promote the sale, use or other dealings in this Software without prior written authorization from mydigifarm.
#### mydigifarm.com
#### EFFECTIVEDATE: 20250929
#### VERSION: 1.0
#### FILE: mydigifarm,1.0,readme.md

### DESCRIPTION: Backend readme file.  
### LASTMODIFIED: 20250929

#! .md

# digifarm backend api

## Local Project setup

## Prerequisites

- Python 3.x

## Installation

1. Clone the repository:

   ```shell
   git clone <repository_url>

   ```

2. Navigate to the project directory:

   ```shell
   cd webback
   ```

3. Activate virtual environment (if you want, not necessary though):
   for linux/ubuntu/debian

   ```shell
   source env/bin/activate
   ```

4. Install all the required packages:
   ```shell
   pip install -r requirements.txt
   ```

## Usage

1. Make sure you have valid database:

   - Whether you can import dmp into your existing database
     OR
   - Create new one and import dmp

   dmp -> It's provided within team

   - make sure you can access database with your username/password
   - Make sure All tables are there

2. Update Database credentials in:

   - File path where you need to change:
     ```
     mydigifarm_api/settings/base.py
     ```
   - change/update values according to your database/username/password etc:
     ```
     DATABASES = {
         "default": {
             "ENGINE": "django.db.backends.mysql",
             "NAME": "mydigifarm_api",
             "USER": "mydigifarm_api_user",
             "PASSWORD": "mydigifarm_api_password",
             "HOST": "localhost",
             "PORT": "",
         }
     }
     ```

3. Run the webback api:

   ```shell
   python3 manage.py runserver

   ```

## contact

If you are not able to set up database , import dmp etc. contact author of repository or digifarm team

#### -10959
#### Copyright 2025 mydigifarm
