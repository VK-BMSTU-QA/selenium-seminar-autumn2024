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

    SEARCH_ICON = (By.XPATH, "//li[contains(@class, 'js-show-search')]//a")
    SEARCH_INPUT = (By.XPATH, "//input[@name='query']")
    USER_NAME = lambda user_name: (By.XPATH, f"//p[contains(@class, 'realname')]/span[contains(text(), '{user_name}')]")
    ABOUT_SECTION = (By.XPATH, "//div[contains(@class, 'right-block profile-about')]")
    PROFILE_ABOUT_TEXT = lambda index: (By.XPATH, f".//div[contains(@class, 'profile-about-text')][{index}]")
    PROGRAM_MENU_ITEM = (By.XPATH, "//li[contains(@class, 'technopark__menu__item_160')]//a[contains(text(), 'Программа')]")
    DISCIPLINE_LINK = (By.XPATH, "//a[contains(@class, 'discipline-card') and contains(., '#2291: Обеспечение качества в разработке ПО')]")
    LESSONS_BUTTON = (By.XPATH, "//li[contains(@class, 'discipline-nav')]//a[contains(text(), 'Занятия')]")
    LESSON_LINK = lambda lesson_name: (By.XPATH, f"//a[contains(@class, 'lesson')]//span[contains(text(), '{lesson_name}')]")
    LESSON_TITLE = (By.CLASS_NAME, "lesson-title")
    LESSON_DATE = (By.XPATH, "//div[contains(@class, 'info-pair')]/strong[text()='Дата проведения']/following-sibling::span")
    LESSON_DESCRIPTION = (By.XPATH, "//div[contains(@class, 'section-text')][last()]/p")
    HOMEWORK_TITLE = (By.XPATH, "//div[contains(@class, 'homework')]//h2[contains(@class, 'title')]")
    HOMEWORK_DEADLINE = (By.XPATH, "//div[contains(@class, 'homework')]//span[contains(@class, 'status')]")


class EventsPageLocators(BasePageLocators):
    pass
