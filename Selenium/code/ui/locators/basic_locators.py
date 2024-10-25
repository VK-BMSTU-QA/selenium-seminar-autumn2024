from selenium.webdriver.common.by import By


class BasePageLocators:
    QUERY_LOCATOR = (By.NAME, 'q')
    QUERY_LOCATOR_ID = (By.ID, 'id-search-field')
    GO_BUTTON_LOCATOR = (By.XPATH, '//*[@id="submit"]')
    START_SHELL = (By.ID, 'start-shell')
    PYTHON_CONSOLE = (By.ID, 'hterm:row-nodes')


class MainPageLocators(BasePageLocators):
    PEOPLE_PAGE_LINK = (By.CSS_SELECTOR, "a[href*='/people/']")
    LESSONS_SLIDER_LEFT_BTN = (By.CSS_SELECTOR, "div[style*='left: 0px;']")

    def get_lesson_link(self, lesson_date):
        return (By.XPATH, f"//div[contains(text(), '{lesson_date}')]/following-sibling::a")
