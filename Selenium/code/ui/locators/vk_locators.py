from selenium.webdriver.common.by import By


class LoginPageLocators:
    AUTHBUTTON_LOCATOR = (By.XPATH, '//a[contains(@class, "gtm-auth-header-btn")]')
    AUTH_LOCATOR = (By.XPATH, '//button[contains(@class, "gtm-signup")]')
    LOGIN_LOCATOR = (By.ID, 'email')
    PASSWORD_LOCATOR = (By.ID, 'password')
    LOGIN_BUTTON_LOCATOR = (By.XPATH, '//button[@type="submit"]')


class MainPageLocators:
    OPENSEARCH_LOCATOR = (By.XPATH, '//li[@class="js-show-search"]')
    SEARCH_LOCATOR = (By.CSS_SELECTOR, 'li.js-search-input input[name="query"]')
    FRIEND_LOCATOR = (By.XPATH, '//a[contains(@href, "/profile/user_191238/")]')
    PROGRAM_LOCATOR = (By.XPATH, '//a[@href="/curriculum/program/"]')
    PROGRAM_TEST_LOCATOR = (By.XPATH, '//a[@href="/curriculum/program/discipline/2291/"]')
    LESSONS_LOCATOR = (By.XPATH, '//a[@class="js-toggle-lessons"]')
    LESSON_LOCATOR = (By.XPATH, '//a[contains(@href, "/curriculum/program/lesson/28796/")]')
    FRIEND_NAME_LOCATOR = (By.XPATH, '//div[@class="profile-username" and contains(text(),"Артём Черников")]')
    LESSON_NAME_LOCATOR = (By.XPATH, '//span[@class="lesson-title" and contains(text(),"End-to-End тесты на Python")]')
