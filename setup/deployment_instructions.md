# Environment Setup
**In `~/.ssh` append your public key to `authorized_keys`.**
```
vi .ssh/authorized_keys
```

## Install Packages
**Install the following Ubuntu packages.**
```bash
sudo apt-get update -y
sudo apt-get install apache2 -y
sudo apt-get install python3-pip -y
sudo apt-get install libapache2-mod-wsgi-py3 -y
sudo apt-get install python-virtualenv -y
sudo apt-get install git -y
sudo apt-get install mysql-server -y
sudo apt-get install python-mysqldb -y
sudo apt-get build-dep python-mysqldb -y
```
Clue: Copy the lines into a file called `install.sh` and install it using `sudo sh install.sh`. Remember to remove the file after the packages are installed.

## Virtual Environment & Clone Project
### Create Virtual Environment
**In `/var/www`, create the virtual environment.**

```bash
sudo virtualenv -p python3.6 blackbee_io
```
Clue: Check that the python version is correct using `source blackbee_io/bin/activate` and then running Python. While in the Python command line, use `exit()` to exit from the command line.

**Change the permissions of the `blackbee_io` folder.**
```bash
sudo chown -R ubuntu: blackbee_io/
```
Clue: Check that the permissions are correct using `ls -la`

### Get the Source Code from Bitbucket
#### Generate SSH Key
**Create the public-private key pair in `~/.ssh`.**
```bash
ssh-keygen
```
#### `git clone` from Code Repositiory
Clue: Before starting this step, use `cat ~/.ssh/id_rsa.pub` to get the public key and store this in Access Keys in Bitbucket. This way, this server can `git pull` from the code repository.
**In `/var/www/blackbee_io`, clone the Python project from the code repositiory.**
```bash
git clone git@bitbucket.org:blackbeelabs/blackbee_io.git
```

### Install Python packages using `pip`
**Activate the virtual environment.**
```bash
source /var/www/blackbee_io/bin/activate
```
**Install the Python packages.**
Clue: The `reuquirements.txt` file resides in `/var/www/blackbee_io/blackbee_io/io_config`.
```bash
pip install -r requirements.txt
```
## Django Configuration

In `/path/to/venv/lib/python3.6/site-packages/django/db/backends/mysql` update `base.py` by adding the following:
```python
try:
    import pymysql
    pymysql.install_as_MySQLdb()
except ImportError:
    pass
```
# Django Project Setup
## Database Configuration
**Start the MySQL server. Then access the server.**
```bash
sudo service mysql start  
sudo mysql -uroot
```
**Create the database and add the applcation user.** 
Clue: Generate the password using the Django Secret Key Generator.
```sql
CREATE DATABASE blackbee_io;
GRANT ALL PRIVILEGES ON blackbee_io.* TO 'username'@'localhost' IDENTIFIED BY 'password';
```

## `settings` of Django Project

**Create the `__init__.py` file at `/var/www/blackbee_io/blackbee_io/django_io_project/django_io_project/settings`**.
```bash
touch __init__.py
```
Then edit `__init__.py` using `vi __init__.py` and add the following lines in:
```python
try:
    from .environment import *
except ImportError:
    pass
```
Clue: `environment` can be `staging` or `production`.

**Create the `environment.py` file. in the same location.** If you are deploying in production, use the following command.
```bash
touch prod.py
```
This file is the settings for your application and it inherits `base.py` and adds the following settings. 
```python
import os
from .base import *

SECRET_KEY = '' # Fill this in
DEBUG = False
ALLOWED_HOSTS = ['blackbeelabs.io']
STATICFILES_DIRS = [
    os.path.join(os.path.dirname(BASE_DIR), 'io_main_app', 'static'),
]
STATIC_ROOT = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(BASE_DIR))), 'static')
ENVIRONMENT = 'PRODUCTION'
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': '', # Fill this in
        'USER': '', # Fill this in
        'PASSWORD': '', # Fill this in
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```
### `static` Files
**Create the `static` folder.**
```bash
mkdir /var/www/blackbee_io/static
```
**Copy the static files into the static folder using `collectstatic`.**
```bash
python manage.py collectstatic
```
Clue: Check the variables `STATICFILES_DIRS` and `STATIC_ROOT` before running `collectstatic`. Also, fix any incorrect code in the Django apps if there are any error messages.

### Migrate Database & Create superuser
**Migrate the database changes using `manage.py`.**
```bash
python manage.py makemigrations
python manage.py makemigrations io_blog_app
python manage.py migrate
```
**Create the superuser in the Django application.**
```bash
python manage.py createsuperuser
```
## Apache Configuration
Go to `/etc/apache2` and update `sites-available/000-default.conf` to the following:
```bash
# Disable display of server information on error pages.
ServerSignature Off
# Only return Apache in the Server header.
ServerTokens Prod

#Other Hardening tools
Timeout 60
MaxClients 5
ThreadsPerChild 5
KeepAliveTimeout 10
LimitRequestFields 50
LimitRequestFieldSize 1024

#Mitigate XSS by setting cookie with HttpOnly and Secure flag
#Header edit Set-Cookie ^(.*)$ $1;HttpOnly;Secure
#Header set X-XSS-Protection "1; mode=block"
<VirtualHost *:80>
    # Domain name
    ServerName blackbeelabs.sg

    # Where apache writes the logs
    ErrorLog ${APACHE_LOG_DIR}/error.log
    CustomLog ${APACHE_LOG_DIR}/access.log combined

    # Aliases
    Alias /static /var/www/blackbee_io/static
    ServerAlias www.blackbeelabs.sg

    # Deny accesss to see the file structure of the application
    <Directory /var/www/blackbee_io/>
        Options -Indexes -Includes -ExecCGI
    </Directory>
    # Allow all requests to access this functionality (static files)
    <Directory /var/www/blackbee_io/static>
        Require all granted
    </Directory>
    # Allow all requests to access this functionality (wsgi file)
    <Directory /var/www/blackbee_io/blackbee_io/django_io_project/django_io_project>
        <Files wsgi.py>
            Require all granted
        </Files>
    </Directory>

    WSGIProcessGroup blackbee
    # Set this to the path of the wsgi file
    WSGIScriptAlias / /var/www/blackbee_io/blackbee_io/django_io_project/django_io_project/wsgi.py
</VirtualHost>
# Set this to the path of the manage.py file, and also the site-packages
WSGIDaemonProcess blackbee python-path=/var/www/blackbee_io/blackbee_io/django_io_project:/var/www/blackbee_io/lib/python3.6/site-packages
```
# Update All Packages
**Update packages and restart the server.**
```bash
sudo apt-get update -y
sudo apt-get upgrade -y
sudo apt-get dist-upgrade -y
sudo shutdown -r 0
```
Clue: You will need to SSH in again to access the server after restart.
# Start the service
In order for `Header edit Set-Cookie ^(.*)$ $1;HttpOnly;Secure` and `Header set X-XSS-Protection "1; mode=block"` to be effective, enable the `headers` module in Apache:
```bash
sudo a2enmod headers
```
**Finally, start the server.**
```bash
sudo systemctl restart apache2
sudo service apache2 restart
```
Clue: If your settings are incorrect, use `apachectl configtest` to debug the XML file.
***
# Security
Note that some of the settings for security purposes are already embedded in the Apache configuration file. In particular, the following settings are already configured:
```bash
ServerSignature Off
ServerTokens Prod
Timeout 60
MaxClients 5
ThreadsPerChild 5
KeepAliveTimeout 10
LimitRequestFields 50
LimitRequestFieldSize 1024
```
## Add a separate user for the process
**Create a new group.**
```bash
sudo groupadd http-web
```
**Create a new user belonging to the group.**
```bash
useradd -d /var/www/blackbee_io -g http-web -s /bin/nologin http-web
```
**Finally, update `/etc/apache2/sites-available/000-default.conf` by adding the following lines in the beginning:**
```bash
#Only allow this user and group to run Apache by editing the virtual hosts file:
User http-web
Group http-web
```
## Install and enable mod_evasive
**Install `mod_evasive`.**
```bash
sudo apt-get install libapache2-mod-evasive -y
```
**Create the log folder for `mod_evasive` and assign this to the `http-web` user and group**
```bash
mkdir /var/log/mod_evasive
sudo chown http-web:http-web /var/log/mod_evasive
```
**Update the configuration for `/etc/apache2/mods-available/evasive.conf`.** 
Update the file to the following configuration:
```bash
<IfModule mod_evasive20.c>
    #max no. of single url page views
    DOSHashTableSize    3097
    #max no. of single site views
    DOSPageCount        16
    #per period of single url page views
    DOSSiteCount        128
    #per period of single site views
    DOSPageInterval     2
    DOSSiteInterval     2
    DOSBlockingPeriod   15

    DOSEmailNotify      blackbeelabs@gmail.com
    #DOSSystemCommand    "su - someuser -c '/sbin/... %s ...'"
    DOSLogDir           /var/log/mod_evasive
</IfModule>
```
***
# SSL
**First, update `/etc/apache2/sites-available/000-default.conf` by adding the following lines, within the `<VirtualHost>` node.**

```bash
    RewriteEngine On
    RewriteCond %{SERVER_PORT} !^443$
    RewriteRule ^(.*)$ https://%{HTTP_HOST}$1 [R=301,L]
```
**Install the SSH Cert using `certbot`.**
Clue: Follow https://linuxhostsupport.com/blog/how-to-install-lets-encrypt-with-apache-on-ubuntu-16-04/ if you're not sure.
```bash
cd /usr/local/sbin
sudo wget https://dl.eff.org/certbot-auto
sudo chmod a+x certbot-auto
certbot-auto --apache -d blackbeelabs.sg
```
**Activate the modules and restart the server.**
```bash
sudo a2ensite default-ssl && sudo a2enmod rewrite && sudo a2enmod ssl
sudo systemctl restart apache2
```
**In `/etc/apache2/sites-available/default-ssl.conf` add the following settings from
`/etc/apache2/sites-available/000-default.conf`.** 
```bash
    ServerName blackbeelabs.sg
    ServerAlias www.blackbeelabs.sg
    DocumentRoot /var/www/html
    # Set this to the path of the wsgi file
    WSGIProcessGroup blackbee
    WSGIScriptAlias / /var/www/blackbee_io/blackbee_io/django_io_project/django_io_project/wsgi.py
```
**In `/etc/apache2/mods-available/ssl.conf` edit the following configurations with the ones below.**
```bash
SSLCipherSuite EECDH+AESGCM:EDH+AESGCM:AES256+EECDH:AES256+EDH
SSLProtocol ALL -SSLv2 -SSLv3
SSLHonorCipherOrder On
```
**Also, add the following configurations.**
```bash
Header always set Strict-Transport-Security "max-age=63072000; includeSubdomains; preload"
        Header always set X-Frame-Options DENY
Header always set X-Content-Type-Options nosniff
```