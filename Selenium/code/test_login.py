import json
import time
import pytest
from _pytest.fixtures import FixtureRequest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from ui.pages.vk_base_page import BasePage
from ui.locators import vk_locators


class BaseCase:
    authorize = True

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver, config, request: FixtureRequest):
        self.driver = driver
        self.config = config
        self.login_page = LoginPage(driver)


@pytest.fixture(scope='session')
def credentials():
    return {
        'user': '',
        'password': ''
    }


class LoginPage(BasePage):
    url = 'https://education.vk.company/'


class MainPage(BasePage):
    url = 'https://education.vk.company/feed/'

    def load_cookies(self):
        with open('cookies.json', 'r') as f:
            cookies = json.load(f)

        for cookie in cookies:
            self.driver.add_cookie(cookie)

    def load_feed(self):
        self.driver.get('https://education.vk.company/feed/')
        time.sleep(3)


class TestLK(BaseCase):

    def test_login(self, credentials):
        login_page = LoginPage(self.driver)
        self.driver.maximize_window()
        login_page.click(
            vk_locators.LoginPageLocators.AUTHBUTTON_LOCATOR,
        )
        time.sleep(15)
        login_page.click(
            vk_locators.LoginPageLocators.AUTH_LOCATOR,
        )
        time.sleep(3)
        loginInput = login_page.find(vk_locators.LoginPageLocators.LOGIN_LOCATOR)
        loginInput.send_keys(credentials.get('user', ''))
        passInput = login_page.find(vk_locators.LoginPageLocators.PASSWORD_LOCATOR)
        passInput.send_keys(credentials.get('password', ''))
        time.sleep(3)
        login_page.click(
            vk_locators.LoginPageLocators.LOGIN_BUTTON_LOCATOR,
        )
        time.sleep(5)

        cookies = self.driver.get_cookies()
        with open('cookies.json', 'w') as f:
            json.dump(cookies, f)

    def test_friend(self):
        main_page = MainPage(self.driver)
        main_page.load_cookies()
        main_page.load_feed()
        main_page.click(
            vk_locators.MainPageLocators.OPENSEARCH_LOCATOR,
        )
        time.sleep(3)
        search_element = vk_locators.MainPageLocators.SEARCH_LOCATOR
        search_field = main_page.find(search_element)
        search_field.send_keys("Артём Черников")
        time.sleep(3)
        main_page.find(search_element).send_keys(Keys.RETURN)
        time.sleep(3)
        main_page.click(
            vk_locators.MainPageLocators.FRIEND_LOCATOR,
        )
        time.sleep(5)

    def test_seminar(self):
        main_page = MainPage(self.driver)
        main_page.load_cookies()
        main_page.load_feed()
        main_page.click(
            vk_locators.MainPageLocators.PROGRAM_LOCATOR,
        )
        time.sleep(3)
        main_page.click(
            vk_locators.MainPageLocators.PROGRAM_TEST_LOCATOR,
        )
        time.sleep(3)
        main_page.click(
            vk_locators.MainPageLocators.LESSONS_LOCATOR,
        )
        time.sleep(3)
        main_page.click(
            vk_locators.MainPageLocators.LESSON_LOCATOR,
        )
        time.sleep(7)
