from django.urls import resolve
from lists.views import home_page

import pytest

@pytest.mark.django_db
class TestHomePage():

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        assert found.func == home_page







