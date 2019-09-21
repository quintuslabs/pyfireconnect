from pyfirebase import pyfirebase
from tests import config


def make_db(service_account=False):
    if service_account:
        c = config.SERVICE_CONFIG
    else:
        c = config.SIMPLE_CONFIG

    return pyfirebase.initialize_app(c).database()
