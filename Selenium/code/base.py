import pytest
from _pytest.fixtures import FixtureRequest

from ui.pages.base_page import BasePage
from ui.pages.login_page import LoginPage


class BaseCase:
    authorize = False
    driver = None

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver, config, request: FixtureRequest):
        self.driver = driver
        self.config = config

        self.base_page: BasePage = BasePage(driver)
        self.login_page: LoginPage = LoginPage(driver)
        if self.authorize:
            credentials = request.getfixturevalue("credentials")
            self.main_page = self.login_page.login(*credentials)