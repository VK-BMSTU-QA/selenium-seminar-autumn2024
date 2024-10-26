from ui.locators.vkeducation_locators import LoginPageLocators
from ui.pages.base_page import BasePage
from ui.pages.vkeducation_mainpage import MainPage


class LoginPage(BasePage):
    locators = LoginPageLocators()

    def login(self, email, password):
        self.click(self.locators.LOGIN_BTN, timeout=5)
        self.click(self.locators.ENTER_BY_EMAIL_BTN, timeout=5)

        self.input(self.locators.EMAIL_INPUT, email, timeout=5)
        self.input(self.locators.PASSWORD_INPUT, password, timeout=5)

        self.click(self.locators.SUBMIT_BTN, timeout=5)

        return MainPage(self.driver)