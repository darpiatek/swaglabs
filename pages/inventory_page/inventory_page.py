from __future__ import annotations

from conf.settings import Timeouts
from page_elements.button import Button
from page_elements.text import TextElement
from pages.AbsBasePage import AbsBasePage
from pages.cart_page.cart_page import CartPage
from pages.inventory_page.inventory_page_locators import InventoryPageLocators


class InventoryPage(AbsBasePage):
    number_of_cart_items_text = TextElement(*InventoryPageLocators.NUMBER_OF_CART_ITEMS_TEXT)
    cart_button = Button(*InventoryPageLocators.CART_BUTTON)
    cart_total = 0

    def is_inventory_page_loaded(self):
        return self.wait_for_presence_of_element_located(*InventoryPageLocators.INVENTORY_PAGE, Timeouts.SHORT)

    def get_cart_total(self):
        return self.cart_total

    def get_inventory_item_price_by_index(self, index):
        item_price = self.driver.find_element(*InventoryPageLocators.INVENTORY_ITEM_PRICE(index)).text
        return float(item_price.replace('$', ''))

    def validate_inventory_page_is_loaded(self):
        assert self.is_inventory_page_loaded();
        return self

    def click_cart_button(self) -> CartPage:
        self.logger.info('Click cart button')
        self.cart_button.click()
        return CartPage(self.driver)

    def add_inventory_item_to_basket(self, *args):
        items = self.driver.find_elements(*InventoryPageLocators.INVENTORY_ITEMS)
        counter = 0
        for i, value in enumerate(args, start=counter):
            for j, item in enumerate(items):
                item_name = item.find_element(*InventoryPageLocators.INVENTORY_ITEM_NAME).text
                if item_name == value:
                    self.driver.find_element(*InventoryPageLocators.INVENTORY_ITEM_ADD_TO_CART_BUTTON(j+1)).click()
                    counter += 1
                    self.cart_total += self.get_inventory_item_price_by_index(j+1)
                    break
            if counter == len(args):
                break
        self.validate_number_of_cart_items(len(args))
        return self

    def validate_number_of_cart_items(self, expected_number):
        assert expected_number == int(self.number_of_cart_items_text.value)
