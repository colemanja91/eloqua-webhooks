"""
    API V1
    Expose classes as endpoints
"""

# Package imports
from flask import Blueprint
from flask_restful_swagger_2 import Api

# Local imports
from .index import Index
from .form_repost import ElqRepost

################################################################################
# BEGIN Flask Config
################################################################################

APP_V1 = Blueprint('api_v1', __name__)
API = Api(APP_V1,
          api_version='1.0',
          api_spec_url='/docs/swagger',
          title='Eloqua Webhook Integration API')

################################################################################
# END Flask Config
################################################################################

################################################################################
# BEGIN Route Config
################################################################################

API.add_resource(Index, '/', endpoint='index')
API.add_resource(ElqRepost, '/elq-repost', endpoint='elqrepost')

################################################################################
# END Route Config
################################################################################
