#odoo auto script by acoder(Htet Arkar Kyaw)
import os
import sys
import time
import nginx 
def system_update():
    system_update="\033[35m \t\t\tSystem Update And Upgrade"
    for char in system_update:
        time.sleep(0.2)
        sys.stdout.write(char)
        sys.stdout.flush()
    time.sleep(5)
    os.system('add-apt-repository universe')
    os.system('add-apt-repository "deb http://mirrors.kernel.org/ubuntu/ xenial main"')
    os.system(' apt-get update && upgrade -y')
    os.system(" apt-get install git python3 python3-pip build-essential wget python3-dev python3-venv python3-wheel libxslt-dev libzip-dev libldap2-dev libsasl2-dev python3-setuptools node-less libpng12-0 libjpeg-dev gdebi -y")
    os.system('pip3 install python-nginx')
    time.sleep(3)
    os.system('clear')
def nginx_config():
    web=input("Enter Your Web or IP: ")
    email=input("Enter Admin Email For SSL Cert: ")
    #ssl and serve add
   
    serv=nginx.Server()
    confi=nginx.Conf()
    upstream = nginx.Upstream('odoo',
     nginx.Key('server', '127.0.0.1:8069')
     	)
    nn=nginx.Upstream('odoochat',
     nginx.Key('server', '127.0.0.1:8072')
     	)

    confi.add(upstream,nn)
    serv.add(
    nginx.Key('listen','80'),
    nginx.Key('server_name',web),
    nginx.Key('proxy_read_timeout','720s'),
    nginx.Key('proxy_connect_timeout','720s'),
    nginx.Key('proxy_send_timeout','720s'),

    nginx.Key('proxy_set_header','X-Forwarded-Host $host'),
    nginx.Key('proxy_set_header', 'X-Forwarded-For $proxy_add_x_forwarded_for'),
    nginx.Key('proxy_set_header', 'X-Forwarded-Proto $scheme'),
    nginx.Key('proxy_set_header','X-Real-IP $remote_addr'),
    nginx.Key('access_log','/var/log/nginx/odoo_access.log'),
    nginx.Key('error_log','/var/log/nginx/odoo_error.log'),
    nginx.Location('location /',
              nginx.Key('proxy_pass ', 'http://odooserver')
     ),
    
    nginx.Location(' location ~* /web/static/',
          nginx.Key('proxy_cache_valid', '200 90m'),
          nginx.Key('proxy_buffering','on'),
          nginx.Key('expires','864000'),
          nginx.Key('proxy_pass ', 'http://odooserver'),

     ),
    nginx.Key('gzip_types','text/css text/less text/plain text/xml application/xml application/json application/javascript'),
    nginx.Key('gzip','on'),
    )
    confi.add(serv)
    nginx.dumpf(confi,f'/etc/nginx/sites-available/{web}')
    os.system('service nginx reload')
    os.system(f' sudo ln -s /etc/nginx/sites-available/{web} /etc/nginx/sites-enabled/{web}')
    os.system(f"add-apt-repository ppa:certbot/certbot -y &&  apt-get update -y")
    os.system(f'certbot --nginx -d {web} --noninteractive --agree-tos --email {email} --redirect')
    os.system(f'service nginx reload')
def odoo_config():
    sever_name=input("Enter You Want To Server Name: ")
    os.system(f'touch /etc/systemd/system/{sever_name}.service')
    os.system("echo 'proxy_mode=True' >> /opt/odoo/debian/odoo.conf")
    os.system("echo 'proxy_mode=True' >> /etc/odoo.conf")
    os.system(f'echo  [Service] >> /etc/systemd/system/{sever_name}.service')
    os.system(f'echo  ExecStart=/opt/odoo/bin/python3 /opt/odoo/odoo-bin -c /etc/odoo.conf >> /etc/systemd/system/{sever_name}.service')
    os.system(f'echo  [Install] >> /etc/systemd/system/{sever_name}.service')
    os.system(f'echo  WantedBy=multi-user.target >> /etc/systemd/system/{sever_name}.service')
    time.sleep(30)
def download_odoo():
    os.system("clear")
    owner="\033[31m\t\t\t\t Script By Htet Arkar Kyaw"
    for char in owner:
        time.sleep(0.2)
        sys.stdout.write(char)
        sys.stdout.flush()
    time.sleep(5)
    version=float(input("Enter Odoo Version: "))
    os.system("clear")
    os.system("apt install git -y")
    os.system("clear")
    down_time="\033[35m \t\t\tOdoo Download From Github.\n \t\t\tIt will take time."
    for char in down_time:
        time.sleep(0.2)
        sys.stdout.write(char)
        sys.stdout.flush()
    time.sleep(5)
    os.system("clear")
    os.chdir('/opt')
    os.system(f"git clone https://www.github.com/odoo/odoo --depth 1 --branch {version} /opt/odoo")
    os.system("cp -r /opt/odoo/debian/odoo.conf /etc/")
    print("Download Finish")
    time.sleep(5)
    os.system("clear")
def pogresql_dbcreate():
    #progresql
    print("\033[36m \t\t\t\tPogresql Download")
    time.sleep(5)
    os.system('apt install postgresql postgresql-client -y')
    print('Finsh.....................................')
    time.sleep(5)
    os.system("clear")
    print("Create System User For odoo")
    time.sleep(5)
    os.system("sudo -u postgres createuser -s $USER")
    os.system("createdb $USER")
    print("User Creating Finish.")
    time.sleep(5)
    os.system("clear")
def python_depends():
    print("\t\t\t \033[32m Instllation Python Depend Dependencies")
    time.sleep(5)
    os.system("apt autoremove -y")
    os.system("apt install python3-dev libxml2-dev libxslt1-dev libldap2-dev libsasl2-dev \
    libtiff5-dev libjpeg8-dev libopenjp2-7-dev zlib1g-dev libfreetype6-dev \
    liblcms2-dev libwebp-dev libharfbuzz-dev libfribidi-dev libxcb1-dev libpq-dev -y")
    os.chdir('/opt/odoo')
    os.system("pip3 install -r requirements.txt")
    print("Finish...................")
    time.sleep(10)
    os.system("clear")
def node():
    print("\t\t\t \033[36m Nodjs Installation")
    os.system(" apt install nodejs -y")
    os.system("apt install npm -y")
    os.system(" npm install -g rtlcss  npm install -g rtlcss -y ")
    print("Finish...................")
    time.sleep(5)
    os.system("clear")
def auto():
    os.system("clear")
   # system_update()
   
   # download_odoo()
   # pogresql_dbcreate()
    
    #python_depends()
    #node() 
    nginx_config()
    odoo_config()
    print("\033[32m \t\t\tInstallation Finsh")
    
    time.sleep(3)
    os.system('clear')
auto()
