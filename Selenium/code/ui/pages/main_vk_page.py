import json
import os
import time

import allure
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.select import Select
from ui.locators import vk_locators
from ui.locators import basic_locators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class PageNotOpenedExeption(Exception):
    pass


class MainVkPage(object):

    locators = vk_locators.MainVkPageLocators()
    url = 'https://education.vk.company/feed/'

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

    @allure.step('Click')
    def click(self, locator, timeout=None) -> WebElement:
        self.find(locator, timeout=timeout)
        elem = self.wait(timeout).until(EC.element_to_be_clickable(locator))
        elem.click()

    @allure.step('Select')
    def select(self, locator, option):
        select_element = self.find(locator, timeout=5)
        select = Select(select_element)
        select.select_by_value(option)
        

        

