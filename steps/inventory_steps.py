import allure
from pytest_bdd import when, parsers

from pages.inventory_page.inventory_page import InventoryPage

@when("The user adds the following products to the cart:")
@allure.step("The user adds the following products to the cart: {datatable}")
def add_products_to_cart(driver, shopping_context, datatable):
    inventory_page = InventoryPage(driver)
    inventory_page.add_remove_inventory_item_to_basket(datatable[1:], add=True, remove=False)
    shopping_context['cart_total'] += inventory_page.get_cart_total()

@when(parsers.parse("The user adds the {idx} product to the cart"))
@allure.step("The user adds the {idx} product to the cart")
def add_products_to_cart(driver, shopping_context, idx):
    inventory_page = InventoryPage(driver)
    items = inventory_page.get_all_inventory_items()
    if idx=='last':
        idx = len(items)-1
    elif idx=='first':
        idx = 1
    cart_item = inventory_page.add_inventory_item_to_basket_by_index(idx)
    shopping_context["cart_items"].append(cart_item)
    shopping_context['cart_total'] += inventory_page.get_cart_total()

@when("The user removes the following products from the cart:")
@allure.step("The user removes the following products from the cart: {datatable}")
def remove_products_to_cart(driver, shopping_context, datatable):
    inventory_page = InventoryPage(driver)
    inventory_page.add_remove_inventory_item_to_basket(datatable[1:], add=False, remove=True)
    shopping_context['cart_total'] = round(shopping_context['cart_total'] - inventory_page.get_removed_card_total(), 2)

@when("The user navigates to the shopping cart")
@allure.step("The user navigates to the shopping cart")
def navigate_to_cart(driver):
    inventory_page = InventoryPage(driver)
    cart_page = inventory_page.click_cart_button()
    cart_page.validate_cart_page_is_loaded()

@when(parsers.parse("The user sorts the products by {sort_method}"))
@allure.step("The user sorts the products by {sort_method}")
def sort_products_by_method(driver, sort_method):
    InventoryPage(driver).select_sort_method(sort_method)