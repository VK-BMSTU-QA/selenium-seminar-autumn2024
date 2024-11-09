import conftest
from ui.pages.base_page import BasePage
from selenium.webdriver.common.keys import Keys


class PeoplePage(BasePage):
    url = conftest.vk_url

    def search_name(self, name, last_name):
        search_input = self.find(self.locators.SEARCH_INPUT)
        search_input.send_keys(name + ' ' + last_name)
        search_input.send_keys(Keys.ENTER)

    def validate_search(self, name, last_name):
        found_name = self.find(self.locators.FOUND_NAME).text
        assert found_name == name, f"Ожидалось имя '{name}', но найдено '{found_name}'"
        found_last_name = self.find(self.locators.FOUND_LAST_NAME).text
        assert found_last_name == last_name, f"Ожидалась фамилия '{last_name}', но найдена '{found_last_name}'"
