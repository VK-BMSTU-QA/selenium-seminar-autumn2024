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
        self._perform_authentication(credentials)

    def _perform_authentication(self, credentials):
        self._click_and_wait(basic_locators_vk.AuthPageLocators.AUTH_BUTTON_LOC)
        self._click_and_wait(basic_locators_vk.DashboardPageLocators.AUTH_TYPE_BUTTON_LOC)
        self._input_credentials(credentials)
        self._click_and_wait(basic_locators_vk.AuthPageLocators.SUBMIT_BUTTON_LOC, delay=5)

    def _click_and_wait(self, locator, delay=3):
        self.click(locator, timeout=10)
        time.sleep(delay)

    def _input_credentials(self, credentials):
        self.input(basic_locators_vk.AuthPageLocators.EMAIL_FIELD_LOC, credentials.get('user', ''))
        self.input(basic_locators_vk.AuthPageLocators.PASSWORD_FIELD_LOC, credentials.get('password', ''))
        time.sleep(3)


class MainPage(BasePage):
    url = 'https://education.vk.company/feed/'

    def is_opened(self):
        return self.driver.current_url == self.url

    def open_main(self):
        self._load_cookies()
        self.driver.get(self.url)
        time.sleep(3)

    def _load_cookies(self):
        with open('cookies.json', 'r') as f:
            cookies = json.load(f)
        for cookie in cookies:
            self.driver.add_cookie(cookie)


class TestLK(BaseCase):

    def test_login(self, credentials):
        self.login_page.login(credentials)
        self._save_cookies()

    def _save_cookies(self):
        cookies = self.driver.get_cookies()
        with open('cookies.json', 'w') as f:
            json.dump(cookies, f)

    def test_friend(self):
        main_page = MainPage(self.driver)
        main_page.open_main()
        self._search_friend(main_page, "Шиятов Наиль")

    def _search_friend(self, page, friend_name):
        page._click_and_wait(basic_locators_vk.DashboardPageLocators.OPEN_SEARCH_BUTTON_LOC, delay=1)
        search_element = basic_locators_vk.DashboardPageLocators.SEARCH_FIELD_LOC
        page.input(search_element, friend_name)
        page.find(search_element).send_keys(Keys.RETURN)
        time.sleep(1)
        page._click_and_wait(basic_locators_vk.DashboardPageLocators.FRIEND_LINK_LOC, delay=5)

    def test_lesson(self):
        main_page = MainPage(self.driver)
        main_page.open_main()
        self._navigate_to_lesson(main_page)

    def _navigate_to_lesson(self, page):
        page._click_and_wait(basic_locators_vk.DashboardPageLocators.PROGRAM_LINK_LOC, delay=1)
        page._click_and_wait(basic_locators_vk.DashboardPageLocators.PROGRAM_TEST_LINK_LOC, delay=1)
        page._click_and_wait(basic_locators_vk.DashboardPageLocators.TOGGLE_LESSONS_BUTTON_LOC, delay=1)
        page._click_and_wait(basic_locators_vk.DashboardPageLocators.LESSON_LINK_LOC, delay=5)
