from selenium.webdriver.common.keys import Keys

from ui.locators.basic_locators import MainPageLocators
from ui.pages.base_page import BasePage


class MainPage(BasePage):

    locators = MainPageLocators
    url = 'https://education.vk.company/feed/'
    default_timeout = 10

    def open_main(self):
        self.driver.get(self.url)

    def find_student(self, student_name):
        self.click(self.locators.QUERY_BUTTON, timeout=self.default_timeout)
        self.input(self.locators.QUERY_INPUT, student_name, timeout=self.default_timeout)
        self.input(self.locators.QUERY_INPUT, Keys.ENTER, timeout=self.default_timeout)
        self.click(self.locators.PROFILE_NAME_LOCATOR, timeout=self.default_timeout)

    def find_current_lesson_info(self):
        self.click(self.locators.SCHEDULE_LINK, timeout=self.default_timeout)
        self.click(self.locators.CURRENT_LESSON_LOCATOR,timeout=self.default_timeout)
