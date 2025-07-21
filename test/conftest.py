import logging
import time
from datetime import datetime

import pytest

from conf import settings
from conf.path_conf import SCREENSHOTS_DIR

pytest_plugins = ("fixtures.driver"
                  )

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Browser")
    parser.addoption("--headless", action="store_true", default=False, help="Run browser in headless mode")

@pytest.fixture(scope='session')
def browser(request):
    """Returns name of browser"""
    return request.config.getoption("--browser")


@pytest.fixture(scope='session')
def headless(request):
    """Returns True if Browser is in headless mode"""
    return request.config.getoption("--headless")


@pytest.fixture(scope='session')
def env():
    """Returns environment"""
    return settings.ENV

# set up a hook to be able to check if a test has failed
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # execute all other hooks to obtain the report object
    outcome = yield
    rep = outcome.get_result()

    # set a report attribute for each phase of a call, which can
    # be "setup", "call", "teardown"

    setattr(item, "rep_" + rep.when, rep)


# check if a test has failed
@pytest.fixture(scope="function", autouse=True)
def test_failed_check(request, driver):
    yield
    # request.node is an "item" because we use the default
    # "function" scope
    if request.node.rep_setup.failed:
        logging.info(f"setting up a test failed! {request.node.nodeid}")
    elif request.node.rep_setup.passed:
        if request.node.rep_call.failed:
            take_screenshot(driver)
            logging.info(f"executing test failed {request.node.nodeid}")


# make a screenshot with a name of the test, date and time
def take_screenshot(driver):
    if settings.LOG_LEVEL == 'DEBUG':
        time.sleep(1)

        file_name = str(SCREENSHOTS_DIR / f'{datetime.today().strftime("%Y%m%d%H%M%S")}.png')
        driver.save_screenshot(file_name)
        logging.info(f"Saved screenshot as {file_name}")


@pytest.fixture
def shopping_context():
    return dict(cart_items=[],
                cart_total=0)