from ui.locators import basic_locators
from ui.pages.base_page import BasePage


class PersonPage(BasePage):
    locators = basic_locators.PersonPageLocators()
    url = 'https://education.vk.company/people/'
