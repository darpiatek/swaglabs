from selenium.webdriver.common.by import By

class OrderCompletionPageLocators:
    ORDER_COMPLETION_PAGE = (By.ID, 'checkout_complete_container')
    COMPLETION_MESSAGE = (By.CLASS_NAME, 'complete-header')