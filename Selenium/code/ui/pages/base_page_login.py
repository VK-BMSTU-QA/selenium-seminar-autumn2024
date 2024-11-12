import time

import allure
from selenium.webdriver.remote.webelement import WebElement
from selenium.common.exceptions import TimeoutException
from ui.locators import basic_locators_login
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver


class PageNotOpenedExeption(Exception):
    pass


class BasePage(object):

    locators = basic_locators_login.BasePageLocators()
    url = 'https://education.vk.company/'

    def is_opened(self, timeout=10):
        started = time.time()
        while time.time() - started < timeout:
            # print(self.driver.current_url)
            if self.driver.current_url == self.url:
                return True
        raise PageNotOpenedExeption(f'{self.url} did not open in ' +
                                    f'{timeout} sec, current url {self.driver.current_url}')

    def __init__(self, driver):
        self.driver: WebDriver = driver
        self.is_opened()

    def wait(self, timeout=5):
        return WebDriverWait(self.driver, timeout=timeout)

    def find(self, locator, timeout=0) -> WebElement:
        try:
            return self.wait(timeout).until(
                EC.presence_of_element_located(locator))
        except TimeoutException:
            print(f'TimeoutException occured: unable to find element during {timeout}s timeout')
            return None

    def click(self, locator, timeout=0):
        element = self.find(locator, timeout)
        if element != None:
            element.click()

    def send_keys(self, locator, data, timeout=0):
        try:
            item = self.find(locator, timeout)
            item.clear()
            item.send_keys(data)
        except TimeoutException:
            return None