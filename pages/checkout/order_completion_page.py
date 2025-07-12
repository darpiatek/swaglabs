from __future__ import annotations

from conf.settings import Timeouts
from page_elements.text import TextElement
from pages.AbsBasePage import AbsBasePage
from pages.checkout.order_completion_page_locators import OrderCompletionPageLocators


class OrderCompletionPage(AbsBasePage):
    completion_message = TextElement(*OrderCompletionPageLocators.COMPLETION_MESSAGE)

    def is_order_completion_page_loaded(self):
        return self.wait_for_presence_of_element_located(*OrderCompletionPageLocators.ORDER_COMPLETION_PAGE, Timeouts.SHORT)

    def validate_order_completion_is_loaded(self):
        assert self.is_order_completion_page_loaded();
        return self

    def validate_complete_message_is_displayed(self, message):
        assert self.completion_message.value == message;
        return self