from selenium.webdriver.common.by import By

from ui.locators import basic_locators
from ui.pages.base_page import BasePage
from ui.pages.lesson_page import LessonPage
from ui.pages.people_page import PeoplePage


class MainPage(BasePage):
    url = "https://education.vk.company/feed/"
    locators = basic_locators.MainPageLocators()

    def go_to_people_page(self):
        self.click(self.locators.ABOUT_PAGE_LINK)
        return PeoplePage(self.driver)

    def open_lesson(self, date):
        self.click(self.locators.LESSONS_SLIDER_LEFT_BTN)
        selector = f"//div[contains(text(), '{date}')]/following-sibling::a"
        link = self.find((By.XPATH, selector))
        lesson_url = link.get_attribute("href")
        link.click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        return LessonPage(self.driver, lesson_url)
