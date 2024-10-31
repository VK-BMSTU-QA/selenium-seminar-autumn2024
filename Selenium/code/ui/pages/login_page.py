import conftest
from ui.pages.base_page import BasePage


class LoginPage(BasePage):
    url = conftest.vk_url

    
    def login(self, email, password):
        self.click(self.locators.AUTH_HEADER_BUTTON)
        self.click(self.locators.SIGNUP_MODAL_LINK)
        self.input(self.locators.EMAIL_INPUT, email)
        self.input(self.locators.PASSWORD_INPUT, password)
        self.click(self.locators.LOGIN_BUTTON)


