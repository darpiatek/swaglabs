from __future__ import annotations

from conf.settings import Timeouts
from page_elements.button import Button
from pages.AbsBasePage import AbsBasePage
from pages.cart_page.cart_page_locators import CartPageLocators
from pages.checkout.checkout_page import CheckoutPage


class CartPage(AbsBasePage):
    checkout_button = Button(*CartPageLocators.CHECKOUT_BUTTON)

    def is_cart_page_loaded(self):
        return self.wait_for_presence_of_element_located(*CartPageLocators.CART_PAGE, Timeouts.SHORT)

    def validate_cart_page_is_loaded(self):
        assert self.is_cart_page_loaded();
        return self

    def click_checkout_button(self) -> CheckoutPage:
        self.logger.substep('Click Checkout button')
        self.checkout_button.click()
        return CheckoutPage(self.driver)