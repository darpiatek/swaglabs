from selenium.webdriver import ActionChains

from .element import Element


class Button(Element):

    def click(self):
        if super().is_displayed():
            super().element.click()

    def action_click(self, how: str, what: str):
        element = self._obj.driver.find_element(how, what)
        ActionChains(self._obj.driver).click(element).perform()