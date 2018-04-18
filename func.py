import pytest
from selenium import webdriver

@pytest.mark.nondestructive
def test_browser(selenium):
    #driver = webdriver.Firefox()
    selenium.get('http://localhost:8000')
    #assert 'Django' in driver.title