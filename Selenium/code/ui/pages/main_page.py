from selenium.webdriver.common.by import By

import allure
from ui.locators import basic_locators
from ui.pages.base_page import BasePage


class MainPage(BasePage):

    locators = basic_locators.MainPageLocators()
