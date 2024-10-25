import json
from telnetlib import EC
from time import sleep
import pytest
from _pytest.fixtures import FixtureRequest

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

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver, config, request: FixtureRequest):
        self.driver = driver
        self.config = config

        self.login_page = LoginPage(driver)
        if self.authorize:
            with open('files/userdata.json', 'r') as file:
                userdata = json.load(file)
            login = userdata['login']
            password = userdata['password']
            self.main_page = self.login_page.login(login, password)
            # self.login_page.click(vk_locators.VkPageLocators.LOGIN_BTN, timeout=5)
            # self.login_page.click(vk_locators.VkPageLocators.CONTINUE_WITH_EMAIL_BTN, timeout=5)
            # login_input = self.login_page.find(vk_locators.VkPageLocators.LOGIN_INPUT)
            # login_input.send_keys(login)
            # password_input = self.login_page.find(vk_locators.VkPageLocators.PASSWORD_INPUT)
            # password_input.send_keys(password)
            # self.login_page.click(vk_locators.VkPageLocators.CONFIRM_LOGIN_BTN, timeout=5)
            # self.login_page.find(vk_locators.VkPageLocators.USER_INFO, timeout=5)


@pytest.fixture(scope='session')
def credentials():
        pass


@pytest.fixture(scope='session')
def cookies(credentials, config):
        pass



class LoginPage(BaseVkPage):
    url = 'https://education.vk.company/'


    
    def login(self, user, password):
        self.click(self.locators.LOGIN_BTN, timeout=5)
        self.click(self.locators.CONTINUE_WITH_EMAIL_BTN, timeout=5)
        login_input = self.find(self.locators.LOGIN_INPUT)
        login_input.send_keys(user)
        password_input = self.find(self.locators.PASSWORD_INPUT)
        password_input.send_keys(password)
        self.click(self.locators.CONFIRM_LOGIN_BTN, timeout=5)
        self.find(self.locators.USER_INFO, timeout=5)
        return MainPage(self.driver)



class MainPage(MainVkPage):

    url = 'https://education.vk.company/feed/'


class TestLogin(VkBaseCase):
    authorize = True
    @pytest.mark.skip('skip')
    def test_login(self):
        # with open('files/userdata.json', 'r') as file:
        #     userdata = json.load(file)
        # login = userdata['login']
        # password = userdata['password']
        # self.login_page.click(vk_locators.VkPageLocators.LOGIN_BTN, timeout=5)
        # self.login_page.click(vk_locators.VkPageLocators.CONTINUE_WITH_EMAIL_BTN, timeout=5)
        # login_input = self.login_page.find(vk_locators.VkPageLocators.LOGIN_INPUT)
        # login_input.send_keys(login)
        # password_input = self.login_page.find(vk_locators.VkPageLocators.PASSWORD_INPUT)
        # password_input.send_keys(password)
        # self.login_page.click(vk_locators.VkPageLocators.CONFIRM_LOGIN_BTN, timeout=5)
        # sleep(5) # пока не понял как  дожидаться загрузки нормально
        # with open('files/userdata.json', 'r') as file:
        #     userdata = json.load(file)
        # login = userdata['login']
        # password = userdata['password']
        # self.login_page.login(login, password)
        current_url = self.driver.current_url
        assert current_url == 'https://education.vk.company/feed/'


class TestLK(VkBaseCase):

    @pytest.mark.skip('skip')
    def test_auth(self):
        current_url = self.driver.current_url
        assert current_url == 'https://education.vk.company/feed/'

    @pytest.mark.skip('skip')
    def test_find_classmate(self):

        with open('files/userdata.json', 'r', encoding='utf-8') as file:
            userdata = json.load(file)
        username = userdata['username']

        self.main_page.click(self.main_page.locators.PEOPLE_BTN, timeout=5)

        name_input = self.main_page.find(self.main_page.locators.SEARCH_BY_NAME, timeout=5)
        name_input.send_keys(username)
        self.main_page.click(self.main_page.locators.SEARCH_BY_NAME_BTN, timeout=5)

        #избыточно, но для исключения тёсок самое то
        self.main_page.select(self.main_page.locators.GROUPS, "Студент") 
        self.main_page.select(self.main_page.locators.SEMESTERS, "Осень 2023")
        
        self.main_page.click(self.main_page.locators.GO_TO_ACCOUNT, timeout=5)
        self.main_page.find(self.main_page.locators.PEOPLE_BTN, timeout=5)
        assert 'https://education.vk.company/profile/' in self.driver.current_url

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

    
