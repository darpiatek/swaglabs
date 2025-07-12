from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait


class Element:
    def __init__(self, how: str, what: str, wait=None,
                 wait_timeout: int = 10, name: str = "Element"):
        self._how = how
        self._what = what
        self._obj = None
        self.wait = wait
        self.wait_timeout = wait_timeout
        self.name = name

    def __get__(self, obj, owner):
        self._obj = obj
        return self

    def __repr__(self):
        return f'{self.__class__.__name__}(name="{self.name}", how="{self._how}", what="{self._what}")'

    @property
    def element(self):
        if self.wait is not None:
            return \
                WebDriverWait(self._obj.driver, self.wait_timeout).until(
                    self.wait((self._how, self._what))
                )
        element = self._obj.driver.find_element(self._how, self._what)
        self._obj.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        return element

    def is_present(self) -> bool:
        try:
            return self.element
        except NoSuchElementException:
            return False

    def is_displayed(self) -> bool:
        try:
            return self.element.is_displayed()
        except NoSuchElementException:
            assert False, f"{self!r} is not present on page"

    def is_clickable(self) -> bool:
        try:
            return self.element.is_clickable()
        except NoSuchElementException:
            assert False, f"{self!r} is not present on page"

    def scroll_into_view(self):
        ActionChains(self._obj.driver).move_to_element(self.element).perform()

