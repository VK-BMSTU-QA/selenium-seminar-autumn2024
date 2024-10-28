import os

import pytest
from _pytest.fixtures import FixtureRequest
from dotenv import load_dotenv
from selenium.webdriver.remote.webdriver import WebDriver

from ui.pages.feed_page import FeedPage
from ui.pages.login_page import LoginPage
from ui.pages.people_page import PeoplePage
from ui.pages.schedule_page import SchedulePage


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
    SCHEDULE_DATE = '22 октября 2024'
    SCHEDULE_LOCATION = 'ауд.395 - зал 3 (МГТУ)'

    PERSON_SEARCH_QUERY = 'Кристина'
    PERSON_NAME = 'Кристина Буйдина'
    PERSON_DESCRIPTION = '>> Нажмите, чтобы развернуть <<'

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
        self.schedule_page.select_interval('all_time')
        self.schedule_page.select_subject('Обеспечение качества в разработке ПО')
        schedule = self.schedule_page.get_schedule()
        # будем делать проверку согласно заданию, хотя в реальности расписание может меняться и тесты могут падать
        assert self.SCHEDULE_DATE in schedule.keys()
        assert schedule.get(self.SCHEDULE_DATE).get('location') == self.SCHEDULE_LOCATION

    def test_find_friend(self, request):
        request.getfixturevalue('setup_people_page')
        # по заданию нужно найти друга, будем искать Кристину Буйдину среди всех студентов с таким именем
        people = self.people_page.search_people(self.PERSON_SEARCH_QUERY)
        # надпись "нажмите, чтобы развернуть" - не ссылка, а реальное описание в профиле у Кристины :)
        assert (self.PERSON_NAME, self.PERSON_DESCRIPTION) in people
