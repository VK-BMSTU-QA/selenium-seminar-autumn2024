import time

import allure
from selenium.webdriver.remote.webelement import WebElement
from ui.locators.vked_locators import AuthPageLocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


class PageNotOpenedExeption(Exception):
    pass


class LoginPage(object):

    login_locators = AuthPageLocators()
    url = 'https://education.vk.company/'

    def is_opened(self, timeout=15):
        started = time.time()
        while time.time() - started < timeout:
            if self.driver.current_url == self.url:
                return True
        raise PageNotOpenedExeption(f'{self.url} did not open in {timeout} sec, current url {self.driver.current_url}')

    def __init__(self, driver):
        self.driver = driver
        self.is_opened()

    def wait(self, timeout=None):
        if timeout is None:
            timeout = 5
        return WebDriverWait(self.driver, timeout=timeout)

    def find(self, locator, timeout=None):
        return self.wait(timeout).until(EC.presence_of_element_located(locator))

    @allure.step('Search')
    def search(self, query):
        elem = self.find(self.locators.QUERY_LOCATOR_ID)
        elem.send_keys(query)
        go_button = self.find(self.locators.GO_BUTTON_LOCATOR)
        go_button.click()
        self.my_assert()

    @allure.step("Step 1")
    def my_assert(self):
        assert 1 == 1

    @allure.step('Click')
    def click(self, locator, timeout=None) -> WebElement:
        self.find(locator, timeout=timeout)
        elem = self.wait(timeout).until(EC.element_to_be_clickable(locator))
        elem.click()

    @allure.step('EnterField')
    def enter_field(self, locator, value, timeout=None) -> WebElement:
        elem = self.find(locator, timeout)
        elem.clear()
        elem.send_keys(value)

    @allure.step('EnterFieldReturn')
    def enter_field_return(self, locator, value, timeout=None) -> WebElement:
        elem = self.find(locator, timeout)
        elem.clear()
        elem.send_keys(value)
        elem.send_keys(Keys.RETURN)

    @allure.step('CheckText')
    def check_text(self, locator, text, timeout=None) -> WebElement:
        checked = self.wait(timeout).until(EC.text_to_be_present_in_element(locator, text))
        assert checked
