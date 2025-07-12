from conf.path_conf import URLS_FILE
from conf.settings import ENV
from data.url_manager import UrlManager
from pages.login_page.login_page import LoginPage


class PageFactory:
    urls_dict = UrlManager(URLS_FILE, ENV).urls

    def __init__(self, driver):
        self._pages: dict = dict()
        self._driver = driver
        self._register_page('login page', LoginPage, PageFactory.urls_dict['login_page'])

    def get(self, page_name: str):
        page, url = self._pages.get(page_name.lower())
        if page is None:
            raise KeyError(page_name)
        return page(self._driver, url)

    def _register_page(self, page_name, obj, url=None):
        self._pages[page_name.lower()] = (obj, url)
