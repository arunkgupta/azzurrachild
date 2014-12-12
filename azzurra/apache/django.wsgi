import os
import sys
import site


paths = [ '/var/www/azzurrabox/azzurra/',
          '/var/www/azzurrabox/azzurra',
          '/var/www/galbiatibox/lib/python2.7/site-packages/',
]

for path in paths:
    if path not in sys.path:
        sys.path.append(path)


# Add the site-packages of the chosen virtualenv to work with
site.addsitedir('/var/www/azzurrabox/azzurra/lib/python2.7/site-packages')

# Add the app's directory to the PYTHONPATH
sys.path.append('/var/www/azzurrabox')
sys.path.append('/var/www/azzurrabox/azzurra')

os.environ['DJANGO_SETTINGS_MODULE'] = 'azzurra.settings'

# Activate your virtual env
activate_env=os.path.expanduser("/var/www/galbiatibox/bin/activate_this.py")
execfile(activate_env, dict(__file__=activate_env))

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()