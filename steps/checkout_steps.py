import allure
from pytest_bdd import when
from pages.checkout.checkout_page import CheckoutPage

@when("The user enters the checkout information:")
@allure.step("The user enters the checkout information:: {datatable}")
def enter_checkout_information(driver, datatable):
    checkout_page = CheckoutPage(driver)
    checkout_page.set_first_name(datatable[1][0])
    checkout_page.set_last_name(datatable[1][1])
    checkout_page.set_postal_code(datatable[1][2])

@when("The user continues to the order overview page")
@allure.step("The user continues to the order overview page")
def navigate_to_order_overview_page(driver):
    checkout_page = CheckoutPage(driver)
    order_overview_page = checkout_page.click_continue_button()
    order_overview_page.validate_order_overview_is_loaded()