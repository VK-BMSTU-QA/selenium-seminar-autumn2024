from selenium.webdriver.common.by import By


class LoginPageLocators:
    LOGIN_BUTTON = (By.XPATH, '//*[@class="AuthButton__SAuthLink-sc-1iwc4q0-0 fqBjCc gtm-auth-header-btn"]')
    LOGIN_BY_CREDENTIALS_BUTTON = (By.XPATH, '//button[@type="reset"]')
    EMAIL_INPUT = (By.ID, 'email')
    PASSWORD_INPUT = (By.ID, 'password')
    SUBMIT_BUTTON = (By.XPATH, '//button[@type="submit"]')

class MainPageLocators:
    QUERY_BUTTON = (By.XPATH, '//header[@id="header"]/ul[3]/li[2]/a/i')
    QUERY_INPUT = (By.NAME, 'query')
    PROFILE_LOCATOR = (By.XPATH, '//div[@id="react-search-root"]/div/div/div[2]/div/table/tbody/tr/td/div/a/p/span[2]/span/span')

    SCHEDULE_BUTTON = (By.LINK_TEXT, 'Расписание')
    CURRENT_LESSON_LOCATOR = (By.XPATH, '//table[@class="schedule-timetable"]/tbody/tr[1]/td[3]/a/strong')
    