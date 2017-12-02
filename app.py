"""
    run API on server
"""

#!/usr/bin/env python
from os import environ
import logging
from socket import gethostname
from logmatic import JsonFormatter

from api import APP

if 'NAMESPACE' in environ:
    ENV = environ['NAMESPACE']
else:
    ENV = 'local'


# Set logging params
def set_log_levels(level):
    """
    Set log level across all logger/handlers

    :param logging.<LEVEL> level: log level imported from standard logging package
    """
    # Setup JSON logging handler so all outputs log to JSON format
    handler = logging.StreamHandler()
    handler.setFormatter(JsonFormatter(extra={"hostname": gethostname()}))
    handler.setLevel(level)

    # Set logging on underlying server
    server_log = logging.getLogger('werkzeug')
    server_log.setLevel(level)
    server_log.addHandler(handler)

    # Set logger on Flask App
    APP.logger.setLevel(level)
    APP.logger.addHandler(handler)

def get_port():
    """
    get listening port
    """

    if 'ELQ_WEBHOOK_SERVICE_PORT' in environ:
        return int(environ['ELQ_WEBHOOK_SERVICE_PORT'])

    return 5000


if __name__ == '__main__':

    DEBUG_MODE = False

    if ENV == '${OPENSHIFT_PROJECT_NAME_DEV}':
        set_log_levels(logging.DEBUG)
    elif ENV == '${OPENSHIFT_PROJECT_NAME_PROD}':
        set_log_levels(logging.INFO)
    else:
        set_log_levels(logging.DEBUG)
        DEBUG_MODE = True

    APP.run(host='0.0.0.0',
            port=get_port(),
            debug=DEBUG_MODE)
