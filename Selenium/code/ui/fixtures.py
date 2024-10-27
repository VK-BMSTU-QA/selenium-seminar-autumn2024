import os

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from ui.pages.base_page import BasePage
from ui.pages.main_page import MainPage
from ui.pages.login_page_vked import LoginPage
import json

@pytest.fixture(scope='function')
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
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    elif browser == 'firefox':
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    else:
        raise RuntimeError(f'Unsupported browser: "{browser}"')
    driver.get(url)
    driver.maximize_window()
    yield driver
    driver.quit()


def get_driver(browser_name):
    if browser_name == 'chrome':
        browser = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    elif browser_name == 'firefox':
        browser = webdriver.Firefox(executable_path=GeckoDriverManager().install())
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
def login_vked_page(driver):
    return LoginPage(driver=driver)



@pytest.fixture(scope='session')
def credentials_vked():
    email = os.getenv('email')
    password = os.getenv('password')
    profile_fi = os.getenv('profile_fi')

    return {
        'email':      email,
        'password':   password,
        'profile_fi': profile_fi
    }

@pytest.fixture(scope='session')
def user_to_find_vked():
    with open('files/userdata.json', 'r') as f:
        userdata = json.load(f)

    name_to_find = userdata['name_to_find']
    surname_to_find = userdata['surname_to_find']
    return {
        'name_to_find':      name_to_find,
        'surname_to_find':   surname_to_find,
    }


@pytest.fixture(scope='session')
def cookies(credentials, config):
        pass
