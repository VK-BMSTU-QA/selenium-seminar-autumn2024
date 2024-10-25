from selenium.webdriver.common.by import By


class VkPageLocators:
    LOGIN_BTN = (By.XPATH, '//*[@class="AuthButton__SAuthLink-sc-1iwc4q0-0 fqBjCc gtm-auth-header-btn"]')
    CONTINUE_WITH_EMAIL_BTN = (By.XPATH, '//*[@type="reset"]' )
    LOGIN_INPUT = (By.XPATH, '//form[@class="ModalAuth__SAuthForm-sc-1lc1krf-0 bvpFZW"]//input[@type="email"]')
    PASSWORD_INPUT = (By.XPATH, '//form[@class="ModalAuth__SAuthForm-sc-1lc1krf-0 bvpFZW"]//input[@type="password"]')
    CONFIRM_LOGIN_BTN = (By.XPATH, '//form[@class="ModalAuth__SAuthForm-sc-1lc1krf-0 bvpFZW"]//button[@type="submit"]')
    USER_INFO = (By.XPATH, '//div[@class="dropdown-user"]')

class MainVkPageLocators:
    PEOPLE_BTN = (By.XPATH, '//a[@href="/people/"]')
    GROUPS = (By.XPATH, '//select[contains(@class, "people-navigator-groups")]') 
    SEMESTERS = (By.XPATH, '//select[contains(@class, "people-navigator-semesters")]')
    SEARCH_BY_NAME = (By.XPATH, '//form[@class="search-form"]//input[@type="text"]')
    SEARCH_BY_NAME_BTN = (By.XPATH, '//form[@class="search-form"]//input[@type="submit"]')
    GO_TO_ACCOUNT = (By.XPATH, '//a[contains(@href, "https://education.vk.company/profile/")]') 
    SHEDULE_BTN = (By.XPATH, '//a[@href="/schedule/"]')
    SHOW_SEMESTER = (By.XPATH, '//li[@intervalid="semester"]') 
    CHOOSE_DISCIPLINE = (By.XPATH, '//div[contains(@class, "schedule-filters__item_discipline")]')
    CHOOSE_QA = (By.XPATH, '//*[contains(text(), "Обеспечение качества в разработке ПО")]')
    CHOOSE_LESSON = (By.XPATH, '//*[contains(text(), "End-to-End тесты на Python")]')