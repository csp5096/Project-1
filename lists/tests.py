from django.urls import resolve
from django.http import HttpRequest
from django.template.loader import render_to_string
from django.test import RequestFactory
from lists.views import home_page
from lists.models import Item

import pytest

#@pytest.mark.usefixtures("rf")
@pytest.mark.django_db
class TestHomeView:

    def test_uses_home_template(self):
        request = RequestFactory().get('/')
        response = home_page(request)
        assert response.status_code == 200

    def test_can_save_a_POST_request(self):
        request = RequestFactory().post('/', data={'item_text': 'A new list item'})
        response = home_page(request)
        assert Item.objects.count() == 1
        new_item = Item.objects.first()
        assert new_item.text == 'A new list item'

    def test_redirects_after_POST(self):
        request = RequestFactory().post('/', data={'item_text': 'A new list item'})
        response = home_page(request)
        assert response.status_code == 302
        assert response['location'] == '/'

    #@pytest.mark.skip(reason='UnboundLocalError: local variable new_text_item')
    def test_only_saves_items_when_necessary(self):
        request = RequestFactory().get('/')
        response = home_page(request)
        assert Item.objects.count() == 0

    def test_displays_all_list_items(self):
        Item.objects.create(text='itemey 1')
        Item.objects.create(text='itemey 2')

        request = RequestFactory().get('/')
        response = home_page(request)

        assert 'itemey 1' in response.content.decode()
        assert 'itemey 2' in response.content.decode()


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







