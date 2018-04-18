import pytest
from splinter import Browser

@pytest.yield_fixture(scope='session')
def browser():
    b = Browser()
    yield b
    b.quit()

BASE_URL = 'http://localhost:8000'

def url(route):
    return '{}/{}'.format(BASE_URL, route)

# Edith has heard about a cool new online to-do app.

def test_can_check_homepage(browser):
    # She goes to check out its homepage
    browser.visit(url('/'))

    # She notices the page title and header mention to-do lists
    assert 'To-Do' in browser.title

    # She is invited to enter a to-do item straight away

    # She types "Buy peacock feathers" into a text box
    # (Edith's hobby is trying fly-fishing lures)

    # When she hits enter, the pages updates, and now the page lists
    # "1: Buy peacock feathers" as an item in a to-do list

    # There is still a text box inviting her to add another item.
    # She enters "Use peacock feathers to make a fly"
    # (Edith is very methodical.)

    # The page updates again, and now shows both items on here list

    # Edith wonders whether the site will remember here lists.
    # Then she sees that the site had generated a unique URL for her.
    # The is some explanatory text to that effect.

    # She visits that URL - her to-do list is still there.

    # Satisfied, she goes back to sleep

    # Browser.quit()

