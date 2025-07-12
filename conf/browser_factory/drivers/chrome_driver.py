from selenium import webdriver

from ..drivers import register_browser


@register_browser
def chrome(**kwargs):
    settings = kwargs.get('settings')
    if settings is None:
        raise ValueError('No settings provided for ChromeBuilder')
    options = webdriver.ChromeOptions()
    options.add_argument('--start-maximized')
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--ignore-certificate-errors-spki-list')
    options.add_argument('--ignore-ssl-errors')
    options.add_argument('--disable-browser-side-navigation')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-gpu')
    options.add_argument('--disable-extensions')
    options.add_argument('--dns-prefetch-disable')
    options.add_argument('--disable-search-engine-choice-screen')
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    prefs = {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
        "profile.password_manager_leak_detection": False
    }
    options.add_experimental_option("prefs", prefs)
    if settings.PROXY_SERVER:
        options.add_argument(f'--proxy_server={settings.PROXY_SERVER}')
    if kwargs.get('headless'):
        options.add_argument("--headless=new")
        options.add_argument('--window-size=1360,768')
    return webdriver.Chrome(options=options)

