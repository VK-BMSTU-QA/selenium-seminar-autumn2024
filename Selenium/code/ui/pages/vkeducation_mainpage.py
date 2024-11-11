import time

from selenium.webdriver.common.keys import Keys

from ui.locators.vkeducation_locators import MainPageLocators
from ui.pages.base_page import BasePage


class MainPage(BasePage):
    locators = MainPageLocators()
    url = "https://education.vk.company/feed/"

    def open(self):
        self.driver.get(self.url)

    def get_student(self, name):
        self.click(self.locators.PEOPLE_BNT, timeout=20)
        self.input(self.locators.SEARCH_FIELD, name, timeout=20)
        self.input(self.locators.SEARCH_FIELD, Keys.ENTER, timeout=20)
        self.click(self.locators.PROFILE_AVATAR, timeout=20)

    def get_lesson(self):
        self.click(self.locators.SCHEDULE_BTN, timeout=20)
        self.click(self.locators.SHOW_FULL_SCHEDULE_BTN, timeout=20)
        lesson_data = self.find(self.locators.CURRENT_LESSON_BTN).text
        self.click(self.locators.CURRENT_LESSON_BTN, timeout=20)

        return lesson_data
