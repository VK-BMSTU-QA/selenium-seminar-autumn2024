import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FireFoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from ui.pages.vk_education_landing import BasePage
from ui.pages.vk_education_main import MainPage

from dotenv import dotenv_values


@pytest.fixture()
def driver(config):
    browser = config['browser']
    url = config['url']
    selenoid = config['selenoid']
    vnc = config['vnc']
    options = Options()
    if selenoid:
        capabilities = {
            'browserName': 'chrome',
            'version': '130.0.6723.70',
        }
        if vnc:
            capabilities['enableVNC'] = True
        driver = webdriver.Remote(
            'http://127.0.0.1:4444/wd/hub',
            options=options,
            desired_capabilities=capabilities
        )
    elif browser == 'chrome':
        service = ChromeService(executable_path=ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)
    elif browser == 'firefox':
        service = FireFoxService(executable_path=GeckoDriverManager().install())
        driver = webdriver.Firefox(service=service)
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


@pytest.fixture(scope='session')
def credentials():
    credentials = dotenv_values(".credentials_env")
    credentials = dict(credentials)
    return credentials


@pytest.fixture(scope='session')
def student_test_data():
    return {"username": "Фёдор Долматов", "profile_link": "https://education.vk.company/profile/user_202440/"}