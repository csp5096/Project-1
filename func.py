import pytest
from splinter import Browser

@pytest.yield_fixture(scope='session')
def browser():
    b = Browser()
    yield b
    b.quit()

url = 'http://localhost:8000'

def test_check_homepage(browser):
    browser.visit(url)
    assert browser.is_text_present('Django')