from django.urls import resolve
from django.http import HttpRequest
from django.template.loader import render_to_string
from django.test import RequestFactory
from lists.views import home_page

import pytest

@pytest.mark.django_db
class TestHomeView:

    def test_uses_home_template(self):
        request = RequestFactory().get('/')
        response = home_page(request)
        assert response.status_code == 200

    def test_can_save_a_POST_request(self):
        request = RequestFactory().post('/', data={'item_text': 'A new list item'})
        response = home_page(request)
        assert 'A new list item' in response.content.decode()








