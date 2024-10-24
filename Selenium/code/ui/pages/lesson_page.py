from ui.locators import lesson_locators
from ui.pages.base_page import BasePage


class LessonPage(BasePage):
    locators = lesson_locators.LessonPageLocators()

    def __init__(self, driver, url):
        self.driver = driver
        self.url = url
        self.is_opened()

    def get_audition(self):
        audition_info = self.find(self.locators.ROOM_INFO_LOCATOR)
        return audition_info.text
