import allure
from pytest_bdd import given, when, parsers, then

from conf.path_conf import USERS_FILE
from conf.settings import ENV
from data.user_manager import UserManager
from pages.PageFactory import PageFactory
from pages.menu_page import MenuPage

users = UserManager(USERS_FILE, ENV)


@given("The user is on the Swag Labs login page")
@allure.step("The user is on the Swag Labs login page")
def open_swag_labs(driver):
    login_page = PageFactory(driver).get('login page').open()
    login_page.validate_login_page_is_loaded()


@when(parsers.parse("The {username} logs in with valid credentials"))
@allure.step("The {username} logs in with valid credentials")
def login_to_swag_labs(driver, username):
    login_page = PageFactory(driver).get('login page').open()
    if login_page.is_login_container_present():
        login_page.set_username(users.get_user_name(username))
        login_page.set_password(users.get_password(username))
        inventory_page = login_page.click_login_button()
        inventory_page.is_inventory_page_loaded()


@then(parsers.parse("The user logs out successfully"))
@allure.step("The user logs out successfully")
def logout_from_swag_labs(driver):
    menu_page = MenuPage(driver)
    menu_page.click_menu_button()
    login_page = menu_page.click_logout_button()
    login_page.validate_login_page_is_loaded()
