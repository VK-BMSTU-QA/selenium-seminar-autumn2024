from selenium.webdriver.common.by import By


class PeoplePageLocators:
    SEARCH_BAR = (By.CSS_SELECTOR, '.search-form .input-text')
    USER_LINK = (By.CSS_SELECTOR, ".realname a")