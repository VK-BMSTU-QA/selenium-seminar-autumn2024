import time

import allure
from selenium.common import TimeoutException
from selenium.webdriver.remote.webelement import WebElement
from ui.locators import vk_locators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage(object):
    locators = vk_locators.LoginPageLocators()
    locators_main = vk_locators.MainPageLocators()
    url = 'https://education.vk.company/'

    def is_opened(self):
        return self.driver.current_url == self.url

    def __init__(self, driver):
        self.driver = driver
        self.is_opened()

    def wait(self, timeout=None):
        if timeout is None:
            timeout = 5
        return WebDriverWait(self.driver, timeout=timeout)

    def find(self, locator, timeout=None):
        try:
            return self.wait(timeout).until(EC.presence_of_element_located(locator))
        except TimeoutException as e:
            raise TimeoutException(f"Element with locator {locator} not found. Waited {timeout} seconds.") from e

    @allure.step('Click')
    def click(self, locator, timeout=10) -> WebElement:
        self.find(locator, timeout=timeout)
        elem = self.wait(timeout).until(EC.element_to_be_clickable(locator))
        elem.click()
