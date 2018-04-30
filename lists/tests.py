from django.urls import resolve
from django.http import HttpRequest
from django.template.loader import render_to_string
from django.test import RequestFactory
from lists.views import home_page, view_list, list_new
from lists.models import Item, List

import pytest

#@pytest.mark.usefixtures("rf")
@pytest.mark.django_db
class TestHomeView:

    @pytest.mark.usefixtures("rf")
    def test_uses_home_template(self):
        request = RequestFactory().get('/')
        response = home_page(request)
        assert response.status_code == 200

@pytest.mark.django_db
class TestListView:

    def test_uses_list_template(self):
        list_ = List.objects.create()
        request = RequestFactory().get(f'/lists/{list_.id}/')
        response = view_list(request, list_id)
        assert response.status_code == 200

    def test_displays_only_items_for_the_list(self):
        correct_list = List.objects.create()
        Item.objects.create(text='itemey 1', list=correct_list)
        Item.objects.create(text='itemey 2', list=correct_list)
        other_list = List.objects.create()
        Item.objects.create(text='other list item 1', list=other_list)
        Item.objects.create(text='other list item 2', list=other_list)

        request = RequestFactory().get(f'/lists/{correct_list.id}/')
        response = view_list(request, list_id)

        assert 'itemey 1' in response.content.decode()
        assert 'itemey 2' in response.content.decode()

@pytest.mark.django_db
class TestNewList:

    def test_can_save_a_POST_request(self):
        request = RequestFactory().post('/lists/new', data={'item_text': 'A new list item'})
        response = list_new(request)
        assert Item.objects.count() == 1
        new_item = Item.objects.first()
        assert new_item.text == 'A new list item'

    def test_redirects_after_POST(self):
        request = RequestFactory().post('/lists/new', data={'item_text': 'A new list item'})
        response = list_new(request)
        new_list = List.objects.first()
        assert response['location'] == f'/lists/{new_list.id}/'

@pytest.mark.django_db
class TestListAndItemModel:

    def test_saving_and_retrieving_items(self):
        list_ = List()
        list_.save()

        first_item = Item()
        first_item.text = 'The first (ever) list item'
        first_item.list = list_
        first_item.save()

        second_item = Item()
        second_item.text = 'Item the second'
        second_item.list = list_
        second_item.save()

        save_list = List.objects.first()
        assert save_list == list_

        saved_items = Item.objects.all()
        assert saved_items.count() == 2

        first_saved_item = saved_items[0]
        second_saved_item = saved_items[1]
        assert first_saved_item.text == 'The first (ever) list item'
        assert first_saved_item.list == list_
        assert second_saved_item.text == 'Item the second'
        assert second_saved_item.list == list_







