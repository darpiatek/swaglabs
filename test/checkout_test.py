from pytest_bdd import scenario

from steps import *

@allure.parent_suite("BDD Tests for Swag Labs")
@allure.title("Standard user completes a purchase successfully")
@allure.description("Standard user completes a purchase successfully")
@scenario('../features/checkout.feature', 'Standard user completes a purchase successfully')
def test_checkout():
    pass


