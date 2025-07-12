from selenium.webdriver import ActionChains

from .element import Element


class InputField(Element):

    @property
    def value(self):
        return self.element.get_attribute("value")

    @value.setter
    def value(self, value):
        self.element.clear()
        self.element.send_keys(value)

    def send_keys(self, how: str, what: str, value: str):
        element = self._obj.driver.find_element(how, what)
        ActionChains(self._obj.driver).move_to_element(element).click(element).send_keys(value).perform()
