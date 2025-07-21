from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select

from .element import Element

class DropDown(Element):

    @property
    def value(self):
        select = Select(self.element)
        return select.first_selected_option.text

    @value.setter
    def value(self, value):
        select = Select(self.element)
        select.select_by_visible_text(value)
