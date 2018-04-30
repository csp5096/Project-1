import pytest

@pytest.fixture()
def rf():
    """RequestFactory instance"""

    from django.test.client import RequestFactory

    return RequestFactory()