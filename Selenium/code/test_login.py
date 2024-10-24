import time
import pytest
from _pytest.fixtures import FixtureRequest

from ui.pages.base_page_vk import BasePage
from ui.locators import basic_locators_vk


class BaseCase:
    authorize = True

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver, config, request: FixtureRequest):
        self.driver = driver
        self.config = config
        self.login_page = LoginPage(driver)
        if self.authorize:
            print('Do something for login')


@pytest.fixture(scope='session')
def credentials():
    return {
        'user': '',
        'password': ''
    }

@pytest.fixture(scope='session')
def cookies(credentials, config, driver):
    login_page = LoginPage(driver)
    login_page.login(credentials)

    cookies = driver.get_cookies()
    yield cookies


class LoginPage(BasePage):
    url = 'https://education.vk.company/'

    def login(self, credentials):
        self.driver.maximize_window()
        self.click(
            basic_locators_vk.LoginPageLocators.GO_BUTTON_AUTHBUTTON_LOCATOR, timeout=10
        )
        time.sleep(3)
        self.click(
            basic_locators_vk.LoginPageLocators.GO_BUTTON_TYPEAUTH_LOCATOR, timeout=10
        )
        time.sleep(3)
        self.input(
            basic_locators_vk.LoginPageLocators.LOGIN_INPUT,
            credentials.get('user', ''),
        )
        self.input(
            basic_locators_vk.LoginPageLocators.PASSWORD_INPUT,
            credentials.get('password', ''),
        )
        time.sleep(3)
        self.click(
            basic_locators_vk.LoginPageLocators.LOGIN_BUTTON, timeout=10
        )
        time.sleep(3)
        return MainPage(self.driver)


class MainPage(BasePage):
    url = 'https://education.vk.company/feed/'

    def is_opened(self):
        # Проверим, что мы находимся на главной странице
        return self.driver.current_url == self.url


class TestLogin(BaseCase):
    authorize = True

    def test_login(self, credentials):
        pass


class TestLK(BaseCase):

    def test_lk1(self, credentials):
        login_page = LoginPage(self.driver)
        login_page.login(credentials)

    def test_lk2(self, cookies):
        for cookie in cookies:
            self.driver.add_cookie(cookie)
        self.driver.get('https://education.vk.company/feed/')
        time.sleep(5)

    @pytest.mark.skip('skip')
    def test_lk3(self):
        pass
