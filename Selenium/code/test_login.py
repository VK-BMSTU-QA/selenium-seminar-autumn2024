import json
import os
import time

import pytest
from _pytest.fixtures import FixtureRequest
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from ui.pages.base_page_vk import BasePage
from ui.locators import basic_locators_vk

# Конфигурация URL
URLS = {
    'login': 'https://education.vk.company/',
    'main': 'https://education.vk.company/feed/'
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
        'user': os.getenv('LOGIN_USER', ''),
        'password': os.getenv('LOGIN_PASSWORD', '')
    }


class LoginPage(BasePage):
    url = URLS['login']

    def login(self, credentials):
        self.driver.maximize_window()
        self.click(
            basic_locators_vk.LoginPageLocators.GO_BUTTON_AUTHBUTTON_LOCATOR
        )
        self.wait().until(
            EC.element_to_be_clickable(basic_locators_vk.LoginPageLocators.GO_BUTTON_TYPEAUTH_LOCATOR)
        ).click()
        self.input(
            basic_locators_vk.LoginPageLocators.LOGIN_INPUT_LOCATOR,
            credentials.get('user', '')
        )
        self.input(
            basic_locators_vk.LoginPageLocators.PASSWORD_INPUT_LOCATOR,
            credentials.get('password', '')
        )
        self.click(
            basic_locators_vk.LoginPageLocators.GO_BUTTON_LOGIN_LOCATOR
        )
        self.wait().until(
            EC.url_contains('/feed/')
        )


class MainPage(BasePage):
    url = URLS['main']

    def is_opened(self):
        # Проверим, что мы находимся на главной странице
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


class TestLK(BaseCase):

    def test_login(self, credentials):
        login_page = LoginPage(self.driver)
        login_page.login(credentials)

        # Сохраняем cookies
        cookies = self.driver.get_cookies()
        with open('cookies.json', 'w') as f:
            json.dump(cookies, f)

    def test_friend(self):
        main_page = MainPage(self.driver)
        main_page.open_main()
        main_page.click(
            basic_locators_vk.MainPageLocators.GO_BUTTON_OPENSEARCH_LOCATOR
        )
        search_element = basic_locators_vk.MainPageLocators.SEARCH_INPUT_LOCATOR
        main_page.input(search_element, "Александр Никитин")
        main_page.find(search_element).send_keys(Keys.RETURN)
        main_page.wait().until(
            EC.presence_of_element_located(basic_locators_vk.MainPageLocators.FRIEND_LOCATOR)
        ).click()
        time.sleep(5)

    def test_lesson(self):
        main_page = MainPage(self.driver)
        main_page.open_main()
        main_page.click(
            basic_locators_vk.MainPageLocators.GO_BUTTON_PROGRAM_LOCATOR
        )
        main_page.wait().until(
            EC.element_to_be_clickable(basic_locators_vk.MainPageLocators.GO_BUTTON_PROGRAM_TEST_LOCATOR)
        ).click()
        main_page.click(
            basic_locators_vk.MainPageLocators.GO_BUTTON_LESSONS_LOCATOR
        )
        main_page.wait().until(
            EC.element_to_be_clickable(basic_locators_vk.MainPageLocators.GO_BUTTON_LESSON_LOCATOR)
        ).click()
        time.sleep(5)
