from contextlib import contextmanager

import pytest
from ui.pages.vk_edu_login_page import LoginPage


class BaseCase:
    driver = None
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
    def setup(self, driver, config, credentials):
        self.driver = driver
        self.config = config

        self.login_page = LoginPage(self.driver)
        self.main_page = None

        if self.authorize:
            email = credentials["email"]
            password = credentials["password"]

            self.main_page = self.login_page.login(email, password)
