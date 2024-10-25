from contextlib import contextmanager

import pytest
from _pytest.fixtures import FixtureRequest
from ui.pages.base_vk_page import BaseVkPage
from ui.pages.main_page import MainPage

CLICK_RETRY = 3


class VkBaseCase:
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

        self.base_vk_page: BaseVkPage = (request.getfixturevalue('vk_page'))
