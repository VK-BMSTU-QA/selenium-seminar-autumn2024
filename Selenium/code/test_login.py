import pytest
import os
from _pytest.fixtures import FixtureRequest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from ui.pages.base_page import BasePage
from ui.locators import basic_locators as BC
import page

@pytest.fixture(scope='session')
def credentials():
    return {
        "username": os.getenv("username"),
        "password": os.getenv("password")
    }

@pytest.fixture(scope='session')
def cookies(credentials, config):
        pass

class TestLogin(page.BaseCase):
    authorize = True

    def test_login(self, credentials):
        main_page = self.login_page.login(credentials["username"], credentials["password"])
        assert main_page.url == page.MainPage.url, "Login successful!"

