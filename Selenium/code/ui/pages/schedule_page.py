from ui.locators import basic_locators
from ui.pages.base_page import BasePage


class SchedulePage(BasePage):
    locators = basic_locators.SchedulePageLocators()
    url = 'https://education.vk.company/schedule/'
