import pytest
import time
import os
from _pytest.fixtures import FixtureRequest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from ui.pages.base_page import BasePage
from ui.locators import basic_locators as BC

class BaseCase:
    authorize = True

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver, config, request: FixtureRequest):
        self.driver = driver
        self.config = config

        self.login_page = LoginPage(driver)
        if self.authorize:
            print('Do something for login')

@pytest.fixture(scope='session')
def credentials():
    return {
        "username": os.getenv("username"),
        "password": os.getenv("password")
    }

@pytest.fixture(scope='session')
def cookies(credentials, config):
        pass

class LoginPage(BasePage):
    url = 'https://education.vk.company/'

    def login(self, user, password):
        self.driver.get(self.url)

        self.click(BC.LoginPageLocators.LOGIN_BUTTON, 10)

        self.click(BC.LoginPageLocators.LOGIN_BUTTON_CHOOSE, 10)

        email_input_box = self.find(BC.LoginPageLocators.INPUT_USER, 10)
        email_input_box.send_keys(user)

        email_input_box = self.find(BC.LoginPageLocators.INPUT_PASS, 10)
        email_input_box.send_keys(password)

        self.click(BC.LoginPageLocators.LOGIN, 10)
        return MainPage(self.driver)

class MainPage(BasePage):
    url = 'https://education.vk.company/feed/'

    def click_people_icon(self):
        self.click(BC.MainPageLocators.SEARCH_PEOPLE_ICON, 10)

    def search_input(self, search_queries):
        search_input = self.find(BC.MainPageLocators.SEARCH_INPUT)
        search_input.send_keys(search_queries)

    def click_search_button(self):
        self.click(BC.MainPageLocators.CLICK_SEARCH_BUTTON, 10)

    def click_user(self):
        self.click(BC.MainPageLocators.CLICK_USER, 10)

    def get_user_info(self):
        profile_element = self.find(BC.MainPageLocators.PROFILE_ELEMENT)
        about_element, birthday_element = [el.text for el in
                                           profile_element.find_elements(*BC.MainPageLocators.GET_USER_INFO_ABOUT)]

        return {
            "about": about_element,
            "birthday": birthday_element
        }

    def click_program_icon(self):
        self.click(BC.MainPageLocators.CLICK_PROGRAM_ICON, 10)

    def select_program(self):
        self.click(BC.MainPageLocators.SELECT_PROGRAM, 10)

    def select_lesson(self):
        self.click(BC.MainPageLocators.SELECT_LESSON, 10)

    def click_selected_lesson(self):
        self.click(BC.MainPageLocators.CLICK_SELECTED_LESSON, 10)

    def get_lesson_info(self):
        info_element = WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located((By.CLASS_NAME, 'block-content')))
        date_info = info_element.find_element(By.XPATH, ".//div[contains(@class, 'info-pair')]/strong[text()='Дата проведения']/following-sibling::span").text
        location_info = info_element.find_element(By.XPATH, ".//div[contains(@class, 'info-pair')]/strong[text()='Место проведения']/following-sibling::span").text

        return {
            "date": date_info,
            "location": location_info
        }
