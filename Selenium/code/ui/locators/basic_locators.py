from selenium.webdriver.common.by import By


class BasePageLocators:
    QUERY_LOCATOR = (By.NAME, 'q')
    QUERY_LOCATOR_ID = (By.ID, 'id-search-field')
    GO_BUTTON_LOCATOR = (By.XPATH, '//*[@id="submit"]')
    START_SHELL = (By.ID, 'start-shell')
    PYTHON_CONSOLE = (By.ID, 'hterm:row-nodes')
    LOGIN_BUTTON = (By.XPATH, '//a[contains(text(), "вход / регистрация")]')
    USE_EMAIL_AND_PASSWORD_BUTTON = (By.XPATH, '//button[@type="reset" and contains(text(), "Продолжить с помощью почты и пароля")]')
    EMAIL_INPUT = (By.ID, 'email')
    PASSWORD_INPUT = (By.ID, 'password')
    SUBMIT_BUTTON = (By.XPATH, '//button[@type="submit" and contains(text(), "Войти с паролем")]')
    SEARCH_BUTTON = (By.CSS_SELECTOR, 'li.js-show-search')
    SEARCH_FIELD = (By.XPATH, '//input[@placeholder="Поиск..."]')



class MainPageLocators(BasePageLocators):
    COMPREHENSIONS = (
        By.XPATH,
        '//code/span[@class="comment" and contains(text(), "comprehensions")]'
    )
    EVENTS = (By.ID, 'events')
    READ_MORE = (By.CSS_SELECTOR, 'a.readmore')


class EventsPageLocators(BasePageLocators):
    pass
