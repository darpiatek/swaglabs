from selenium import webdriver
from selenium.webdriver.firefox.options import Options

from . import register_browser

@register_browser
def firefox(**kwargs):
    firefox_options = Options()
    if kwargs.get('headless'):
        firefox_options.add_argument("--headless")
        firefox_options.add_argument("--width=1920")
        firefox_options.add_argument("--height=1080")
    return webdriver.Firefox(options=firefox_options)
