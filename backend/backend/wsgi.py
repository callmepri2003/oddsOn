import os
import sys

# Add outer backend folder to sys.path
path = '/home/pri20032003/backend'  # replace with your PythonAnywhere username
if path not in sys.path:
    sys.path.append(path)

# Set the Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
