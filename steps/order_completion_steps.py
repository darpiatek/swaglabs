import allure
from pytest_bdd import parsers, then

from conf.allure import attach_screenshot_to_step
from pages.checkout.order_completion_page import OrderCompletionPage


@then(parsers.parse("A confirmation message {message} is displayed"))
@allure.step("A confirmation message {message} is displayed")
def validate_completion_message(driver, message):
    order_completion_page = OrderCompletionPage(driver)
    order_completion_page.validate_complete_message_is_displayed(message)
    attach_screenshot_to_step(driver)
