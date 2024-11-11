from selenium.webdriver.common.by import By

class LoginPageLocators:
    GO_BUTTON_AUTHBUTTON_LOCATOR = (By.XPATH, '//a[contains(@class, "AuthButton")]')
    GO_BUTTON_TYPEAUTH_LOCATOR = (By.XPATH, '//button[contains(@class, "gtm-signup")]')
    LOGIN_INPUT_LOCATOR = (By.ID, 'email')
    PASSWORD_INPUT_LOCATOR = (By.ID, 'password')
    GO_BUTTON_LOGIN_LOCATOR = (By.XPATH, '//button[@type="submit"]')

class MainPageLocators:
    GO_BUTTON_OPENSEARCH_LOCATOR = (By.XPATH, '//li[@class="js-show-search"]')
    SEARCH_INPUT_LOCATOR = (By.CSS_SELECTOR, 'li.js-search-input input[name="query"]')
    FRIEND_LOCATOR = (By.XPATH, '//a[contains(@href, "user_188197")]')
    GO_BUTTON_PROGRAM_LOCATOR = (By.XPATH, '//a[@href="/curriculum/program/"]')
    GO_BUTTON_PROGRAM_TEST_LOCATOR = (By.XPATH, '//div[contains(text(), "Обеспечение качества")]')
    GO_BUTTON_LESSONS_LOCATOR = (By.XPATH, '//a[@class="js-toggle-lessons"]')
    GO_BUTTON_LESSON_LOCATOR = (By.XPATH, '//span[contains(text(), "End-to-End")]')