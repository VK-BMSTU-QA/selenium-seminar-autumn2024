import os
import allure
import pytest
from dotenv import load_dotenv
from ui.locators import basic_locators, basic_urls
from _pytest.fixtures import FixtureRequest
from ui.pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BaseCase:
    authorize = True

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver, config, request: FixtureRequest):
        self.driver = driver
        self.config = config

        self.login_page = LoginPage(driver)
        if self.authorize:
            print('Do something for login')


@pytest.fixture(scope='session')
def credentials():
    load_dotenv()
    return {
        "username": os.getenv("username"),
        "password": os.getenv("password")
    }


class LoginPage(BasePage):
    url = basic_urls.START_URL
    locators = basic_locators.LoginPageLocators

    def login(self, user, password):
        self.driver.get(self.url)

        auth_button = self.find(self.locators.AUTH_BUTTON)
        auth_button.click()

        continue_button = self.find(self.locators.CONTINUE_BUTTON)
        continue_button.click()

        email_input = self.find(self.locators.EMAIL_INPUT)
        email_input.send_keys(user)

        password_input = self.find(self.locators.PASSWORD_INPUT)
        password_input.send_keys(password)

        login_button = self.find(self.locators.LOGIN_BUTTON)
        login_button.click()

        return MainPage(self.driver)


class MainPage(BasePage):
    url = basic_urls.FEED_URL
    locators = basic_locators.MainPageLocators

    @allure.step('Click Search Icon')
    def click_search_icon(self):
        self.click(self.locators.SEARCH_ICON)

    @allure.step('Enter Search Query')
    def enter_search_query(self, query):
        search_input = self.find(self.locators.SEARCH_INPUT)
        search_input.send_keys(query + Keys.ENTER)

    @allure.step('Click on User')
    def click_on_user(self, user_name):
        self.click(self.locators.USER_NAME(user_name))

    def get_user_info(self):
        about_section = self.find(self.locators.ABOUT_SECTION)
        about_text = about_section.find_element(*self.locators.PROFILE_ABOUT_TEXT(1)).text
        birthday_text = about_section.find_element(*self.locators.PROFILE_ABOUT_TEXT(2)).text
        return {"about": about_text, "birthday": birthday_text}

    @allure.step('Click Program')
    def click_program(self):
        self.click(self.locators.PROGRAM_MENU_ITEM)

    @allure.step('Click Discipline')
    def click_discipline(self):
        self.click(self.locators.DISCIPLINE_LINK)

    @allure.step('Click List Of Lessons')
    def click_list_of_lessons(self):
        self.click(self.locators.LESSONS_BUTTON)

    @allure.step('Click Lesson With Given Name')
    def click_lesson_with_given_name(self, lesson_name):
        self.click(self.locators.LESSON_LINK(lesson_name))

    def get_lesson_info(self):
        lesson_title = self.find(self.locators.LESSON_TITLE).text
        lesson_date = self.find(self.locators.LESSON_DATE).text
        lesson_description = self.find(self.locators.LESSON_DESCRIPTION).text
        homework_title = self.find(self.locators.HOMEWORK_TITLE).text
        homework_deadline = self.find(self.locators.HOMEWORK_DEADLINE).text
        return {
            "title": lesson_title,
            "date": lesson_date,
            "description": lesson_description,
            "hw_title": homework_title,
            "hw_deadline": homework_deadline
        }


class TestLogin(BaseCase):
    authorize = True

    def test_login(self, credentials):
        main_page = self.login_page.login(credentials['username'], credentials['password'])

        assert main_page.url == MainPage.url, "Не удалось войти!"


class TestMemberSearch(BaseCase):

    def test_member_search(self, credentials):
        main_page = self.login_page.login(credentials['username'], credentials['password'])

        main_page.click_search_icon()

        main_page.enter_search_query("Федасов")

        main_page.click_on_user("Сергей")

        user_info = main_page.get_user_info()

        assert self.driver.current_url == basic_urls.CHECK_USER_URL

        print("Информация о пользователе:")
        print("Обо мне:", user_info["about"])
        print("Дата рождения:", user_info["birthday"])

        assert "Пользователь не заполнил раздел \"О себе\"" in user_info["about"]
        assert "22 июля" in user_info["birthday"]


class TestLessonPage(BaseCase):

    def test_lesson_page(self, credentials):
        main_page = self.login_page.login(credentials['username'], credentials['password'])

        main_page.click_program()

        main_page.click_discipline()

        main_page.click_list_of_lessons()

        main_page.click_lesson_with_given_name("End-to-End тесты на Python")

        lesson_info = main_page.get_lesson_info()

        assert self.driver.current_url == basic_urls.CHECK_LESSON_URL

        print("Информация о занятии:")
        print("Тема:", lesson_info["title"])
        print("Дата:", lesson_info["date"])
        print("Описание:", lesson_info["description"])

        assert lesson_info['title'] == "End-to-End тесты на Python"
        assert lesson_info['date'] == "22 октября 18:00 — 21:00 Мск"
        assert "современные инструменты для тестирования веб-приложений" in lesson_info['description']
        assert "Домашнее задание 4" in lesson_info['hw_title']
        assert "Дедлайн 5 декабря в 18:00" in lesson_info['hw_deadline']
