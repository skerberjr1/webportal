"""
WSGI config for webportal project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/howto/deployment/wsgi/
"""

import sys
import os
import time
import traceback
import signal

from django.core.wsgi import get_wsgi_application

sys.path.append(os.path.dirname(os.path.abspath(__file__))+'/..')
sys.path.append(os.path.dirname(os.path.abspath(__file__))+'/../webportal')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "webportal.settings")

try:
    application = get_wsgi_application()
    print('WSGI without exception')
except Exception:
    print('handling WSGI exception')
    # Error loading applications
    if 'mod_wsgi' in sys.modules:
        traceback.print_exc()
        os.kill(os.getpid(), signal.SIGINT)
        time.sleep(2.5)