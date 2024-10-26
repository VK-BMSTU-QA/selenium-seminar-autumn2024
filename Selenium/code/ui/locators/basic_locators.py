from selenium.webdriver.common.by import By

class AuthPageLocators:
    GO_BUTTON_AUTHBUTTON_LOCATOR = (By.XPATH, '//a[contains(@class, "AuthButton")]')
    AUTH_BUTTON_LOC = (By.XPATH, '//a[contains(@class, "AuthButton")]')
    EMAIL_FIELD_LOC = (By.ID, 'email')
    PASSWORD_FIELD_LOC = (By.ID, 'password')
    SUBMIT_BUTTON_LOC = (By.XPATH, '//button[@type="submit"]')

class DashboardPageLocators:
    AUTH_TYPE_BUTTON_LOC = (By.XPATH, '//button[contains(@class, "gtm-signup")]')
    OPEN_SEARCH_BUTTON_LOC = (By.XPATH, '//li[contains(@class, "js-show-search")]')
    SEARCH_FIELD_LOC = (By.CSS_SELECTOR, 'li.js-search-input input[name="query"]')
    FRIEND_LINK_LOC = (By.XPATH, '//a[contains(@href, "188197")]')
    PROGRAM_LINK_LOC = (By.XPATH, '//a[@href="/curriculum/program/"]')
    PROGRAM_TEST_LINK_LOC = (By.XPATH, '//a[@href="/curriculum/program/discipline/2291/"]')
    TOGGLE_LESSONS_BUTTON_LOC = (By.XPATH, '//a[@class="js-toggle-lessons"]')
    LESSON_LINK_LOC = (By.XPATH, '//a[contains(@href, "28796")]')
