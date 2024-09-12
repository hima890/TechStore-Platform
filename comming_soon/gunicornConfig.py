import os

# Paths to include
project_path = '/home/ubuntu/TechStore/TechStore-Platform/comming_soon'
venv_site_packages = '/home/ubuntu/TechStore/TechStore-Platform/comming_soon/soon/lib/python3.8/site-packages'

# Set the PYTHONPATH
os.environ['PYTHONPATH'] = "{}:{}".format(project_path, venv_site_packages)

bind = '127.0.0.1:5003'
workers = 3
accesslog = '/var/log/gunicorn/access.log'
errorlog = '/var/log/gunicorn/error.log'
loglevel = 'info'

