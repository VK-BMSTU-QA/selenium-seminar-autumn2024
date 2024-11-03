import json
import os
from telnetlib import EC
from time import sleep
import pytest
from _pytest.fixtures import FixtureRequest
import allure

from selenium.webdriver.support.wait import WebDriverWait

from ui.pages.main_vk_page import MainVkPage
from ui.locators import vk_locators
from ui.pages.base_vk_page import BaseVkPage
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


class VkBaseCase:
    authorize = True

    @pytest.fixture(scope='session')
    def userdata(self):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        filepath = os.path.join(base_dir, 'files/userdata.json')
        with open(filepath, 'r', encoding='utf-8') as file:
            data = json.load(file)
        yield data

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver, config, request: FixtureRequest, userdata):
        self.driver = driver
        self.config = config

        self.login_page = LoginPage(driver)
        if self.authorize:
            self.login_page.authorize(userdata)
            self.main_page = MainPage(self.driver)
        self.username = userdata['username']


@pytest.fixture(scope='session')
def credentials():
        pass


@pytest.fixture(scope='session')
def cookies(credentials, config):
        pass



class LoginPage(BaseVkPage):
    url = 'https://education.vk.company/'



class MainPage(MainVkPage):

    url = 'https://education.vk.company/feed/'


class TestLogin(VkBaseCase):
    authorize = True

    # @pytest.mark.skip('skip')
    @allure.title('Тест авторизации внутри страницы')
    def test_login(self):
        current_url = self.driver.current_url
        assert current_url == 'https://education.vk.company/feed/'


class TestLK(VkBaseCase):

    # @pytest.mark.skip('skip')
    @allure.title('Тест авторизации внутри класса TestLK')
    def test_auth(self):
        current_url = self.driver.current_url
        assert current_url == 'https://education.vk.company/feed/'

    @allure.title('Тест поиска одногруппника на портале')
    def test_find_classmate(self, request: FixtureRequest, userdata):

        self.main_page.click(self.main_page.locators.PEOPLE_BTN, timeout=5)

        name_input = self.main_page.find(self.main_page.locators.SEARCH_BY_NAME, timeout=5)
        name_input.send_keys(self.username) 
        self.main_page.click(self.main_page.locators.SEARCH_BY_NAME_BTN, timeout=5)

        #избыточно, но для исключения тёсок самое то
        # self.main_page.select(self.main_page.locators.GROUPS, "Студент") 
        # self.main_page.select(self.main_page.locators.SEMESTERS, "Осень 2023")
        
        self.main_page.find(self.main_page.locators.GO_TO_ACCOUNT, timeout=5)
        self.main_page.click(self.main_page.locators.GO_TO_ACCOUNT, timeout=10)
        self.main_page.find(self.main_page.locators.PEOPLE_BTN, timeout=5)
        assert 'https://education.vk.company/profile/' in self.driver.current_url

    # @pytest.mark.skip('skip')
    @allure.title('Тест поиска текущего занятия на портале')
    def test_open_lesson(self):

        self.main_page.click(self.main_page.locators.SHEDULE_BTN, timeout=5)
        self.main_page.click(self.main_page.locators.SHOW_SEMESTER, timeout=5)
        self.main_page.click(self.main_page.locators.CHOOSE_DISCIPLINE, timeout=5)
        self.main_page.click(self.main_page.locators.CHOOSE_QA, timeout=5)
        self.main_page.click(self.main_page.locators.CHOOSE_LESSON, timeout=5)
        original_window = self.driver.current_window_handle
        WebDriverWait(self.driver, 10).until(
            lambda d: len(d.window_handles) > 1
        )

        all_windows = self.driver.window_handles

        for window in all_windows:
            if window != original_window:
                self.driver.switch_to.window(window)
                break

        assert "https://education.vk.company/curriculum/program/lesson/28796/" in self.driver.current_url

        pass

    
