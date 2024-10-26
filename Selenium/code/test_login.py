import time

import pytest
import json
import os
from _pytest.fixtures import FixtureRequest
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from ui.pages.base_page import BasePage

class BaseCase:
    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver, config, request: FixtureRequest):
        self.driver = driver
        self.config = config
        request.addfinalizer(self.teardown)

    def teardown(self):
        self.driver.delete_all_cookies()

@pytest.fixture(scope='session')
def credentials():
    file_path = os.path.join(os.path.dirname(__file__), 'files', 'credentials.json')
    with open(file_path, 'r') as f:
        return json.load(f)


@pytest.fixture(scope='session')
def cookies(credentials, driver):
    login_page = LoginPage(driver)
    login_page.login(credentials['login'], credentials['password'])

    return driver.get_cookies()


class LoginPage(BasePage):
    url = 'https://education.vk.company/'

    def login(self, user, password):
        login_button = self.find(self.locators.LOGIN_BUTTON)
        login_button.click()
        use_email_and_password_button = self.find(self.locators.USE_EMAIL_AND_PASSWORD_BUTTON)
        use_email_and_password_button.click()
        email_input = self.find(self.locators.EMAIL_INPUT)
        email_input.send_keys(user)
        password_input = self.find(self.locators.PASSWORD_INPUT)
        password_input.send_keys(password)
        submit_button = self.find(self.locators.SUBMIT_BUTTON)
        submit_button.click()

        WebDriverWait(self.driver, 15).until(
            EC.url_contains("/feed/")
        )


class MainPage(BasePage):
    url = 'https://education.vk.company/feed/'

class SchedulePage(BasePage):
    url = 'https://education.vk.company/schedule/'

class PersonPage(BasePage):
    url = 'https://education.vk.company/people/'

class TestLogin(BaseCase):
    @pytest.fixture(autouse=True)
    def setup_login_page(self, driver):
        self.login_page = LoginPage(driver)

    # 1. авторизация
    def test_login(self, credentials):
        self.login_page.login(credentials["login"], credentials["password"])
        assert self.driver.current_url == MainPage.url

class TestLK(BaseCase):
    @pytest.fixture(autouse=True)
    def setup_cookies(self, cookies):
        for cookie in cookies:
            self.driver.add_cookie(cookie)

    @pytest.fixture()
    def setup_schedule_page(self, driver):
        self.schedule_page = SchedulePage(self.driver)

    @pytest.fixture()
    def setup_person_page(self, driver):
        self.person_page = PersonPage(self.driver)

    # 2. найти человека в лк и получить информацию "о себе"
    def test_lk1(self, request):
        request.getfixturevalue('setup_person_page')
        people_button = self.person_page.find(self.person_page.locators_person.PEOPLE_BUTTON)
        people_button.click()
        search_field = self.person_page.find(self.person_page.locators_person.SEARCH_FIELD)
        search_field.send_keys("Александр Горбатов")
        search_field.send_keys(Keys.ENTER)
        person_block = self.person_page.find(self.person_page.locators_person.PERSON_BLOCK)
        person_block.click()
        about_info = self.person_page.find(self.person_page.locators_person.ABOUT_INFO)
        assert about_info.text == "Пользователь не заполнил раздел \"О себе\""

    # 3. узнать аудиторию занятия по QA 22.10.2024
    def test_lk2(self, request):
        request.getfixturevalue('setup_schedule_page')
        schedule_button = self.schedule_page.find(self.schedule_page.locators_schedule.SCHEDULE_BUTTON)
        schedule_button.click()
        time.sleep(2)
        semester_interval = self.schedule_page.find(self.schedule_page.locators_schedule.SEMESTER_INTERVAL)
        semester_interval.click()
        dropdown = self.schedule_page.find(self.schedule_page.locators_schedule.DROPDOWN)
        dropdown.click()
        my_groups_option = self.schedule_page.find(self.schedule_page.locators_schedule.MY_GROUPS_OPTION)
        my_groups_option.click()
        lesson_block = self.schedule_page.find(self.schedule_page.locators_schedule.LESSON_BLOCK)
        lesson_block.click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        class_info = self.schedule_page.find(self.schedule_page.locators_schedule.CLASS_INFO)
        assert class_info.text == "Аудитория ауд.395 - зал 3 (МГТУ) и Онлайн (ссылки пока нет)"