from selenium.webdriver.common.by import By

class CheckoutPageLocators:
    CHECKOUT_PAGE = (By.ID, 'checkout_info_container')
    CONTINUE_BUTTON = (By.XPATH, '//input[contains(@class, "cart_button")]')
    FIRST_NAME_FIELD = (By.ID, 'first-name')
    LAST_NAME_FIELD = (By.ID, 'last-name')
    POSTAL_CODE_FIELD = (By.ID, 'postal-code')