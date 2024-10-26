import time
import allure
from selenium.webdriver.remote.webelement import WebElement
from ui.locators import basic_locators_vk
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class PageNotOpenedException(Exception):
    pass


class BasePage:
    locators = basic_locators_vk.AuthPageLocators
    locators_main = basic_locators_vk.DashboardPageLocators
    url = 'https://education.vk.company/'
    default_timeout = 5

    def __init__(self, driver):
        self.driver = driver
        self._ensure_page_opened()

    def _ensure_page_opened(self, timeout: int = 15) -> None:
        WebDriverWait(self.driver, timeout).until(
            lambda driver: driver.current_url == self.url,
            f"{self.url} did not open in {timeout} sec, current URL: {self.driver.current_url}"
        )

    def wait_until(self, condition, timeout: int = default_timeout) -> WebDriverWait:
        return WebDriverWait(self.driver, timeout).until(condition)

    def find(self, locator, timeout: int = default_timeout) -> WebElement:
        return self.wait_until(EC.presence_of_element_located(locator), timeout)

    def click(self, locator, timeout: int = default_timeout) -> None:
        self.wait_until(EC.element_to_be_clickable(locator), timeout).click()

    @allure.step("Performing search")
    def search(self, query: str) -> None:
        self.input(self.locators.QUERY_LOCATOR_ID, query)
        self.click(self.locators.GO_BUTTON_LOCATOR)
        self._assert_search()

    def input(self, locator, data: str) -> None:
        element = self.find(locator)
        element.clear()
        element.send_keys(data)

    @allure.step("Verifying search result")
    def _assert_search(self) -> None:
        assert 1 == 1, "Search verification placeholder"
