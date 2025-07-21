import pytest
from pytest_bdd import scenario

from steps import *

@allure.parent_suite("BDD Tests for Swag Labs")
@allure.title("Standard user completes a purchase successfully")
@allure.description("Standard user completes a purchase successfully")
@scenario('../features/checkout.feature', 'Standard user completes a purchase successfully')
@pytest.mark.smoke
def test_checkout():
    pass


@allure.parent_suite("BDD Tests for Swag Labs")
@allure.title("Standard user purchases the cheapest and most expensive product")
@allure.description("Standard user purchases the cheapest and most expensive product")
@scenario('../features/checkout.feature', 'Standard user purchases the cheapest and most expensive product')
@pytest.mark.regression
def test_checkout_cheapest_and_most_expensive_product():
    pass