from selenium.webdriver.common.by import By

class CartPageLocators:
    CART_PAGE = (By.ID, 'cart_contents_container')
    CHECKOUT_BUTTON = (By.XPATH, '//a[contains(@class, "checkout_button")]')