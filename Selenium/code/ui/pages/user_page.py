from ui.locators import user_locators
from ui.pages.base_page import BasePage


class UserPage(BasePage):
    locators = user_locators.UserPageLocators()

    def __init__(self, driver, url):
        self.driver = driver
        self.url = url
        self.is_opened()

    def get_about(self):
        about_info = self.find(self.locators.ABOUT_INFO)
        return about_info.text
