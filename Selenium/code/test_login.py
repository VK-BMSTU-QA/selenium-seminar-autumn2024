import time
import pytest
from _pytest.fixtures import FixtureRequest

from ui.pages.login_page import LoginPage
from ui.pages.schedule_page import SchedulePage
from ui.pages.people_page import PeoplePage
import logindata
from base import BaseCase
from ui.pages.base_page import BasePage

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from ui.locators import basic_locators
import conftest

search_data = {
    'date': '22 октября 2024',
    'room': ' ауд.395 - зал 3 (МГТУ)',
    'name': 'Александр',
    'last_name': 'Батовкин'
}

class BaseCase:
    authorize = True

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver, config, request: FixtureRequest):
        self.driver = driver
        self.config = config
        self.cresentials = getCredentials

        self.login_page = LoginPage(driver)
        self.schedule_page = SchedulePage(driver)
        self.people_page = PeoplePage(driver)
        self.locators = basic_locators.BasePageLocators()
        if self.authorize:
            print('Do something for login')

    def set_cookie(self, cookies):
        self.driver.get(MainPage.url)
        for cookie in cookies:
            self.driver.add_cookie(cookie)
        self.driver.refresh()

    def login_and_verify(self, email, password, expected_url):
        self.login_page.login(email, password)
        self.login_page.wait_for_url(expected_url)
        assert self.login_page.driver.current_url == expected_url, f"URL не соответствует ожидаемому: {expected_url}"

@pytest.fixture(scope='session')
def getCredentials():
        return {
            'email': logindata.email,
            'password': logindata.password
    }

@pytest.fixture(scope='function')
def getCookies(driver, getCredentials):
    base_case = BaseCase()
    base_case.driver = driver
    base_case.login_page = LoginPage(driver)
    base_case.login_and_verify(getCredentials['email'], getCredentials['password'], MainPage.url)
    cookies = driver.get_cookies()
    return cookies

class MainPage(BasePage):
    url = conftest.vk_feed_url


class TestLogin(BaseCase):
    authorize = True

    def test_login(self, getCredentials):
        self.login_and_verify(getCredentials['email'], getCredentials['password'], MainPage.url)

class TestLK(BaseCase):


    def test_find_name(self, getCookies):
        self.set_cookie(getCookies)
        self.login_page.click(self.locators.SEARCH_BUTTON)
        self.people_page.search_name(search_data['name'], search_data['last_name'])
        # Проверка
        self.people_page.validate_search(search_data['name'], search_data['last_name'])

    def test_find_room(self, getCookies):
        self.set_cookie(getCookies)
        self.schedule_page.find_room_in_schedule(search_data['date'], search_data['room'])
