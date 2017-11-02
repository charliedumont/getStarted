""" Our Token tools """
import logging
from datetime import datetime, timedelta
import jwt

from webapp2_extras.appengine.auth.models import User #pylint:disable=import-error

from pbi.config import Config


def extract(headers):
    """ Extract and convert the token from headers """
    token = None
    if 'Authorization' in headers:
        # Strip off "Bearer "
        token = headers['Authorization'][6:]
    if not token:
        return None
    try:
        data = jwt.decode(token,
                          Config.get('main', 'jwt_secret'),
                          algorithms=['HS256'])
        # Expiration
        logging.info(data)
        expires = datetime.utcfromtimestamp(int(data['expires']))
        if expires <= datetime.utcnow():
            return False
        return data
    except jwt.exceptions.InvalidTokenError:
        logging.info("invalid token error")
        return False



def generate(user_id):
    """ function to create a token """
    user = User.get_by_id(user_id)

    expires = datetime.utcnow() + timedelta(days=3)

    toke = jwt.encode(
        {
            "avatar": None,
            "firstname": user.firstname,
            "lastname": user.lastname,
            "email": user.email_address,
            "user_id": user_id,
            "user_type": user.userType,
            "expires": expires.strftime("%s"),
        },
        Config.get('main', 'jwt_secret'),
        algorithm='HS256'
    )
    return toke
