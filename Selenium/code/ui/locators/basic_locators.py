from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_BUTTON = (By.XPATH, '//*[@class="AuthButton__SAuthLink-sc-1iwc4q0-0 fqBjCc gtm-auth-header-btn"]')
    LOGIN_WITH_EMAIL = (By.XPATH, '//*[@class="Button__SButton-sc-74bmbt-0 bLqIKi gtm-signup-modal-link"]')
    EMAIL_INPUT = (By.ID, 'email')
    PASSWORD_INPUT = (By.ID, 'password')
    SUBMIT_BUTTON = (By.XPATH, '//button[@type="submit"]')
    
class MainPageLocators:
    QUERY_BUTTON = (By.XPATH, '//li[@class="js-show-search"]')
    QUERY_INPUT = (By.NAME, 'query')
    PROFILE_NAME_LOCATOR = (By.XPATH, '//div[@class="people-list"]/table/tbody/tr/td/div/a/p/span[2]/span/span')

    SCHEDULE_LINK = (By.LINK_TEXT, 'Расписание')
    CURRENT_LESSON_LOCATOR = (By.XPATH, '//table[@class="schedule-timetable"]/tbody/tr[1]/td[3]/a/strong')


