from ui.pages.vk_education_base import BasePage
from ui.pages.vk_education_main import MainPage
from ui.locators.vk_education_locators import LandingPageLocators

class LandingPage(BasePage):

    locators = LandingPageLocators
    url = 'https://education.vk.company/'

    def login(self, email, password):
        self.driver.maximize_window()
        self.click(self.locators.LOGIN_LINK, timeout=self.default_timeout)
        self.click(self.locators.LOGIN_WITH_CREDENTIALS_BUTTON, timeout=self.default_timeout)
        self.input(self.locators.EMAIL_INPUT, email, timeout=self.default_timeout)
        self.input(self.locators.PASSWORD_INPUT, password, timeout=self.default_timeout)
        self.click(self.locators.SUBMIT_BUTTON, timeout=self.default_timeout)
        return MainPage(self.driver)
