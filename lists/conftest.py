import pytest
from .lazy_django import get_django_version, skip_if_no_django

@pytest.fixture()
def rf():
    """RequestFactory instance"""
    skip_if_no_django()

    from django.test.client import RequestFactory

    return RequestFactory()