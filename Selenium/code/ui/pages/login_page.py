from conftest import Config
from ui.locators.vk_edu_locators import LoginPageLocators
from ui.pages.base_page import BasePage


class LoginPage(BasePage):
    url = Config.URL_VK_EDU

    def login(self, user, password):
        self.click(LoginPageLocators.AUTH_OR_REG_BUTTON)
        self.click(LoginPageLocators.SIGN_UP_BUTTON)
        self.find(LoginPageLocators.EMAIL_INPUT).send_keys(user)
        self.find(LoginPageLocators.PASSWORD_INPUT).send_keys(password)
        self.click(LoginPageLocators.LOGIN_BUTTON)
        # ждем, когда загрузится следующая страница
        self.wait().until(lambda d: d.current_url != self.url and 'auth' not in d.current_url)
