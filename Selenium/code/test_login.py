import pytest
from _pytest.fixtures import FixtureRequest

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


@pytest.fixture(scope='session')
def credentials():
        pass


@pytest.fixture(scope='session')
def cookies(credentials, config):
        pass


class LoginPage(BasePage):
    url = 'https://education.vk.company/'

    def login(self, user, password):
        self.driver.get(self.url)
        return MainPage(self.driver)


class MainPage(BasePage):
    url = 'https://education.vk.company/feed/'


class TestLogin(BaseCase):
    authorize = True

    def test_login(self, credentials):
        pass


class TestLK(BaseCase):

    def test_lk1(self):
        pass

    def test_lk2(self):
        pass

    def test_lk3(self):
        pass
