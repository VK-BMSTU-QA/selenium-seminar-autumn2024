import time

import allure
import pytest

from selenium.webdriver.common.keys import Keys

from ui.pages.login_page import LoginPage
from base import BaseCase
from ui.pages.person_page import PersonPage
from ui.pages.schedule_page import SchedulePage
from ui.pages.main_page import MainPage


class TestLogin(BaseCase):
    @pytest.fixture(autouse=True)
    def setup_login_page(self, driver):
        self.login_page = LoginPage(driver)

    @allure.title("Авторизация пользователя")
    def test_login(self, credentials):
        self.login_page.login(credentials["login"], credentials["password"])
        assert self.driver.current_url == MainPage.url, "Не удалось выполнить вход. Проверьте URL"


class TestLK(BaseCase):
    @allure.title("Поиск человека в личном кабинете и получение информации 'О себе'")
    def test_lk1(self, request, setup_cookies):
        self.person_page: PersonPage = (request.getfixturevalue('person_page'))
        people_button = self.person_page.find(self.person_page.locators.PEOPLE_BUTTON)
        people_button.click()
        search_field = self.person_page.find(self.person_page.locators.SEARCH_FIELD)
        search_field.send_keys("Александр Горбатов")
        search_field.send_keys(Keys.ENTER)
        person_block = self.person_page.find(self.person_page.locators.PERSON_BLOCK)
        person_block.click()
        about_info = self.person_page.find(self.person_page.locators.ABOUT_INFO)
        assert about_info.text == "Пользователь не заполнил раздел \"О себе\"", "Ожидаемое сообщение о пустом разделе не найдено"

    @allure.title("Просмотр аудитории занятия по QA 22.10.2024")
    def test_lk2(self, request, setup_cookies):
        self.schedule_page: SchedulePage = (request.getfixturevalue('schedule_page'))
        schedule_button = self.schedule_page.find(self.schedule_page.locators.SCHEDULE_BUTTON)
        schedule_button.click()
        time.sleep(2)
        semester_interval = self.schedule_page.find(self.schedule_page.locators.SEMESTER_INTERVAL)
        semester_interval.click()
        dropdown = self.schedule_page.find(self.schedule_page.locators.DROPDOWN)
        dropdown.click()
        my_groups_option = self.schedule_page.find(self.schedule_page.locators.MY_GROUPS_OPTION)
        my_groups_option.click()
        lesson_block = self.schedule_page.find(self.schedule_page.locators.LESSON_BLOCK)
        lesson_block.click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        class_info = self.schedule_page.find(self.schedule_page.locators.CLASS_INFO)
        assert class_info.text == "Аудитория ауд.395 - зал 3 (МГТУ) и Онлайн (ссылки пока нет)", "Аудитория занятия не совпадает с ожидаемой"
