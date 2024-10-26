from selenium.webdriver.common.by import By


class LessonPageLocators:
    ROOM_INFO_LOCATOR = (By.XPATH, '//div[@class="lesson-right"]//div[@class="info"][3]//span[@class="info-pair-value"]')