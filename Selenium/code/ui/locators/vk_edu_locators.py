from selenium.webdriver.common.by import By


class LoginPageLocators:
    AUTH_OR_REG_BUTTON = (By.CLASS_NAME, 'gtm-auth-header-btn')
    SIGN_UP_BUTTON = (By.CLASS_NAME, 'gtm-signup-modal-link')
    EMAIL_INPUT = (By.ID, 'email')
    PASSWORD_INPUT = (By.ID, 'password')
    LOGIN_BUTTON = (By.CLASS_NAME, 'gtm-login-btn')


class SchedulePageLocators:
    SCHEDULE_TWO_WEEKS_INTERVAL = (By.XPATH, '//*[@intervalid="near"]')
    SCHEDULE_ALL_TIME_INTERVAL = (By.XPATH, '//*[@intervalid="semester"]')
    SUBJECTS_LIST_BUTTON = (By.CSS_SELECTOR, 'div.r-input')
    SUBJECT_LIST_ELEM = lambda subject: (By.XPATH, f'//*[contains(text(), "{subject}") and contains(@class, "option-label")]')
    SCHEDULE_TABLE = (By.CSS_SELECTOR, 'table.schedule-timetable')
    ROWS = (By.CSS_SELECTOR, 'tr.schedule-timetable__item')
    ROW_DATE = (By.TAG_NAME, 'strong')
    ROW_LOCATION = (By.CSS_SELECTOR, 'span.schedule-auditorium')


class PeoplePageLocators:
    SEARCH_INPUT = (By.XPATH, '//*[@name="q" and @class="input-text"]')
    SEARCH_BUTTON = (By.XPATH, '//*[@value="Найти" and @class="input-submit"]')
    ROWS = (By.CSS_SELECTOR, 'td.cell-name')
    ROW_NAME = (By.CSS_SELECTOR, 'p.realname')
    ROW_DESCRIPTION = (By.CSS_SELECTOR, 'p.user-desc')
