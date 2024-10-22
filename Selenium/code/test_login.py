import pytest
import json
import time
from _pytest.fixtures import FixtureRequest
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

from ui.pages.base_page import BasePage


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
    with open(r'C:\Учеба\ТП\3 сем\QA\selenium-seminar-autumn2024\Selenium\code\files\credentials.json', 'r') as f:
        return json.load(f)


@pytest.fixture(scope='session')
def cookies(credentials, config):
        pass


class LoginPage(BasePage):
    url = 'https://education.vk.company/'

    def login(self, user, password):
        login_button = self.find(self.locators.LOGIN_BUTTON)
        login_button.click()
        use_email_and_password_button = self.find(self.locators.USE_EMAIL_AND_PASSWORD_BUTTON)
        use_email_and_password_button.click()
        email_input = self.find(self.locators.EMAIL_INPUT)
        email_input.send_keys(user)
        password_input = self.find(self.locators.PASSWORD_INPUT)
        password_input.send_keys(password)
        submit_button = self.find(self.locators.SUBMIT_BUTTON)
        submit_button.click()
        return MainPage(self.driver)


class MainPage(BasePage):
    url = 'https://education.vk.company/feed/'


class TestLogin(BaseCase):
    authorize = True

    def test_login(self, credentials):
        self.login_page.login(credentials["login"], credentials["password"])
        pass


class TestLK(BaseCase):
    # 1. найти человека в лк и получить информацию "о себе"
    def test_lk1(self, credentials):
        self.login_page.login(credentials["login"], credentials["password"])
        search_button = self.login_page.find(self.login_page.locators.SEARCH_BUTTON)
        search_button.click()
        search_field = self.login_page.find(self.login_page.locators.SEARCH_FIELD)
        search_field.send_keys("Александр Горбатов")
        search_field.send_keys(Keys.ENTER)
        time.sleep(5)
        pass

    @pytest.mark.skip('skip')
    def test_lk2(self):
        pass

    @pytest.mark.skip('skip')
    def test_lk3(self):
        pass


# 1. найти человека в лк и получить информацию о себе
#
# 2. узнать аудиторию сегодняшнего занятия
#
# 3. получить инфу о месте проведения