"""
    Common API endpoints + versions
"""

# Package imports
from flask import Flask, json
from flask_restful_swagger_2 import Api

# local imports
from api.v1 import APP_V1, Index

##########################################################################
# BEGIN Flask Config
##########################################################################

APP = Flask(__name__)

# Limit overall size to 1 mb
APP.config['MAX_CONTENT_LENGTH'] = 1 * 1024 * 1024

API = Api(APP,
          api_version=None,
          api_spec_url='/docs/swagger',
          description='Eloqua Webhook Integration API',
          terms='Apache License',
          title='ELQ-WEBHOOK')

json.JSONEncoder(ensure_ascii=False)

##########################################################################
# END Flask Config
##########################################################################

##########################################################################
# BEGIN Blueprint Registration
##########################################################################

APP.register_blueprint(APP_V1, url_prefix='/api/v1')

##########################################################################
# END Blueprint Registration
##########################################################################

##########################################################################
# BEGIN Endpoint registration
##########################################################################

API.add_resource(Index, '/', endpoint='index')

##########################################################################
# END Endpoint registration
##########################################################################
