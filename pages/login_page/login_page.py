from __future__ import annotations

from conf.settings import Timeouts
from page_elements.button import Button
from page_elements.input import InputField
from pages.AbsBasePage import AbsBasePage
from pages.inventory_page.inventory_page import InventoryPage
from pages.login_page.login_page_locators import LoginPageLocators


class LoginPage(AbsBasePage):
    login_button = Button(*LoginPageLocators.LOGIN_BUTTON)
    user_name_input = InputField(*LoginPageLocators.USERNAME_FIELD)
    password_input = InputField(*LoginPageLocators.PASSWORD_FIELD)

    def click_login_button(self) -> InventoryPage:
        self.logger.info('Click Login button')
        self.login_button.click()
        return InventoryPage(self.driver)

    def is_login_container_present(self):
        return self.wait_for_presence_of_element_located(*LoginPageLocators.LOGIN_CONTAINER, Timeouts.VERY_SHORT)

    def validate_login_page_is_loaded(self):
        assert self.is_login_container_present()
        return self

    def set_username(self, value: str) -> LoginPage:
        self.logger.info(f'Set Username as "{value}"')
        self.user_name_input.value = value
        return self

    def set_password(self, value: str) -> LoginPage:
        self.logger.info(f'Set password as "{value}"')
        self.password_input.value = value
        return self
