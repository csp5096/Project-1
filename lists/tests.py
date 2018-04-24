from django.urls import resolve
from django.http import HttpRequest
from django.template.loader import render_to_string
from django.test import RequestFactory
from lists.views import home_page
from lists.models import Item

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

@pytest.mark.django_db
class TestItemModel:

    def test_saving_and_retrieving_items(self):
        first_item = Item()
        first_item.text = 'The first (ever) list item'
        first_item.save()

        second_item = Item()
        second_item.text = 'Item the second'
        second_item.save()

        saved_items = Item.objects.all()
        assert saved_items.count() == 2

        first_saved_item = saved_items[0]
        second_saved_item = saved_items[1]
        assert first_saved_item.text == 'The first (ever) list item'
        assert second_saved_item.text == 'Item the second'








