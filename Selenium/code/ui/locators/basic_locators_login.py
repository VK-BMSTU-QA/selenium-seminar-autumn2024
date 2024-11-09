from selenium.webdriver.common.by import By


class BasePageLocators:
    OPEN_AUTH_MODAL_BUTTON = (By.XPATH, "//a[contains(@class, 'AuthButton')]")
    LOG_IN_WITH_CREDENTIALS_BUTTON = (
        By.XPATH, "//button[contains(@class, 'gtm-signup-modal-link')]")
    EMAIL_INPUT = (By.ID, 'email')
    PASSWORD_INPUT = (By.ID, 'password')
    LOG_IN_BUTTON = (
        By.XPATH, "//button[contains(@class, 'gtm-login-btn') and @type='submit']")
    USER_AGREEMENT_CHECK = (
        By.XPATH, "//div[contains(@class, 'CheckboxStyles') and @role='checkbox']")


class MainPageLocators:
    OPEN_SEARCH_BUTTON = (By.XPATH, "//li[contains(@class, 'js-show-search')]")
    SEARCH_BAR = (By.NAME, "query")
    SEARCH_FORM = (By.XPATH, "//form[@action='/search/']")
    SCHEDULE = (By.XPATH, "(//a[@href='/schedule/'])[1]")


class SchedulePageLocators:
    SEMESTER_SCHEDULE = (By.XPATH, "//li[@intervalid='semester']")
    DISCIPLINE_FILTER = (By.XPATH, "//div[contains(@class, 'schedule-filters__item_discipline')]")
    ALL_DISCIPLINES = (By.XPATH, "//div[contains(@class, 'active')]")


class LessonPageLocators:
    LESSON_HEADER = (By.XPATH, "//span[@class='lesson-title']")
