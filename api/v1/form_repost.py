"""
    Repost route
    /api/v1/elq-repost

    Returns 200 status code; reposts data to Eloqua
"""

from os import environ
import logging
import requests

from flask import Response, request
from flask_restful_swagger_2 import Resource

from api.auth.auth import AUTH
from api.v1.form_field_map import hb_elq_fieldmap
from api.v1.form_querystring_params import parse_qstring

# Constants

LOGGER = logging.getLogger(__name__)

ELQ_SITE_ID = environ['ELQ_SITE_ID']
ELQ_HTML_FORM_NAME = environ['ELQ_HTML_FORM_NAME']

# Functions

def data_prep(webhook_data, qstring_data):
    """
    Process incoming data from Hubspot webhook

    :param dict webhook_data: Incoming webhook JSON from Hubspot
    :param dict qstring_data: pre-parsed data from incoming querystring params
    :return dict:
    """

    mapped_data = hb_elq_fieldmap(webhook_data)

    mapped_data.update(qstring_data)

    return mapped_data


def elq_post(data):
    """
    POST a payload to the Eloqua form defined in secret

    :param dict data: Payload of data to repost
    :return bool: whether or not POST was successful
    """

    url = 'https://s{site_id}.t.eloqua.com/e/f2'.format(site_id=ELQ_SITE_ID)

    querystring = {'elqSiteID': ELQ_SITE_ID,
                   'elqFormName': ELQ_HTML_FORM_NAME}

    req = requests.post(url, params=querystring, data=data)

    if req.status_code == 200:
        if req.content != b'\r\n':
            status = False
        else:
            status = True
    else:
        status = False

    LOGGER.info('Repost attempt made with success: %s', status)

    if status is False:
        LOGGER.warning('Repost status code: %s', req.status_code)
        LOGGER.warning('Repost response body: %s', req.json())

    return status


class ElqRepost(Resource):
    """ repost route """

    @AUTH.login_required
    def post(self):
        """ Process repost, send to Eloqua """

        data = request.json

        headers = request.headers

        if headers['User-Agent'] != 'HubSpot Workflows Webhook':
            return Response(status=403)

        qstring_data = parse_qstring(request)

        mapped_data = data_prep(data, qstring_data)

        status = elq_post(mapped_data)

        if status is True:
            return Response(status=200)

        return Response(status=400)
