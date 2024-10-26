from ui.locators.basic_locators import MainPageLocators
from ui.pages.base_page import BasePage
from ui.pages.main_page import MainPage

class LandingPage(BasePage):

    locators = LandingPageLocators
    url = 'https://education.vk.company/'

    def login(self, email, password):
        self.driver.maximize_window()
        self.click(self.locators.LOGIN_BUTTON, timeout=self.default_timeout)
        self.click(self.locators.LOGIN_WITH_EMAIL, timeout=self.default_timeout)
        self.input(self.locators.EMAIL_INPUT, email, timeout=self.default_timeout)
        self.input(self.locators.PASSWORD_INPUT, password, timeout=self.default_timeout)
        self.click(self.locators.SUBMIT_BUTTON, timeout=self.default_timeout)
        return MainPage(self.driver)