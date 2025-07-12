from selenium.webdriver.common.by import By

class InventoryPageLocators:
    INVENTORY_PAGE = (By.ID, 'inventory_container')
    INVENTORY_ITEMS = (By.CLASS_NAME, 'inventory_item')
    INVENTORY_ITEM_NAME = (By.CLASS_NAME, 'inventory_item_name')
    INVENTORY_ITEM_ADD_TO_CART_BUTTON = lambda index: (By.XPATH, f'(//div[@class="pricebar"]//button)[{index}]')
    INVENTORY_ITEM_PRICE = lambda index: (By.XPATH, f'(//div[@class ="inventory_item_price"])[{index}]')
    NUMBER_OF_CART_ITEMS_TEXT = (By.XPATH, '//span[contains(@class, "shopping_cart_badge")]')
    CART_BUTTON = (By.ID, 'shopping_cart_container')