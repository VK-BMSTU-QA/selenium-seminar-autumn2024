from ui.locators import lesson_locators
from ui.pages.base_page import BasePage


class LessonPage(BasePage):
    check_url = False
    locators = lesson_locators.LessonPageLocators()

    def get_audition(self):
        audition_info = self.find(self.locators.ROOM_INFO_LOCATOR)
        return audition_info.text
