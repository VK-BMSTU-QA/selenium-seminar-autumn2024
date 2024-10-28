import time
from typing import Literal

from conftest import Config
from ui.locators.vk_edu_locators import SchedulePageLocators
from ui.pages.base_page import BasePage


class SchedulePage(BasePage):
    url = Config.URL_VK_EDU_SCHEDULE

    def select_interval(self, time_interval: Literal['all_time', 'two_weeks'] = 'all_time') -> None:
        if time_interval == 'two_weeks':
            self.click(SchedulePageLocators.SCHEDULE_TWO_WEEKS_INTERVAL)
        else:
            self.click(SchedulePageLocators.SCHEDULE_ALL_TIME_INTERVAL)

    def select_subject(self, subject: str = 'Обеспечение качества в разработке ПО') -> None:
        self.click(SchedulePageLocators.SUBJECTS_LIST_BUTTON)
        self.click(SchedulePageLocators.SUBJECT_LIST_ELEM(subject))

    @staticmethod
    def parse_row(row) -> dict:
        date = row.find_element(*SchedulePageLocators.ROW_DATE).text.strip()
        location = row.find_element(*SchedulePageLocators.ROW_LOCATION).text.strip()

        return {
            'date': date,
            'location': location,
        }

    def get_schedule(self) -> dict:
        # у элемента должен пропасть класс loading
        self.wait().until(lambda d: 'loading' not in d.find_element(*SchedulePageLocators.SCHEDULE_TABLE).get_attribute('class'))
        time.sleep(0.5)  # На отрисовку таблицы. Никаких других элементов для индикации загрузки нет, так что только time.sleep

        schedule = dict()
        rows = self.driver.find_elements(*SchedulePageLocators.ROWS)

        for row in rows:
            row_data = self.parse_row(row)
            schedule[row_data['date']] = row_data

        return schedule
