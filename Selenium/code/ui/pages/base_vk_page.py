import json
import os
import time

import allure
from selenium.webdriver.remote.webelement import WebElement
from ui.locators import vk_locators
from ui.locators import basic_locators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class PageNotOpenedExeption(Exception):
    pass


class BaseVkPage(object):

    locators = vk_locators.VkPageLocators()
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


    @allure.step('Click')
    def click(self, locator, timeout=None) -> WebElement:
        self.find(locator, timeout=timeout)
        elem = self.wait(timeout).until(EC.element_to_be_clickable(locator))
        elem.click()

    @allure.step('Authorize')
    def authorize(self, userdata):
        login = userdata['login']
        password = userdata['password']
        self.click(self.locators.LOGIN_BTN, timeout=5)
        self.click(self.locators.CONTINUE_WITH_EMAIL_BTN, timeout=5)
        login_input = self.find(self.locators.LOGIN_INPUT)
        login_input.send_keys(login)
        password_input = self.find(self.locators.PASSWORD_INPUT)
        password_input.send_keys(password)
        self.click(self.locators.CONFIRM_LOGIN_BTN, timeout=5)
        self.find(self.locators.USER_INFO, timeout=5) # для ожмдания загрузки страницы (перехода)
        

