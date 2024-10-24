import pytest

from ui.pages.base_page import BasePage
from ui.pages.login_page import LoginPage


class BaseCase:
    driver = None

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver, config):
        self.driver = driver
        self.config = config

        self.base_page: BasePage = BasePage(driver)
        self.login_page: LoginPage = LoginPage(driver)
