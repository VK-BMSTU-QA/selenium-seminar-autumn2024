import time
import conftest
from ui.pages.base_page import BasePage
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SchedulePage(BasePage):
    url = conftest.vk_url

    def find_room_in_schedule(self, date, room):
        # идем на страницу расписания
        self.click(self.locators.SCHEDULE_BUTTON)
        # считываем занятия 2х недель
        self.click(self.locators.WEEK_BUTTON)
        weeks_items = self.wait_for_elements(self.locators.SCHEDULE_ITEM, timeout=20) 
        # считываем занятия семестра 
        self.click(self.locators.SEMESTER_BUTTON)
        self.wait().until(
                lambda driver: len(driver.find_elements(*self.locators.SCHEDULE_ITEM)) != len(weeks_items)
            )
        semester_items = self.wait_for_elements(self.locators.SCHEDULE_ITEM, timeout=20)
        for item in semester_items:
            date_text = item.find_element(*self.locators.SCHEDULE_ITEM_DATE).text
            if date_text == date:
                room_text = item.find_element(*self.locators.SCHEDULE_ITEM_ROOM).text
                assert room_text == room, f"Ожидается '{room}', но найдено '{room_text}'"
                break
        else:
            assert False, f"Элемент с датой '{date}' не найден"
