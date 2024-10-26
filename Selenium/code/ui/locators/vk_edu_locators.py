from selenium.webdriver.common.by import By


class LoginPageLocators:
    AUTH_OR_REG_BUTTON = (By.CLASS_NAME, 'gtm-auth-header-btn')
    SIGN_UP_BUTTON = (By.CLASS_NAME, 'gtm-signup-modal-link')
    EMAIL_INPUT = (By.ID, 'email')
    PASSWORD_INPUT = (By.ID, 'password')
    LOGIN_BUTTON = (By.CLASS_NAME, 'gtm-login-btn')


class SchedulePageLocators:
    SCHEDULE_TWO_WEEKS_INTERVAL = (By.XPATH, '//*[@id="schedule-interval"]/li[1]/a')
    SCHEDULE_ALL_TIME_INTERVAL = (By.XPATH, '//*[@id="schedule-interval"]/li[2]/a')
    SUBJECTS_LIST = (By.XPATH, '//*[@id="react-schedule"]/div/div[1]/div/div/div[2]/div/div[2]')
    SUBJECT_LIST_ELEM = lambda subject: (By.XPATH, f'//*[contains(text(), "{subject}")]')
    SCHEDULE_TABLE = (By.XPATH, '//*[@id="react-schedule"]/div/div[2]/div[1]')
    ROWS = (By.CSS_SELECTOR, 'tr.schedule-timetable__item')
    ROW_DATE = (By.XPATH, './td[1]/p[1]/nobr/strong')
    ROW_EVENT = (By.XPATH, './td[3]/p/span[1]')
    ROW_LOCATION = (By.XPATH, './td[3]/p/span[2]')


class PeoplePageLocators:
    SEARCH_INPUT = (By.XPATH, '//*[@id="content"]/div/div[1]/form/input[1]')
    SEARCH_BUTTON = (By.XPATH, '//*[@id="content"]/div/div[1]/form/input[2]')
    ROWS = (By.CSS_SELECTOR, 'td.cell-name')
    ROW_NAME = (By.XPATH, './div/p[2]/a')
    ROW_DESCRIPTION = (By.XPATH, '//*[@class="user-desc"]')
