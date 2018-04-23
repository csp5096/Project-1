from django.urls import resolve
from django.http import HttpRequest
from django.template.loader import render_to_string
from lists.views import home_page

import pytest

@pytest.mark.django_db
class TestHomePage:

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        assert found.func == home_page

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = home_page(request)
        html = response.content.decode('utf8')
        expected_html = render_to_string('home.html')
        assert html == expected_html








