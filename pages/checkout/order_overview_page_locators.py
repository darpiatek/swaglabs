from selenium.webdriver.common.by import By

class OrderOverviewPageLocators:
    ORDER_OVERVIEW_PAGE = (By.ID, 'checkout_summary_container')
    FINISH_BUTTON = (By.XPATH, '//a[contains(@class, "cart_button")]')
    TOTAL_TEXT = (By.CLASS_NAME, 'summary_subtotal_label')