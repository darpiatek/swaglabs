from __future__ import annotations

from conf.settings import Timeouts
from page_elements.button import Button
from page_elements.input import InputField
from pages.AbsBasePage import AbsBasePage
from pages.checkout.checkout_page_locators import CheckoutPageLocators
from pages.checkout.order_overview_page import OrderOverviewPage


class CheckoutPage(AbsBasePage):
    continue_button = Button(*CheckoutPageLocators.CONTINUE_BUTTON)
    first_name_input = InputField(*CheckoutPageLocators.FIRST_NAME_FIELD)
    last_name_input = InputField(*CheckoutPageLocators.LAST_NAME_FIELD)
    postal_code_input = InputField(*CheckoutPageLocators.POSTAL_CODE_FIELD)

    def is_checkout_page_loaded(self):
        return self.wait_for_presence_of_element_located(*CheckoutPageLocators.CHECKOUT_PAGE, Timeouts.SHORT)

    def validate_checkout_page_is_loaded(self):
        assert self.is_checkout_page_loaded();
        return self

    def click_continue_button(self) -> OrderOverviewPage:
        self.logger.info('Click Continue button')
        self.continue_button.click()
        return OrderOverviewPage(self.driver)

    def set_first_name(self, value: str) -> CheckoutPage:
        self.logger.info(f'Set first name as "{value}"')
        self.first_name_input.value = value
        return self

    def set_last_name(self, value: str) -> CheckoutPage:
        self.logger.info(f'Set last name as "{value}"')
        self.last_name_input.value = value
        return self

    def set_postal_code(self, value: str) -> CheckoutPage:
        self.logger.info(f'Set postal code as "{value}"')
        self.postal_code_input.value = value
        return self