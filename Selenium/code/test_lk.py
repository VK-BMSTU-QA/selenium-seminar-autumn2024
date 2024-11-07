import pytest
import time
import os
from _pytest.fixtures import FixtureRequest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from ui.pages.base_page import BasePage
from ui.locators import basic_locators as BC
import page

@pytest.fixture(scope='session')
def credentials():
    return {
        "username": os.getenv("username"),
        "password": os.getenv("password")
    }

@pytest.fixture(scope='session')
def cookies(credentials, config):
        pass

class TestLK(page.BaseCase):
    def test_lk1(self, credentials):
        main_page = self.login_page.login(credentials['username'], credentials['password'])

        main_page.click_people_icon()

        main_page.search_input("Иван Карпов")

        main_page.click_search_button()

        main_page.click_user()

        user_info = main_page.get_user_info()

        assert "Учусь на СГН3-71Б 😎" in user_info["about"], "About info is incorrect"
        assert "17 октября" in user_info["birthday"], "Birthday info is incorrect"

    def test_lk2(self, credentials):
        main_page = self.login_page.login(credentials['username'], credentials['password'])

        main_page.click_program_icon()

        main_page.select_program()

        main_page.select_lesson()

        main_page.click_selected_lesson()

        lesson_info = main_page.get_lesson_info()

        assert "22 октября 18:00 — 21:00 Мск" in lesson_info["date"], "Date info is incorrect"
        assert "Аудитория ауд.395 - зал 3 (МГТУ) и Онлайн (ссылки пока нет)" in lesson_info["location"], "Location info is incorrect"
