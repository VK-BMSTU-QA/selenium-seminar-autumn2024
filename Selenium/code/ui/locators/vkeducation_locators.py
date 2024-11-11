from selenium.webdriver.common.by import By

class LoginPageLocators:
    LOGIN_BTN = (By.CLASS_NAME, "gtm-auth-header-btn")
    ENTER_BY_EMAIL_BTN = (By.CLASS_NAME, "gtm-signup-modal-link")
    EMAIL_INPUT = (By.CLASS_NAME, "kbKfOy")
    PASSWORD_INPUT = (By.CLASS_NAME, "kLHUmL")
    SUBMIT_BTN = (By.CLASS_NAME, "gtm-login-btn")

class MainPageLocators:
    PEOPLE_BNT = (By.LINK_TEXT, "Люди")
    SEARCH_FIELD = (By.NAME, "q")
    PROFILE_AVATAR = (By.CLASS_NAME, "avatar-wrapper")
    SCHEDULE_BTN = (By.LINK_TEXT, "Расписание")
    SHOW_FULL_SCHEDULE_BTN = (By.LINK_TEXT, "Весь семестр")
    CURRENT_LESSON_BTN = (By.XPATH, '//*[@id="schedule_item_1729544400"]/td[3]/a')
    LESSON_SUBJECT = (By.XPATH, '//*[@id="schedule_item_1729544400"]/td[3]/a/span')
