import json
import os


import pytest
from _pytest.fixtures import FixtureRequest
from selenium.webdriver.common.keys import Keys

from ui.pages.base_page import BasePage
from ui.locators import basic_locators

from dotenv import load_dotenv

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from config import URLS


load_dotenv(dotenv_path='credential.env')


class BaseCase:
    authorize = True

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver, config, request: FixtureRequest):
        self.driver = driver
        self.config = config
        self.login_page = LoginPage(driver)
        self.main_page = MainPage(driver)



@pytest.fixture(scope='session')
def credentials():
    return {
        'user': os.getenv('USER_CREDENTIAL', ''),
        'password': os.getenv('PASSWORD_CREDENTIAL', '')
    }


class LoginPage(BasePage):
    url = URLS['login_page']

    def login(self, credentials):
        self.driver.maximize_window()
        self._perform_authentication(credentials)

    def _perform_authentication(self, credentials):
        self.click(
            basic_locators.LoginPageLocators.GO_BUTTON_AUTHBUTTON_LOCATOR
        )
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(basic_locators.LoginPageLocators.GO_BUTTON_TYPEAUTH_LOCATOR)
        ).click()
        self._input_credentials(credentials)
        self.click(
            basic_locators.LoginPageLocators.GO_BUTTON_LOGIN_LOCATOR
        )
        WebDriverWait(self.driver, 10).until(
            EC.url_contains('/feed/')
        )

    def _click_and_wait(self, locator, delay=3):
        element = WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable(locator)
        )
        element.click()
        WebDriverWait(self.driver, delay).until(
            EC.staleness_of(element)
        )

    def _input_credentials(self, credentials):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(basic_locators.LoginPageLocators.LOGIN_INPUT_LOCATOR)
        ).send_keys(credentials.get('user', ''))

        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(basic_locators.LoginPageLocators.PASSWORD_INPUT_LOCATOR)
        ).send_keys(credentials.get('password', ''))


class MainPage(BasePage):
    url = URLS['main_page']

    def is_opened(self):
        return self.driver.current_url == self.url

    def open_main(self):
        # Загружаем cookies из файла
        with open('cookies.json', 'r') as f:
            cookies = json.load(f)

        # Добавляем cookies в браузер
        for cookie in cookies:
            self.driver.add_cookie(cookie)
        self.driver.get(self.url)
        WebDriverWait(self.driver, 10).until(EC.url_contains('/feed/'))

    def _click_and_wait(self, locator, delay=3):
        element = WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable(locator)
        )
        element.click()
        WebDriverWait(self.driver, delay).until(
            EC.staleness_of(element)
        )

    def _save_cookies(self):
        cookies = self.driver.get_cookies()
        with open('cookies.json', 'w') as f:
            json.dump(cookies, f)


class TestLK(BaseCase):
    def test_login(self, credentials):
        login_page = LoginPage(self.driver)
        login_page.login(credentials)

        cookies = self.driver.get_cookies()
        with open('cookies.json', 'w') as f:
            json.dump(cookies, f)
        print("Авторизация прошла успешно")

    def _save_cookies(self):
        cookies = self.driver.get_cookies()
        with open('cookies.json', 'w') as f:
            json.dump(cookies, f)

    def test_friend(self, credentials):
        main_page = MainPage(self.driver)
        main_page.open_main()

        main_page.click(
            basic_locators.MainPageLocators.GO_BUTTON_OPENSEARCH_LOCATOR
        )
        search_element = basic_locators.MainPageLocators.SEARCH_INPUT_LOCATOR
        main_page.input(search_element, "Шиятов Наиль")
        main_page.find(search_element).send_keys(Keys.RETURN)
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(basic_locators.MainPageLocators.FRIEND_LOCATOR)
        ).click()




    def _search_friend(self, page, friend_name):
        page._click_and_wait(basic_locators.MainPageLocators.GO_BUTTON_OPENSEARCH_LOCATOR, delay=1)
        search_input = basic_locators.MainPageLocators.SEARCH_INPUT_LOCATOR
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(search_input)
        ).send_keys(friend_name)
        WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located(basic_locators.MainPageLocators.FRIEND_LOCATOR)
        )
        page._click_and_wait(basic_locators.MainPageLocators.FRIEND_LOCATOR, delay=5)

    def test_lesson(self, credentials):
        main_page = MainPage(self.driver)
        main_page.open_main()
        self._navigate_to_lesson(main_page)

    def _navigate_to_lesson(self, page):
        page._click_and_wait(basic_locators.MainPageLocators.GO_BUTTON_PROGRAM_LOCATOR, delay=1)
        page._click_and_wait(basic_locators.MainPageLocators.GO_BUTTON_PROGRAM_TEST_LOCATOR, delay=1)
        page._click_and_wait(basic_locators.MainPageLocators.GO_BUTTON_LESSONS_LOCATOR, delay=1)
        page._click_and_wait(basic_locators.MainPageLocators.GO_BUTTON_LESSON_LOCATOR, delay=5)