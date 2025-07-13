from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from conf.logger import get_logger
from conf.settings import Timeouts


class BasePageLocators:
    TITLE = (By.XPATH, '//title')


class AbsBasePage:

    def __init__(self, driver, url=None):
        self.base_url = url
        self.driver = driver
        self.logger = get_logger('Main')

    def open(self, timeout=Timeouts.SHORT):
        if self.base_url is None:
            raise Exception('base_url is not set')
        self.logger.substep(f'Visit website: {self.base_url}')
        self.driver.get(self.base_url)
        self.wait_for_page_to_load(timeout)
        return self

    def wait_for_page_to_load(self, timeout: int = Timeouts.SHORT):
        self.wait_for_presence_of_element_located(*BasePageLocators.TITLE, timeout=timeout)
        return self

    def wait_for_presence_of_element_located(self, how: str, what: str, timeout: int) -> bool:
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located((how, what))
            )
        except TimeoutException:
            return False
        return True

    def wait_for_element_to_be_enabled(self, how: str, what: str, timeout: int) -> bool:
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable((how, what)))
        except TimeoutException:
            return False
        return True

    def wait_for_visibility_of_element_located(self, how: str, what: str, timeout: int) -> bool:
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located((how, what))
            )
        except TimeoutException:
            return False
        return True

    def force_click(self, how, what):
        element = self.driver.find_element(how, what)
        self.driver.execute_script("arguments[0].click();", element)
