"""
    Index route
    /

    Returns 200 status code
"""

from flask import Response
from flask_restful_swagger_2 import Resource

class Index(Resource):
    """ index route """
    def get(self):
        """ return 200 """
        return Response(status=200)
