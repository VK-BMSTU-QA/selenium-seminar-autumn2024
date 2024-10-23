from selenium.webdriver.common.by import By


class AuthPageLocators:
    REG_BTN_LOC = (By.XPATH, '//a[contains(@class, "AuthButton")]')
    GO_WITH_EMAIL_BTN_LOC = (By.CLASS_NAME, "bLqIKi")
    EMAIL_INP_LOC = (By.CLASS_NAME, "kbKfOy")
    PASSWORD_INP_LOC = (By.CLASS_NAME, "kLHUmL")
    SUBMIT_ENTER_BTN_LOC = (By.CLASS_NAME, 'gmKwFa')
