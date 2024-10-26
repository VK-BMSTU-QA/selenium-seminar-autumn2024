from selenium.webdriver.common.by import By


class BasePageLocators:
    QUERY_LOCATOR = (By.NAME, 'q')
    QUERY_LOCATOR_ID = (By.ID, 'id-search-field')
    GO_BUTTON_LOCATOR = (By.XPATH, '//*[@id="submit"]')
    START_SHELL = (By.ID, 'start-shell')
    PYTHON_CONSOLE = (By.ID, 'hterm:row-nodes')


class MainPageLocators(BasePageLocators):
    COMPREHENSIONS = (
        By.XPATH,
        '//code/span[@class="comment" and contains(text(), "comprehensions")]'
    )
    EVENTS = (By.ID, 'events')
    READ_MORE = (By.CSS_SELECTOR, 'a.readmore')

    SEARCH_PEOPLE_ICON = (By.XPATH, "//li[contains(@class, 'technopark__menu__item_159')]//a")
    SEARCH_INPUT = (By.NAME, "q")
    CLICK_SEARCH_BUTTON = (By.XPATH, '//input[@value="Найти"]')
    CLICK_USER = (By.XPATH, "//p[@class='realname']/a")
    PROFILE_ELEMENT = (By.CLASS_NAME, 'profile-about')
    GET_USER_INFO_ABOUT = [By.XPATH, ".//div[@class='profile-about-text'][1]"]
    GET_USER_INFO_BIRTHDAY = [By.XPATH, ".//div[contains(@class, 'profile-about-text')][2]"]
    CLICK_PROGRAM_ICON = (By.XPATH, "//li[contains(@class, 'technopark__menu__item_160')]//a")
    CLICK_PROGRAM = (By.XPATH,"//a[contains(@class, 'discipline-card') and contains(., '#2291: Обеспечение качества в разработке ПО')]")
    CLICK_LESSON = (By.LINK_TEXT, 'Занятия')
    CLICK_SELECTED_LESSON = (By.PARTIAL_LINK_TEXT, 'End-to-End тесты на Python')
    LESSON_TITLE = (By.CLASS_NAME, "lesson-title")
    GET_LESSON_DATE_INFO = (By.XPATH,"//div[contains(@class, 'info-pair')]/strong[text()='Дата проведения']/following-sibling::span")
    GET_LESSON_LOCATION_INFO = (By.XPATH,"//div[contains(@class, 'info-pair')]/strong[text()='Место проведения']/following-sibling::span")

class LoginPageLocators(BasePageLocators):
    LOGIN_BUTTON = (By.XPATH, '//button[normalize-space()="вход / регистрация"]')
    LOGIN_BUTTON_CHOOSE = (By.XPATH, '//button[normalize-space()="Продолжить с помощью почты и пароля"]')
    INPUT_USER = (By.ID, "email")
    INPUT_PASS = (By.ID, "password")
    LOGIN = (By.XPATH, '//button[normalize-space()="Войти с паролем"]')

class EventsPageLocators(BasePageLocators):
    pass
