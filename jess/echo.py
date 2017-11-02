""" RESTfull interface for echo testing"""
import logging

import ndb_json

from pbi.errors import CustomException
from pbi.handlers import BaseRequestHandler

class Interface(BaseRequestHandler):
    """ Interface class """

    def get(self, words=None):
        """ GET request endpoint """
        try:
            if words is None:
                details = "You didn't give me anything"
                raise CustomException(details=details)
        except CustomException as cex:
            logging.info(cex.details)
            cex.respond(response=self.response, status=400)
            return
        json_dict = {"words": words}
        self.response.write(ndb_json.dumps(json_dict))
