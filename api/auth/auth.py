"""
    Authentication Method

    This script defines the admin user (credential generated via env var)
    and the verify_password fcn. The resulting auth object is then imported
    to api_main.py for all the auths.
"""

from os import environ
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash

AUTH = HTTPBasicAuth()

USERS = {
    environ['WEBHOOK_USR']: generate_password_hash(environ['WEBHOOK_PWD'])
}


@AUTH.verify_password
def verify_password(username, password):
    """
    Given a username/password, determine if the login is valid

    :param username:
    :param password:
    :return bool:
    """

    if username in USERS:
        return check_password_hash(USERS.get(username), password)
    return False
