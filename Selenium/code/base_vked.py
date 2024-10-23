import time
from contextlib import contextmanager

import pytest
from _pytest.fixtures import FixtureRequest
from ui.locators.vked_locators import AuthPageLocators

CLICK_RETRY = 3


class BaseCaseVkEd:
    authorize = True
    driver = None

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

        self.login_page = (request.getfixturevalue('login_vked_page'))
        self.email = (request.getfixturevalue('credentials_vked'))['email']
        self.password = (request.getfixturevalue('credentials_vked'))['password']

        if self.authorize:
            self.login_page.click(AuthPageLocators.REG_BTN_LOC)
            self.login_page.click(AuthPageLocators.GO_WITH_EMAIL_BTN_LOC)
            self.login_page.enter_field(AuthPageLocators.EMAIL_INP_LOC, self.email)
            self.login_page.enter_field(AuthPageLocators.PASSWORD_INP_LOC, self.password)
            self.login_page.click(AuthPageLocators.SUBMIT_ENTER_BTN_LOC)
            print('Do something for login')
            time.sleep(4)