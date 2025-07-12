from selenium.webdriver.common.by import By


class LoginPageLocators:
    LOGIN_BUTTON = (By.ID, 'login-button')
    USERNAME_FIELD = (By.ID, 'user-name')
    PASSWORD_FIELD = (By.ID, 'password')
    LOGIN_CONTAINER = (By.ID, 'login_button_container')