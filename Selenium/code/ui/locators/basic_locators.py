from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_BUTTON = (By.XPATH, '//a[contains(text(), "вход / регистрация")]')
    USE_EMAIL_AND_PASSWORD_BUTTON = (By.XPATH, '//button[@type="reset" and contains(text(), "Продолжить с помощью почты и пароля")]')
    EMAIL_INPUT = (By.ID, 'email')
    PASSWORD_INPUT = (By.ID, 'password')
    SUBMIT_BUTTON = (By.XPATH, '//button[@type="submit" and contains(text(), "Войти с паролем")]')


class MainPageLocators(BasePageLocators):
    SEARCH_BUTTON = (By.CSS_SELECTOR, 'li.js-show-search')
    SEARCH_FIELD = (By.XPATH, '//input[@placeholder="Поиск..."]')
    PERSON_BLOCK = (By.XPATH, '//a[@href="https://education.vk.company/profile/user_149167/"]')
    SCHEDULE_BUTTON = (By.XPATH, '//a[@href="/schedule/"]')
    SEMESTER_INTERVAL = (By.XPATH, '//li[@intervalid="semester"]')
    LESSON_BLOCK = (By.XPATH, '//a[@class="schedule-show-info" and contains(strong, "End-to-End тесты на Python")]')
    ABOUT_INFO = (By.CSS_SELECTOR, '.profile-about-text')
    CLASS_INFO = (By.XPATH, '//div[@class="lesson-right"]//div[@class="info"][3]//span[@class="info-pair-value"]')
    MY_GROUPS_OPTION = (By.XPATH, '//div/span[contains(text(), "Мои группы")]')
    DROPDOWN = (By.CSS_SELECTOR, 'div.schedule-filters__item_group .r-input.r-input-flex')

class EventsPageLocators(BasePageLocators):
    pass
