import json
import os
import time
import pytest
from _pytest.fixtures import FixtureRequest
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from ui.pages.vk_base_page import BasePage
from ui.locators import vk_locators

URL_CONFIG = {
    'base': 'https://education.vk.company/',
    'feed': 'https://education.vk.company/feed/',
    'friend': 'https://education.vk.company/profile/user_191238/'
}


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
        'user': os.environ.get("VK_USERNAME"),
        'password': os.environ.get("VK_PASSWORD")
    }


class LoginPage(BasePage):
    url = URL_CONFIG['base']


class MainPage(BasePage):
    url = URL_CONFIG['feed']

    def load_cookies(self):
        with open('cookies.json', 'r') as f:
            cookies = json.load(f)

        for cookie in cookies:
            self.driver.add_cookie(cookie)

    def load_feed(self):
        self.driver.get('https://education.vk.company/feed/')


class TestLK(BaseCase):

    def test_login(self, credentials):
        login_page = LoginPage(self.driver)
        self.driver.maximize_window()
        login_page.click(
            vk_locators.LoginPageLocators.AUTHBUTTON_LOCATOR,
        )
        login_page.click(
            vk_locators.LoginPageLocators.AUTH_LOCATOR,
        )
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(vk_locators.LoginPageLocators.LOGIN_LOCATOR)
        )
        loginInput = login_page.find(vk_locators.LoginPageLocators.LOGIN_LOCATOR)
        loginInput.send_keys(credentials.get('user', ''))
        passInput = login_page.find(vk_locators.LoginPageLocators.PASSWORD_LOCATOR)
        passInput.send_keys(credentials.get('password', ''))
        login_page.click(
            vk_locators.LoginPageLocators.LOGIN_BUTTON_LOCATOR,
        )
        WebDriverWait(self.driver, 10).until(
            EC.url_contains(URL_CONFIG['feed'])
        )
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
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(vk_locators.MainPageLocators.SEARCH_LOCATOR)
        )
        search_element = vk_locators.MainPageLocators.SEARCH_LOCATOR
        search_field = main_page.find(search_element)
        search_field.send_keys("Артём Черников")
        main_page.find(search_element).send_keys(Keys.RETURN)
        main_page.click(
            vk_locators.MainPageLocators.FRIEND_LOCATOR,
        )
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(vk_locators.MainPageLocators.FRIEND_NAME_LOCATOR)
        )

    def test_seminar(self):
        main_page = MainPage(self.driver)
        main_page.load_cookies()
        main_page.load_feed()
        main_page.click(
            vk_locators.MainPageLocators.PROGRAM_LOCATOR,
        )
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(vk_locators.MainPageLocators.PROGRAM_TEST_LOCATOR)
        )
        main_page.click(
            vk_locators.MainPageLocators.PROGRAM_TEST_LOCATOR,
        )
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(vk_locators.MainPageLocators.LESSONS_LOCATOR)
        )
        main_page.click(
            vk_locators.MainPageLocators.LESSONS_LOCATOR,
        )
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(vk_locators.MainPageLocators.LESSON_LOCATOR)
        )
        main_page.click(
            vk_locators.MainPageLocators.LESSON_LOCATOR,
        )
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(vk_locators.MainPageLocators.LESSON_NAME_LOCATOR)
        )
