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
    FRIEND_LOCATOR = (By.XPATH, '//a[contains(@href, "188197")]')
    SEARCH_BUTTON = (By.XPATH, '//button[@type="submit"]')
    SEARCH_RESULTS = (By.CLASS_NAME, 'results')
    SEMINAR_SEARCH_INPUT = (By.ID, 'seminar_search')
    SEMINAR_SEARCH_BUTTON = (By.XPATH, '//button[@type="submit"]')
    SEMINAR_RESULTS = (By.CLASS_NAME, 'seminar_results')
