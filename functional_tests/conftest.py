from selenium import webdriver
#from lazy_django import get_django_version, skip_if_no_django

import pytest
import os
import warnings

@pytest.fixture(scope="session")
def driver_get(request):
    web_driver = webdriver.Firefox()
    session = request.node
    for item in session.items:
        cls = item.getparent(pytest.Class)
        setattr(cls.obj,"driver",web_driver)
    yield
    web_driver.close()

@pytest.fixture(scope='session')
def live_server(request):
    """Run a live Django server in the background during tests

    The address the server is started from is taken from the
    --liveserver command line option or if this is not provided from
    the DJANGO_LIVE_TEST_SERVER_ADDRESS environment variable.  If
    neither is provided ``localhost:8081,8100-8200`` is used.  See the
    Django documentation for it's full syntax.

    NOTE: If the live server needs database access to handle a request
          your test will have to request database access.  Furthermore
          when the tests want to see data added by the live-server (or
          the other way around) transactional database access will be
          needed as data inside a transaction is not shared between
          the live server and test code.

          Static assets will be served for all versions of Django.
          Except for django >= 1.7, if ``django.contrib.staticfiles`` is not
          installed.
    """
    #skip_if_no_django()
    addr = request.config.getvalue('liveserver')
    if not addr:
        addr = os.getenv('DJANGO_LIVE_TEST_SERVER_ADDRESS')
    if not addr:
        addr = os.getenv('DJANGO_TEST_LIVE_SERVER_ADDRESS')
        if addr:
            warnings.warn('Please use DJANGO_LIVE_TEST_SERVER_ADDRESS'
                          ' instead of DJANGO_TEST_LIVE_SERVER_ADDRESS.',
                          DeprecationWarning)
    if not addr:
        addr = 'localhost:8000'
    server = live_server_helper.LiveServer(addr)
    request.addfinalizer(server.stop)
    return server

@pytest.fixture(autouse=True, scope='function')
def live_server_helper(request):
    """Helper to make live_server work, internal to pytest-django.

    This helper will dynamically request the transactional_db fixture
    for a test which uses the live_server fixture.  This allows the
    server and test to access the database without having to mark
    this explicitly which is handy since it is usually required and
    matches the Django behaviour.

    The separate helper is required since live_server can not request
    transactional_db directly since it is session scoped instead of
    function-scoped.
    """
    if 'live_server' in request.funcargnames:
        request.getfuncargvalue('transactional_db')

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



