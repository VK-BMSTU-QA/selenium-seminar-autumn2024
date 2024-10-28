import time
import pytest
from _pytest.fixtures import FixtureRequest

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
        self.cresentials = credentials

        self.login_page = LoginPage(driver)
        self.locators = basic_locators.BasePageLocators()
        if self.authorize:
            print('Do something for login')


@pytest.fixture(scope='session')
def credentials():
        return {
            'email': logindata.email,
            'password': logindata.password
    }


@pytest.fixture(scope='function')
def cookies(driver, credentials):
    login_page = LoginPage(driver)
    login_page.login(credentials['email'], credentials['password'])

    WebDriverWait(driver, 10).until(
        EC.url_to_be(MainPage.url)
    )
    assert driver.current_url == MainPage.url, "URL не соответствует ожидаемому"

    cookies = driver.get_cookies()
    return cookies


class LoginPage(BasePage):
    url = conftest.vk_url

    
    def login(self, email, password):
        self.click(self.locators.AUTH_HEADER_BUTTON)
        self.click(self.locators.SIGNUP_MODAL_LINK)
        self.input(self.locators.EMAIL_INPUT, email)
        self.input(self.locators.PASSWORD_INPUT, password)
        self.click(self.locators.LOGIN_BUTTON)



class MainPage(BasePage):
    url = conftest.vk_feed_url


class TestLogin(BaseCase):
    authorize = True

    def wait_for_url(self, url):
        WebDriverWait(self.driver, 10).until(
            EC.url_to_be(url)
        )

    def test_login(self, credentials):
        self.login_page.login(credentials['email'], credentials['password'])
        self.wait_for_url(MainPage.url)
        assert self.login_page.driver.current_url == MainPage.url, "URL не соответствует ожидаемому"


class TestLK(BaseCase):

    def set_cookie(self, cookies):
        self.driver.get(MainPage.url)
        for cookie in cookies:
            self.driver.add_cookie(cookie)
        self.driver.refresh()

    def search_name(self, name, last_name):
        search_input = self.login_page.find(self.locators.SEARCH_INPUT)
        search_input.send_keys(name + ' ' + last_name)
        search_input.send_keys(Keys.ENTER)

    def validate_search(self, name, last_name):
        found_name = self.login_page.find(self.locators.FOUND_NAME).text
        assert found_name == name, f"Ожидалось имя '{name}', но найдено '{found_name}'"
        found_last_name = self.login_page.find(self.locators.FOUND_LAST_NAME).text
        assert found_last_name == last_name, f"Ожидалась фамилия '{last_name}', но найдена '{found_last_name}'"

    def find_room_in_schedule(self, date, room, schedule_items):
        for item in schedule_items:
            date_text = item.find_element(*self.locators.SCHEDULE_ITEM_DATE).text
            if date_text == date:
                room_text = item.find_element(*self.locators.SCHEDULE_ITEM_ROOM).text
                assert room_text == room, f"Ожидается '{room}', но найдено '{room_text}'"
                break
        else:
            assert False, f"Элемент с датой '{date}' не найден"

    def test_find_name(self, cookies):
        self.set_cookie(cookies)
        self.login_page.click(self.locators.SEARCH_BUTTON)
        self.search_name(search_data['name'], search_data['last_name'])
        # Проверка
        self.validate_search(search_data['name'], search_data['last_name'])


    def test_find_room(self, cookies):
        self.set_cookie(cookies)
        # зайти в расписание
        self.login_page.click(self.locators.SCHEDULE_BUTTON)
        time.sleep(2)
        # кнопка "Весь семестр"
        self.login_page.click(self.locators.SEMESTER_BUTTON)
        time.sleep(10)
        schedule_items = WebDriverWait(
            self.driver, 10).until(EC.presence_of_all_elements_located(self.locators.SCHEDULE_ITEM))
        self.find_room_in_schedule(search_data['date'], search_data['room'], schedule_items)

