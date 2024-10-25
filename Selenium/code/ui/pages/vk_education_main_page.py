from selenium.webdriver.common.keys import Keys

from ui.pages.base_page import BasePage
from ui.locators.vk_education_locators import MainPageLocators

class MainPage(BasePage):

    locators = MainPageLocators
    url = 'https://education.vk.company/feed/'

    def open_main(self):
        self.driver.get(self.url)

    def find_student(self, student_name):
        self.click(self.locators.QUERY_BUTTON, timeout=100)
        self.input(self.locators.QUERY_INPUT, student_name, timeout=10)
        self.input(self.locators.QUERY_INPUT, Keys.ENTER, timeout=10)
        self.click(self.locators.PROFILE_LOCATOR, timeout=10)

    def find_current_lesson_info(self):
        self.click(self.locators.SCHEDULE_BUTTON, timeout=10)
        self.click(self.locators.CURRENT_LESSON_LOCATOR,timeout=100)
