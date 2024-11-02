import urllib.parse

from conftest import Config
from ui.locators.vk_edu_locators import PeoplePageLocators
from ui.pages.base_page import BasePage


class PeoplePage(BasePage):
    url = Config.URL_VK_EDU_PEOPLE

    def search_people(self, name: str) -> list[tuple[str, str]]:
        self.find(PeoplePageLocators.SEARCH_INPUT).send_keys(name)
        self.click(PeoplePageLocators.SEARCH_BUTTON)
        # ждем, когда загрузится страница с результатами поиска
        self.wait().until(lambda d: d.current_url == f'{self.url}?{urllib.parse.urlencode({"q": name})}')
        result = []
        rows = self.driver.find_elements(*PeoplePageLocators.ROWS)
        for row in rows:
            result.append(
                (
                    row.find_element(*PeoplePageLocators.ROW_NAME).text.strip(),
                    row.find_element(*PeoplePageLocators.ROW_DESCRIPTION).text.strip()
                )
            )
        return result
