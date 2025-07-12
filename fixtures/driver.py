import allure
import pytest

from conf.browser_factory import BrowserFactory

@allure.title("Initiate driver")
@pytest.fixture(scope="module")
def driver(request, browser, headless):
    """Provide Selenium WebDriver instance"""
    driver_instance = BrowserFactory().get(browser, headless=headless)

    def close_driver():
        if driver_instance:
            driver_instance.close()
            driver_instance.quit()

    request.addfinalizer(close_driver)
    return driver_instance