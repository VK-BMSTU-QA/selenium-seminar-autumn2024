from selenium.webdriver.common.by import By


class MainPageLocators:
    SEARCH_BTN = (By.CLASS_NAME, "fa-search")
    SEARCH_FIELD = (By.NAME, "query")
    PROFILE_AVATAR = (By.CLASS_NAME, "avatar-wrapper")

    SCHEDULE_BTN = (By.LINK_TEXT, "Расписание")
    SHOW_FULL_SCHEDULE_BTN = (By.LINK_TEXT, "Весь семестр")
    CURRENT_LESSON_BTN = (By.XPATH, '//*[@id="schedule_item_1729544400"]/td[3]/a')
    LESSON_SUBJECT = (By.XPATH, '//*[@id="schedule_item_1729544400"]/td[3]/a/span')


class LoginPageLocators:
    LOGIN_BTN = (By.CLASS_NAME, "gtm-auth-header-btn")
    ENTER_BY_EMAIL_BTN = (By.CLASS_NAME, "gtm-signup-modal-link")
    EMAIL_INPUT = (By.ID, "email")
    PASSWORD_INPUT = (By.ID, "password")
    SUBMIT_BTN = (By.XPATH, "//button[@type='submit']")
