from __future__ import annotations

from conf.settings import Timeouts
from page_elements.button import Button
from pages.AbsBasePage import AbsBasePage
from pages.login_page.login_page import LoginPage
from pages.menu_page_locators import MenuPageLocators


class MenuPage(AbsBasePage):
    menu_button = Button(*MenuPageLocators.MENU_BUTTON)
    logout_button = Button(*MenuPageLocators.LOGOUT_BUTTON)

    def click_menu_button(self):
        self.logger.substep('Click Menu button')
        self.menu_button.click()
        return self

    def click_logout_button(self) -> LoginPage:
        self.logger.substep('Click Logout button')
        self.wait_for_element_to_be_enabled(*MenuPageLocators.LOGOUT_BUTTON, Timeouts.VERY_SHORT)
        self.logout_button.click()
        return LoginPage(self.driver)
