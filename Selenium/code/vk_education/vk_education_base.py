from contextlib import contextmanager

import pytest

from ui.pages.vk_education_landing import LandingPage


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
    def setup(self, driver, config, credentials):
        self.driver = driver
        self.config = config

        self.landing_page = LandingPage(driver)
        if self.authorize:
            email = credentials['EMAIL']
            password = credentials['PASSWORD']
            self.main_page = self.landing_page.login(email, password)