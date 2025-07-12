import allure
from pytest_bdd import when

from pages.inventory_page.inventory_page import InventoryPage

@when("The user adds the following products to the cart:")
@allure.step("The user adds the following products to the cart: {datatable}")
def add_products_to_cart(driver, shopping_context, datatable):
    inventory_page = InventoryPage(driver)
    inventory_page.add_inventory_item_to_basket(datatable[1][0], datatable[2][0])
    shopping_context['cart_total'] = inventory_page.get_cart_total()

@when("The user navigates to the shopping cart")
@allure.step("The user navigates to the shopping cart")
def navigate_to_cart(driver):
    inventory_page = InventoryPage(driver)
    cart_page = inventory_page.click_cart_button()
    cart_page.validate_cart_page_is_loaded()