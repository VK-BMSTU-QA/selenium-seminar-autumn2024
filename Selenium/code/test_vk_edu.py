import os
import time
from typing import Literal

import pytest
from _pytest.fixtures import FixtureRequest
from dotenv import load_dotenv
from selenium.webdriver.remote.webdriver import WebDriver

from ui.locators.vk_edu_locators import LoginPageLocators, SchedulePageLocators, PeoplePageLocators
from ui.pages.base_page import BasePage


class LoginPage(BasePage):
    url = 'https://education.vk.company/'

    def login(self, user, password):
        self.click(LoginPageLocators.AUTH_OR_REG_BUTTON)
        self.click(LoginPageLocators.SIGN_UP_BUTTON)
        self.find(LoginPageLocators.EMAIL_INPUT).send_keys(user)
        self.find(LoginPageLocators.PASSWORD_INPUT).send_keys(password)
        self.click(LoginPageLocators.LOGIN_BUTTON)
        # ждем, когда загрузится следующая страница
        self.wait().until(lambda d: d.current_url != self.url and 'auth' not in d.current_url)


class FeedPage(BasePage):
    # По заданию первую страницу тестировать не нужно, так что этот класс используется только для получения url
    url = 'https://education.vk.company/feed/'


class SchedulePage(BasePage):
    url = 'https://education.vk.company/schedule/'

    def get_schedule(self, time_interval: Literal['all_time', 'two_weeks'] = 'all_time', subject: str = 'Обеспечение качества в разработке ПО') -> dict:
        if time_interval == 'two_weeks':
            self.click(SchedulePageLocators.SCHEDULE_TWO_WEEKS_INTERVAL)
        else:
            self.click(SchedulePageLocators.SCHEDULE_ALL_TIME_INTERVAL)

        if subject:
            # чтобы не ждать загрузки огромного расписания, конкретизируем его до выбранного предмета
            self.click(SchedulePageLocators.SUBJECTS_LIST)  # открываем список предметов
            self.click(SchedulePageLocators.SUBJECT_LIST_ELEM(subject))  # выбираем нужный предмет

        # у элемента должен пропасть класс loading
        self.wait().until(lambda d: 'loading' not in self.find(SchedulePageLocators.SCHEDULE_TABLE).get_attribute('class'))
        time.sleep(0.5)  # на работу js, который подгружает расписание из полученного результата

        schedule = dict()
        rows = self.driver.find_elements(*SchedulePageLocators.ROWS)

        for row in rows:
            date = row.find_element(*SchedulePageLocators.ROW_DATE).text.strip()
            event = row.find_element(*SchedulePageLocators.ROW_EVENT).text.strip()
            location = row.find_element(*SchedulePageLocators.ROW_LOCATION).text.strip()

            schedule[date] = {
                'event': event,
                'location': location,
            }

        return schedule


class PeoplePage(BasePage):
    url = 'https://education.vk.company/people/'

    def search_people(self, name: str) -> list[tuple[str, str]]:
        self.find(PeoplePageLocators.SEARCH_INPUT).send_keys(name)
        self.click(PeoplePageLocators.SEARCH_BUTTON)
        # ждем, когда загрузится страница с результатами поиска
        time.sleep(8)
        result = []
        rows = self.driver.find_elements(*PeoplePageLocators.ROWS)
        for row in rows:
            result.append(
                (
                    row.find_element(*PeoplePageLocators.ROW_NAME).text,
                    row.find_element(*PeoplePageLocators.ROW_DESCRIPTION).text
                )
            )
        return result


class BaseCase:
    driver: WebDriver
    config: dict

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver, config, request: FixtureRequest):
        self.driver = driver
        self.config = config
        request.addfinalizer(self.teardown)

    def teardown(self):
        self.driver.delete_all_cookies()


@pytest.fixture(scope='session')
def credentials() -> dict:
    load_dotenv()
    return {
        'login': os.getenv('LOGIN'),
        'password': os.getenv('PASSWORD')
    }


@pytest.fixture(scope='session')
def cookies(credentials, driver) -> list[dict]:
    login_page = LoginPage(driver)
    login_page.login(credentials['login'], credentials['password'])
    # помимо сессии могут быть нужны и другие куки, поэтому возвращаем полный список
    return driver.get_cookies()


class TestLogin(BaseCase):
    @pytest.fixture(autouse=True)
    def setup_login_page(self, driver):
        self.login_page = LoginPage(driver)

    def test_login(self, credentials):
        self.login_page.login(credentials['login'], credentials['password'])
        # проверяем, что мы перешли на страницу ленты
        assert self.driver.current_url == FeedPage.url


class TestLK(BaseCase):
    @pytest.fixture(autouse=True)
    def setup_cookies(self, cookies):
        for cookie in cookies:
            self.driver.add_cookie(cookie)

    @pytest.fixture()
    def setup_schedule_page(self, driver):
        self.schedule_page = SchedulePage(self.driver)

    @pytest.fixture()
    def setup_people_page(self, driver):
        self.people_page = PeoplePage(self.driver)

    def test_schedule(self, request):
        request.getfixturevalue('setup_schedule_page')
        schedule = self.schedule_page.get_schedule()
        # будем делать проверку согласно заданию, хотя в реальности расписание может меняться и тесты могут падать
        assert '22 октября 2024' in schedule.keys()
        assert schedule.get('22 октября 2024').get('location') == 'ауд.395 - зал 3 (МГТУ)'

    def test_find_friend(self, request):
        request.getfixturevalue('setup_people_page')
        query = 'Кристина'
        # по заданию нужно найти друга, будем искать Кристину Буйдину среди всех студентов с таким именем
        people = self.people_page.search_people(query)
        # надпись "нажмите, чтобы развернуть" - не ссылка, а реальное описание в профиле у Кристины :)
        assert ('Кристина Буйдина', '>> Нажмите, чтобы развернуть <<') in people
