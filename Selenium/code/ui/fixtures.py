import json
import os

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from ui.pages.base_page import BasePage
from ui.pages.login_page import LoginPage
from ui.pages.main_page import MainPage
from ui.pages.person_page import PersonPage
from ui.pages.schedule_page import SchedulePage
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


@pytest.fixture(scope='session')
def driver(config):
    browser = config['browser']
    url = config['url']
    selenoid = config['selenoid']
    vnc = config['vnc']
    options = Options()
    if selenoid:
        capabilities = {
            'browserName': 'chrome',
            'version': '118.0',
        }
        if vnc:
            capabilities['enableVNC'] = True
        driver = webdriver.Remote(
            'http://127.0.0.1:4444/wd/hub',
            options=options,
            desired_capabilities=capabilities
        )
    elif browser == 'chrome':
        s = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=s)
    elif browser == 'firefox':
        s = Service(GeckoDriverManager().install())
        driver = webdriver.Firefox(service=s)
    else:
        raise RuntimeError(f'Unsupported browser: "{browser}"')
    driver.get(url)
    driver.maximize_window()
    yield driver
    driver.quit()


def get_driver(browser_name):
    if browser_name == 'chrome':
        s = Service(ChromeDriverManager().install())
        browser = webdriver.Chrome(service=s)
    elif browser_name == 'firefox':
        s = Service(GeckoDriverManager().install())
        browser = webdriver.Firefox(service=s)
    else:
        raise RuntimeError(f'Unsupported browser: "{browser_name}"')
    browser.maximize_window()
    return browser


@pytest.fixture(scope='session', params=['chrome', 'firefox'])
def all_drivers(config, request):
    url = config['url']
    browser = get_driver(request.param)
    browser.get(url)
    yield browser
    browser.quit()


@pytest.fixture
def base_page(driver):
    return BasePage(driver=driver)


@pytest.fixture
def main_page(driver):
    return MainPage(driver=driver)


@pytest.fixture
def schedule_page(driver):
    return SchedulePage(driver=driver)


@pytest.fixture
def person_page(driver):
    return PersonPage(driver=driver)


@pytest.fixture
def setup_cookies(driver, cookies):
    for cookie in cookies:
        driver.add_cookie(cookie)


@pytest.fixture(scope='session')
def credentials():
    file_path = os.path.join(os.path.dirname(__file__), '..', 'files', 'credentials.json')
    with open(file_path, 'r') as f:
        return json.load(f)


@pytest.fixture(scope='session')
def cookies(credentials, driver):
    login_page = LoginPage(driver)
    login_page.login(credentials['login'], credentials['password'])

    return driver.get_cookies()
