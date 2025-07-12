from typing import Union

from selenium.common.exceptions import WebDriverException
from selenium.webdriver.remote.webdriver import WebDriver

from . import drivers


class BaseSettings:
    """Browser options"""
    DRIVER_DIR: str = ''
    LOG_DIR: str = ''
    PAGE_LOAD_TIMEOUT: int = 600
    SCRIPT_TIMEOUT: int = 180
    HEADLESS: bool = False
    PROXY_SERVER: str = ''


class BrowserFactory:
    """Browser Factory"""

    @staticmethod
    def get(browser_name: str, settings: BaseSettings = None, **kwargs) -> Union[WebDriver, None]:
        """Returns WebDriver instance"""
        if not hasattr(drivers, browser_name):
            raise ValueError(f'"{browser_name}" is not valid browser name')
        if settings is None:
            settings = BaseSettings()  # type: ignore
        if not isinstance(settings, BaseSettings):
            raise TypeError('settings must by an instance of BaseSettings class')
        driver_builder = getattr(drivers, browser_name)
        try:
            driver_instance = driver_builder(settings=settings, **kwargs)
        except (WebDriverException, ConnectionRefusedError) as e:
            print(f'Check if driver version is compatible with your browser version. '
                  f'If versions are different please update your browser: {e}')
            return None
        if driver_instance:
            driver_instance.set_page_load_timeout(settings.PAGE_LOAD_TIMEOUT)
            driver_instance.set_script_timeout(settings.SCRIPT_TIMEOUT)
            driver_instance.maximize_window()
        return driver_instance
