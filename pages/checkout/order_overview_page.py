from __future__ import annotations

from conf.settings import Timeouts
from page_elements.button import Button
from page_elements.text import TextElement
from pages.AbsBasePage import AbsBasePage
from pages.checkout.order_completion_page import OrderCompletionPage
from pages.checkout.order_overview_page_locators import OrderOverviewPageLocators


class OrderOverviewPage(AbsBasePage):
    finish_button = Button(*OrderOverviewPageLocators.FINISH_BUTTON)
    total_text = TextElement(*OrderOverviewPageLocators.TOTAL_TEXT)

    def is_order_overview_page_loaded(self):
        return self.wait_for_presence_of_element_located(*OrderOverviewPageLocators.ORDER_OVERVIEW_PAGE, Timeouts.SHORT)

    def validate_order_overview_is_loaded(self):
        assert self.is_order_overview_page_loaded();
        return self

    def validate_order_total(self, value):
        assert self.get_item_total() == value
        return self

    def get_item_total(self):
        return float(self.total_text.value.replace('Item total: $', ''))

    def click_finish_button(self) -> OrderCompletionPage:
        self.logger.info('Click Finish button')
        self.finish_button.click()
        return OrderCompletionPage(self.driver)
