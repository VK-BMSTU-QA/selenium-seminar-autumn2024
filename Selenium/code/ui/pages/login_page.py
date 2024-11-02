from selenium.webdriver.support.wait import WebDriverWait
from ui.pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC


class LoginPage(BasePage):
    url = 'https://education.vk.company/'

    def login(self, user, password):
        login_button = self.find(self.locators.LOGIN_BUTTON)
        login_button.click()
        use_email_and_password_button = self.find(self.locators.USE_EMAIL_AND_PASSWORD_BUTTON)
        use_email_and_password_button.click()
        email_input = self.find(self.locators.EMAIL_INPUT)
        email_input.send_keys(user)
        password_input = self.find(self.locators.PASSWORD_INPUT)
        password_input.send_keys(password)
        submit_button = self.find(self.locators.SUBMIT_BUTTON)
        submit_button.click()

        WebDriverWait(self.driver, 15).until(
            EC.url_contains("/feed/")
        )
