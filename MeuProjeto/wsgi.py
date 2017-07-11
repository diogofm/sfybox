"""
WSGI config for MeuProjeto project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/howto/deployment/wsgi/
"""

import os
import sys

# ADD YOUR PROJECT TO THE PYTHONPATH FOR THE PYTHON INSTANCE
path = '/home/diogofm/MeuProjeto/'
if path not in sys.path:
    sys.path.append(path)

# IMPORTANTLY GO TO THE PROJECT DIR
os.chdir(path)

# TELL DJANGO WHERE YOUR SETTINGS MODULE IS LOCATED
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "MeuProjeto.settings")

# IMPORT THE DJANGO SETUP - NEW TO 1.7
import django
django.setup()

# IMPORT THE DJANGO WSGI HANDLER TO TAKE CARE OF REQUESTS
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()