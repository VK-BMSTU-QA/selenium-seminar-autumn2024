from ui.locators import user_locators
from ui.pages.base_page import BasePage


class UserPage(BasePage):
    check_url = False
    locators = user_locators.UserPageLocators()

    def get_about(self):
        about_info = self.find(self.locators.ABOUT_INFO)
        return about_info.text
