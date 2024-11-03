from selenium.webdriver.common.by import By


class AuthPageLocators:
    REG_BTN_LOC = (By.XPATH, '//a[contains(@class, "AuthButton")]')
    GO_WITH_EMAIL_BTN_LOC = (By.CLASS_NAME, "bLqIKi")
    EMAIL_INP_LOC = (By.CLASS_NAME, "kbKfOy")
    PASSWORD_INP_LOC = (By.CLASS_NAME, "kLHUmL")
    SUBMIT_ENTER_BTN_LOC = (By.CLASS_NAME, 'gmKwFa')
    PROFILE_FIO_LOC = (By.CLASS_NAME, 'username')

class FeedPageLocators:
    PEOPLE_BTN_LOC = (By.XPATH, '//*[@id="header"]/ul[2]/li[6]/a') # кнопка ЛЮДИ наверху a href
    SEARCH_FIELD_LOC = (By.XPATH, '//*[@id="content"]/div/div[1]/form/input[1]') # input text строка поиска
    SPAN_SURNAME_LOC = (By.XPATH, '//*[@id="content"]/div/div[1]/div[2]/table/tbody/tr/td[1]/div/p[2]/a/span[2]')  # фамилия найденная
    SPAN_NAME_LOC = (By.XPATH, '//*[@id="content"]/div/div[1]/div[2]/table/tbody/tr/td[1]/div/p[2]/a/span[1]') # имя найденное

    PROGRAM_BTN_LOC = (By.XPATH, '//*[@id="header"]/ul[2]/li[2]/a')
    COURSE_NAME_HREF_LOC = (By.XPATH, '//*[@id="curriculum709"]/div[2]/div[2]/a[2]') # ссылка на инфу о курсе
    LESSONS_BTN_LOC = (By.XPATH, '//*[@id="content"]/div/div[1]/div/div[1]/ul/li[2]/a') # кнопка занятия
    LESSON_NAME_FIELD_LOC = (By.XPATH, '//*[@id="content"]/div/div[1]/div/div[3]/section/ul/li[8]/a/div[1]/div[2]/div[1]/span[2]') # название семинара
    DATETIME_FIELD_LOC = (By.XPATH, '//*[@id="content"]/div/div[1]/div/div[3]/section/ul/li[8]/a/div[1]/div[2]/div[2]/span[1]') # время проведения
    VENUE_FIELD_LOC = (By.XPATH, '//*[@id="content"]/div/div[1]/div/div[3]/section/ul/li[8]/a/div[1]/div[2]/div[2]/span[2]') # место проведения
