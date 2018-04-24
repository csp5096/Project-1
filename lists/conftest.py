import pytest
from lists import apps

@pytest.fixture(scope='session')
def client():
    apps.config['TESTING'] = True
    return apps.test_client()