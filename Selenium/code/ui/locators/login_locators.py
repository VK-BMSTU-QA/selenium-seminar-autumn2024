from selenium.webdriver.common.by import By


class LoginPageLocators:
    NAVBAR_LOGIN_BTN_LOCATOR = (By.CSS_SELECTOR, '[class*="AuthButton__SAuthLink"]')
    LOGIN_BY_CREDENTIALS_BTN_LOCATOR = (By.CSS_SELECTOR, 'button[type="reset"]')
    LOGIN_INPUT_LOCATOR = (By.CSS_SELECTOR, '[name=email]')
    PASSWORD_INPUT_LOCATOR = (By.CSS_SELECTOR, '[name=password]')
    LOGIN_SUBMIT_BTN_LOCATOR = (By.CSS_SELECTOR, 'button[type=submit]')