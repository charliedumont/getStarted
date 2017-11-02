#pylint: disable=too-few-public-methods
""" File for holding GAE Datastore models """
#pylint: disable=import-error
import webapp2_extras.appengine.auth.models
from webapp2_extras import security

from google.appengine.ext import ndb


class User(webapp2_extras.appengine.auth.models.User):
    """ Basic user model required by webapp2 """
    def set_password(self, raw_password):
        """Sets the password for the current user

        :param raw_password:
            The raw password which will be hashed and stored
        """
        #pylint: disable=attribute-defined-outside-init
        self.password = security.generate_password_hash(raw_password, length=12)



