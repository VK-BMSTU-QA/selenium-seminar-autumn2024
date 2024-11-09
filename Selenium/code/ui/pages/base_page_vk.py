import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException, WebDriverException

class PageNotOpenedException(Exception):
    pass

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.url = getattr(self, 'url', None)
        if self.url:
            self.is_opened()

    def is_opened(self, timeout=15):
        try:
            WebDriverWait(self.driver, timeout).until(EC.url_contains(self.url))
            return True
        except TimeoutException:
            allure.attach(self.driver.get_screenshot_as_png(), name="is_opened_failed", attachment_type=allure.attachment_type.PNG)
            raise PageNotOpenedException(f"{self.url} did not open in {timeout} seconds")

    def wait(self, timeout=10):
        return WebDriverWait(self.driver, timeout=timeout)

    def find(self, locator, timeout=10):
        try:
            return self.wait(timeout).until(EC.presence_of_element_located(locator))
        except TimeoutException:
            allure.attach(self.driver.get_screenshot_as_png(), name=f"find_failed_{locator}", attachment_type=allure.attachment_type.PNG)
            raise TimeoutException(f"Element with locator {locator} was not found within {timeout} seconds")

    def click(self, locator, timeout=10):
        try:
            elem = self.wait(timeout).until(EC.element_to_be_clickable(locator))
            elem.click()
            return elem
        except (TimeoutException, WebDriverException) as e:
            allure.attach(self.driver.get_screenshot_as_png(), name=f"click_failed_{locator}", attachment_type=allure.attachment_type.PNG)
            raise WebDriverException(f"Error occurred while clicking on element with locator {locator}: {str(e)}")

    def input(self, locator, data):
        try:
            elem = self.find(locator)
            elem.send_keys(data)
        except NoSuchElementException as e:
            allure.attach(self.driver.get_screenshot_as_png(), name=f"input_failed_{locator}", attachment_type=allure.attachment_type.PNG)
            raise NoSuchElementException(f"Input field not found for locator {locator}: {str(e)}")
