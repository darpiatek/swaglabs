import allure
from pytest_bdd import when

from pages.cart_page.cart_page import CartPage

@when("The user proceeds to the checkout step")
@allure.step("The user proceeds to the checkout step")
def navigate_to_checkout(driver):
    cart_page = CartPage(driver)
    checkout_page = cart_page.click_checkout_button()
    checkout_page.validate_checkout_page_is_loaded()

@when("The user validates product names in cart")
@allure.step("The user validates product names in cart")
def navigate_to_checkout(driver, shopping_context):
    cart_page = CartPage(driver)
    cart_page.validate_products_in_cart(shopping_context['cart_items'])