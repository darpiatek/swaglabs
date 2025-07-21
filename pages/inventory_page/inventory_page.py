from __future__ import annotations

from conf.settings import Timeouts
from page_elements.button import Button
from page_elements.dropdown import DropDown
from page_elements.text import TextElement
from pages.AbsBasePage import AbsBasePage
from pages.cart_page.cart_page import CartPage
from pages.inventory_page.inventory_page_locators import InventoryPageLocators


class InventoryPage(AbsBasePage):
    number_of_cart_items_text = TextElement(*InventoryPageLocators.NUMBER_OF_CART_ITEMS_TEXT)
    cart_button = Button(*InventoryPageLocators.CART_BUTTON)
    sort_menu = DropDown(*InventoryPageLocators.DROPDOWN_SORT_MENU)
    cart_total = 0
    removed_card_total = 0

    def is_inventory_page_loaded(self):
        return self.wait_for_presence_of_element_located(*InventoryPageLocators.INVENTORY_PAGE, Timeouts.SHORT)

    def get_cart_total(self):
        return self.cart_total

    def get_removed_card_total(self):
        return self.removed_card_total

    def get_all_inventory_items(self):
        return self.driver.find_elements(*InventoryPageLocators.INVENTORY_ITEMS)

    def get_inventory_item_price_by_index(self, index):
        item_price = self.driver.find_element(*InventoryPageLocators.INVENTORY_ITEM_PRICE(index)).text
        return float(item_price.replace('$', ''))

    def validate_inventory_page_is_loaded(self):
        assert self.is_inventory_page_loaded();
        return self

    def click_cart_button(self) -> CartPage:
        self.logger.substep('Click cart button')
        self.cart_button.click()
        return CartPage(self.driver)

    def add_remove_inventory_item_to_basket(self, datatable, add=True, remove=False):
        items = self.get_all_inventory_items()
        for i in datatable:
            for j, item in enumerate(items):
                item_name = item.find_element(*InventoryPageLocators.INVENTORY_ITEM_NAME).text
                if item_name == i[0]:
                    if add:
                        self.driver.find_element(*InventoryPageLocators.INVENTORY_ITEM_ADD_TO_CART_BUTTON(j+1)).click()
                        self.cart_total += self.get_inventory_item_price_by_index(j + 1)
                    if remove:
                        self.driver.find_element(
                            *InventoryPageLocators.INVENTORY_ITEM_REMOVE_FROM_CART_BUTTON(j + 1)).click()
                        self.removed_card_total += self.get_inventory_item_price_by_index(j + 1)
                    break
        self.validate_number_of_cart_items(len(datatable))
        return self

    def add_inventory_item_to_basket_by_index(self, index):
        self.driver.find_element(*InventoryPageLocators.INVENTORY_ITEM_ADD_TO_CART_BUTTON(index)).click()
        self.cart_total += self.get_inventory_item_price_by_index(index)
        return self.get_all_inventory_items()[index-1].find_element(*InventoryPageLocators.INVENTORY_ITEM_NAME).text

    def validate_number_of_cart_items(self, expected_number):
        assert expected_number == int(self.number_of_cart_items_text.value)

    def select_sort_method(self, sort_method):
        self.sort_menu.value = sort_method