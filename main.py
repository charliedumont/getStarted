""" Main definition of routes etc for Google App Engine """
#!/usr/bin/env python
# Lint can't comb this directory properly
#pylint: disable=import-error
from webapp2 import WSGIApplication, Route

from google.appengine.ext import vendor
# Add any libraries installed in the "lib" folder.
vendor.add('lib')
vendor.add('myLib')


# Map URLs to handlers
ROUTES = [
    # This is for resetting a demo or dev site
    Route('/reset_demo/', handler='tools.demo_set.DataManager'),
    Route('/api/echo', handler='jess.echo.Interface'),
    Route('/api/echo/', handler='jess.echo.Interface'),
    Route('/api/echo/<words>', handler='jess.echo.Interface')

]

# webapp2 config
APP_CONFIG = {
    'webapp2_extras.sessions': {
        'cookie_name': '_simpleauth_sess',
        'secret_key': 'SESSION_KEY'
        },
    'webapp2_extras.auth': {
        'user_model': 'models.User',
        'user_attributes': []
        }
    }
# WSGI expects this to be named app
#pylint: disable=invalid-name
app = WSGIApplication(ROUTES, config=APP_CONFIG, debug=True)
