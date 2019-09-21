import pytest

from tests.tools import make_db


@pytest.fixture(scope='session')
def db():
    # To make it easier to test, we keep the test restricted to firebase_tests
    # Because of the current mutations on calls, we return it as a function.
    try:
        yield lambda: make_db(service_account=False).child('pyfireconnect_tests')
    finally:
        pass
        #make_db(service_account=False).child('pyfireconnect_tests').remove()
