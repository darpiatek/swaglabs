import allure


def attach_screenshot_to_step(driver):
    """Attach screenshot to an allure step"""
    allure.attach(driver.get_screenshot_as_png(), name='screenshot', attachment_type=allure.attachment_type.PNG)