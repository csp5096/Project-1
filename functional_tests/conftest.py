from selenium import webdriver
from selenium.webdriver.firefox.options import Options

import pytest
import os
import warnings

@pytest.fixture(scope="session")
def driver_get(request):
    options = Options()
    options.set_headless(headless=True)
    web_driver = webdriver.Firefox(firefox_options=options)
    session = request.node
    for item in session.items:
        cls = item.getparent(pytest.Class)
        setattr(cls.obj,"driver",web_driver)
    yield
    web_driver.close()

"""Incremental Pytest Feature"""
def pytest_runtest_makereport(item, call):
    if "incremental" in item.keywords:
        if call.excinfo is not None:
            parent = item.parent
            parent._previousfailed = item

def pytest_runtest_setup(item):
    if "incremental" in item.keywords:
        previousfailed = getattr(item.parent, "_previousfailed", None)
        if previousfailed is not None:
            pytest.xfail("previous test failed (%s)" %previousfailed.name)
