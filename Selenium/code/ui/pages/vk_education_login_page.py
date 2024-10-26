from ui.pages.base_page import BasePage
from ui.pages.vk_education_main_page import MainPage
from ui.locators.vk_education_locators import LoginPageLocators


class LoginPage(BasePage):

    locators = LoginPageLocators
    url = 'https://education.vk.company/'

    def login(self, user, password):
        self.driver.maximize_window()
        self.click(self.locators.LOGIN_BUTTON, timeout=10)
        self.click(self.locators.LOGIN_BY_CREDENTIALS_BUTTON, timeout=10)
        self.input(self.locators.EMAIL_INPUT, user, timeout=10)
        self.input(self.locators.PASSWORD_INPUT, password, timeout=10)
        self.click(self.locators.SUBMIT_BUTTON, timeout=10)
        
        return MainPage(self.driver)
    