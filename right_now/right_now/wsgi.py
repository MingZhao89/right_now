"""
WSGI config for right_now project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/howto/deployment/wsgi/
"""

import os
import sys
import site

# Add the site-packages of the chosen virtualenv to work with
site.addsitedir('/opt/right_now/venv/lib/python2.6/site-packages')

# Add the app's directory to the PYTHONPATH
sys.path.append('/opt/right_now/right_now')
sys.path.append('/opt/right_now/right_now/survey')

os.environ['DJANGO_SETTINGS_MODULE'] = 'right_now.settings'

# Activate the virtual env
activate_env=os.path.expanduser("/opt/right_now/venv/bin/activate_this.py")
execfile(activate_env, dict(__file__=activate_env))

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
