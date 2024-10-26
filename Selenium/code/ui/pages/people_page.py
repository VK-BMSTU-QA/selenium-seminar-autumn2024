from selenium.webdriver import Keys

from ui.locators import people_locators
from ui.pages.base_page import BasePage
from ui.pages.user_page import UserPage


class PeoplePage(BasePage):
    url = "https://education.vk.company/people/"
    locators = people_locators.PeoplePageLocators()

    def find_user(self, username):
        search_people = self.find(self.locators.SEARCH_BAR)
        search_people.send_keys(username)
        search_people.send_keys(Keys.ENTER)
        link = self.find(self.locators.USER_LINK)
        href = link.get_attribute("href")
        link.click()
        assert self.driver.current_url == href
        return UserPage(self.driver)
