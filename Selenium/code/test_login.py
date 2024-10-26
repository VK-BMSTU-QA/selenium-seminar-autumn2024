import time
import os
import pytest
from contextlib import contextmanager
from dotenv import load_dotenv
from _pytest.fixtures import FixtureRequest
from ui.pages.base_page_login import BasePage
from ui.locators import basic_locators_login
from selenium.webdriver.common.by import By

load_dotenv()


class BaseCase:
    authorize = True

    @contextmanager
    def switch_to_window(self, current, close=False):
        for w in self.driver.window_handles:
            if w != current:
                self.driver.switch_to.window(w)
                break
        yield
        if close:
            self.driver.close()
        self.driver.switch_to.window(current)

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
        'email': os.getenv('EMAIL'),
        'password': os.getenv('PASSWORD')
    }


@pytest.fixture(scope='session')
def cookies(credentials, config):
    pass


class LoginPage(BasePage):
    url = 'https://education.vk.company/'

    def open_login_modal(self):
        self.click(self.locators.OPEN_AUTH_MODAL_BUTTON, 2)
        self.click(self.locators.LOG_IN_WITH_CREDENTIALS_BUTTON, 2)

    def login(self, user, password):
        self.open_login_modal()
        self.send_keys(self.locators.EMAIL_INPUT, user, 2)
        self.send_keys(self.locators.PASSWORD_INPUT, password, 2)
        self.click(self.locators.LOG_IN_BUTTON, 2)
        user_agreement = self.find(self.locators.USER_AGREEMENT_CHECK, 3)
        if (user_agreement != None):
            user_agreement.click()
            self.click(self.locators.LOG_IN_BUTTON, 2)
        return MainPage(self.driver)


class MainPage(BasePage):
    url = 'https://education.vk.company/feed/'
    locators_main = basic_locators_login.MainPageLocators()

    def search(self, query):
        self.send_keys(self.locators_main.SEARCH_BAR, query)
        self.find(self.locators_main.SEARCH_FORM).submit()

    def open_schedule(self):
        self.click(self.locators_main.SCHEDULE)
        return SchedulePage(self.driver)


class SchedulePage(BasePage):
    url = 'https://education.vk.company/schedule/'
    locators_schedule = basic_locators_login.SchedulePageLocators()

    def click_lesson(self, id):
        self.click(
            (By.XPATH, f"//a[@href='/curriculum/program/lesson/{id}/']"), 10)
        return LessonPage(self.driver, id)


class LessonPage(BasePage):
    locators_lesson = basic_locators_login.LessonPageLocators()

    def __init__(self, driver, id):
        self.url = 'https://education.vk.company/curriculum/' + \
            f'program/lesson/{id}/'
        self.driver = driver

    def get_header(self):
        return self.find(self.locators_lesson.LESSON_HEADER).text


class TestLogin(BaseCase):
    authorize = True

    def test_login(self, credentials):
        self.login_page.login(credentials['email'], credentials['password'])
        assert self.driver.current_url == 'https://education.vk.company/feed/'


class TestLK(BaseCase):

    def test_search(self, credentials):
        main_page = self.login_page.login(
            credentials['email'], credentials['password'])
        main_page.click(main_page.locators_main.OPEN_SEARCH_BUTTON)
        main_page.search('Никитин')
        assert main_page.find(
            (By.XPATH, "//a[@href='https://education.vk.company/profile/user_188197/']")) != None

    def test_lesson(self, credentials):
        main_page = self.login_page.login(
            credentials['email'], credentials['password'])

        # Open schedule page
        schedule_page = main_page.open_schedule()
        time.sleep(2)
        schedule_page.click(
            schedule_page.locators_schedule.SEMESTER_SCHEDULE)

        # Open lesson page
        current_tab = self.driver.current_window_handle
        lesson_page = schedule_page.click_lesson(28796)
        with self.switch_to_window(current=current_tab, close=False):
            assert lesson_page.get_header() == 'End-to-End тесты на Python'
