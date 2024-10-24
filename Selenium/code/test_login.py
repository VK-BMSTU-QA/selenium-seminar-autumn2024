import json
import time
import pytest
from _pytest.fixtures import FixtureRequest
from selenium.webdriver.common.keys import Keys

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
            basic_locators_vk.LoginPageLocators.LOGIN_INPUT_LOCATOR,
            credentials.get('user', ''),
        )
        self.input(
            basic_locators_vk.LoginPageLocators.PASSWORD_INPUT_LOCATOR,
            credentials.get('password', ''),
        )
        time.sleep(3)
        self.click(
            basic_locators_vk.LoginPageLocators.GO_BUTTON_LOGIN_LOCATOR, timeout=10
        )
        time.sleep(5)


class MainPage(BasePage):
    url = 'https://education.vk.company/feed/'

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
            # Переходим на страницу /feed/, требующую авторизации
        self.driver.get('https://education.vk.company/feed/')
        time.sleep(3)


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
            basic_locators_vk.MainPageLocators.GO_BUTTON_OPENSEARCH_LOCATOR, timeout=10
        )
        time.sleep(1)
        search_element = basic_locators_vk.MainPageLocators.SEARCH_INPUT_LOCATOR
        main_page.input(search_element, "Александр Никитин")
        time.sleep(1)
        main_page.find(search_element).send_keys(Keys.RETURN)
        time.sleep(1)
        main_page.click(
            basic_locators_vk.MainPageLocators.FRIEND_LOCATOR, timeout=10
        )
        time.sleep(5)

    def test_lesson(self):
        main_page = MainPage(self.driver)
        main_page.open_main()
        main_page.click(
            basic_locators_vk.MainPageLocators.GO_BUTTON_PROGRAM_LOCATOR, timeout=10
        )
        time.sleep(1)
        main_page.click(
            basic_locators_vk.MainPageLocators.GO_BUTTON_PROGRAM_TEST_LOCATOR, timeout=10
        )
        time.sleep(1)
        main_page.click(
            basic_locators_vk.MainPageLocators.GO_BUTTON_LESSONS_LOCATOR, timeout=10
        )
        time.sleep(1)
        main_page.click(
            basic_locators_vk.MainPageLocators.GO_BUTTON_LESSON_LOCATOR, timeout=10
        )
        time.sleep(5)
