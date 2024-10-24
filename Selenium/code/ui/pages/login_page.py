from ui.locators.login_locators import LoginPageLocators
from ui.pages.base_page import BasePage
from ui.pages.main_page import MainPage


class LoginPage(BasePage):
    url = "https://education.vk.company/"
    locators = LoginPageLocators()
    authorize = False

    def login(self, username, password):
        self.click(self.locators.NAVBAR_LOGIN_BTN_LOCATOR)
        self.click(self.locators.LOGIN_BY_CREDENTIALS_BTN_LOCATOR)
        login_input = self.find(self.locators.LOGIN_INPUT_LOCATOR)
        password_input = self.find(self.locators.PASSWORD_INPUT_LOCATOR)
        login_input.send_keys(username)
        password_input.send_keys(password)
        self.click(self.locators.LOGIN_SUBMIT_BTN_LOCATOR)

        return MainPage(self.driver)