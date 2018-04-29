from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import pytest
import time

@pytest.mark.usefixtures("driver_get")
@pytest.mark.incremental
class TestNewVistor:

    def wait_for_row_in_list_table(self, row_text):
        """
        Testing helper method 1
        :param row_text:
        :return:
        """
        table = self.driver.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        assert row_text in [row.text for row in rows]

    def test_can_start_a_list_and_retrieve_it_later(self, live_server):
        # Edith has heard about a cool new online to-do app.
        # She goes to check out its homepage
        self.driver.get(live_server.url)

        # She notices the page title and header mention to-do lists
        assert 'To-Do' in self.driver.title
        header_text = self.driver.find_element_by_tag_name('h1').text
        assert 'To-Do' in header_text

        # She is invited to enter a to-do item straight away
        inputbox = self.driver.find_element_by_id('id_new_item')
        assert inputbox.get_attribute('placeholder') == 'Enter a to-do item'

        # She types "Buy peacock feathers" into a text box
        # (Edith's hobby is trying fly-fishing lures)
        inputbox.send_keys('Buy peacock feathers')

        # When she hits enter, the pages updates, and now the page lists
        # "1: Buy peacock feathers" as an item in a to-do list
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Buy peacock feathers')

        # There is still a text box inviting her to add another item.
        # She enters "Use peacock feathers to make a fly"
        # (Edith is very methodical.)
        inputbox = self.driver.find_element_by_id('id_new_item')
        inputbox.send_keys('Use peacock feathers to make a fly')
        inputbox.send_keys(Keys.ENTER)

        # The page updates again, and now shows both items on here list.
        self.wait_for_row_in_list_table('1: Buy peacock feathers')
        self.wait_for_row_in_list_table('2: Use peacock feathers to make a fly')

        # Edith wonders whether the site will remember here lists.
        # Then she sees that the site had generated a unique URL for her.
        # The is some explanatory text to that effect.

        # She visits that URL - her to-do list is still there.

        # Satisfied, she goes back to sleep