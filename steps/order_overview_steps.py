import allure
from pytest_bdd import when

from pages.checkout.order_overview_page import OrderOverviewPage


@when("The user finishes the checkout")
@allure.step("The user finishes the checkout")
def finish_checkout(driver):
    order_overview_page = OrderOverviewPage(driver)
    order_completion_page = order_overview_page.click_finish_button()
    order_completion_page.validate_order_completion_is_loaded()


@when("The user validates the order total")
@allure.step("The user validates the order total")
def validate_order_total(driver, shopping_context):
    order_overview_page = OrderOverviewPage(driver)
    order_overview_page.validate_order_total(shopping_context['cart_total'])

@when("The user validates the product names in order")
@allure.step("The user validates the product names in order")
def validate_order_total(driver, shopping_context):
    order_overview_page = OrderOverviewPage(driver)
    order_overview_page.validate_products_in_order(shopping_context['cart_items'])
