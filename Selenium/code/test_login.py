import os
import time
import pytest
from dotenv import load_dotenv
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
    return {
        "username": os.getenv("USERNAME"),
        "password": os.getenv("PASSWORD")
    }


@pytest.fixture(scope='session')
def cookies(credentials, config):
    pass


class LoginPage(BasePage):
    url = 'https://education.vk.company/'

    def login(self, user, password):
        self.driver.get(self.url)

        auth_button = self.driver.find_element(By.XPATH, "//button/a[contains(text(), 'вход / регистрация')]")
        auth_button.click()

        continue_button = self.driver.find_element(By.XPATH, "//button[contains(text(), 'Продолжить с помощью почты и пароля')]")
        continue_button.click()

        email_input = self.driver.find_element(By.ID, "email")
        email_input.send_keys(user)

        password_input = self.driver.find_element(By.ID, "password")
        password_input.send_keys(password)

        login_button = self.driver.find_element(By.XPATH, "//button[contains(text(), 'Войти с паролем')]")
        login_button.click()

        return MainPage(self.driver)


class MainPage(BasePage):
    url = 'https://education.vk.company/feed/'

    def click_search_icon(self):
        search_icon = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH,
                                        "//li[contains(@class, 'js-show-search')]//a"))
        )
        search_icon.click()

    def enter_search_query(self, query):
        search_input = self.driver.find_element(By.XPATH, "//input[@name='query']")
        search_input.send_keys(query)
        search_input.send_keys(Keys.ENTER)

    def click_on_user(self, user_name):
        user_element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH,
                                        f"//p[contains(@class, 'realname')]/span[contains(text(), '{user_name}')]"))
        )
        user_element.click()

    def get_user_info(self):
        about_section = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH,
                                            "//div[contains(@class, 'right-block profile-about')]"))
        )

        about_text = about_section.find_element(By.XPATH, ".//div[contains(@class, 'profile-about-text')][1]").text
        birthday_text = about_section.find_element(By.XPATH, ".//div[contains(@class, 'profile-about-text')][2]").text

        return {
            "about": about_text,
            "birthday": birthday_text
        }

    def click_program(self):
        program_menu_item = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH,
                                        "//li[contains(@class, 'technopark__menu__item') and contains(@class, 'technopark__menu__item_160')]//a[contains(text(), 'Программа')]"))
        )
        program_menu_item.click()

    def click_discipline(self):
        discipline_link = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH,
                                        "//a[contains(@class, 'discipline-card') and contains(., '#2291: Обеспечение качества в разработке ПО')]"))
        )
        discipline_link.click()

    def click_lessons(self):
        lessons_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, "//li[contains(@class, 'discipline-nav')]//a[contains(text(), 'Занятия')]"))
        )
        lessons_button.click()

    def click_lesson(self, lesson_name):
        lesson_link = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, f"//a[contains(@class, 'lesson')]//span[contains(text(), '{lesson_name}')]"))
        )
        lesson_link.click()

    def extract_lesson_info(self):
        lesson_title = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "lesson-title"))
        ).text

        lesson_date = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH,
                                            "//div[contains(@class, 'info-pair')]/strong[text()='Дата проведения']/following-sibling::span"))
        ).text

        lesson_description = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.XPATH,
                                              "//div[contains(@class, 'section-text')][last()]/p"))
        ).text

        homework_description = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH,
                                            "//div[contains(@class, 'homework')]//h2[contains(@class, 'title')]"))
        ).text

        homework_deadline = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH,
                                            "//div[contains(@class, 'homework')]//span[contains(@class, 'status')]"))
        ).text

        return {
            "title": lesson_title,
            "date": lesson_date,
            "description": lesson_description,
            "homework": {
                "title": homework_description,
                "deadline": homework_deadline
            }
        }


class TestLogin(BaseCase):
    authorize = True

    def test_login(self, credentials):
        main_page = self.login_page.login(credentials['username'], credentials['password'])

        assert main_page.url == MainPage.url, "Login was not successful!"


class TestLK(BaseCase):

    def test_lk1(self, credentials):
        main_page = self.login_page.login(credentials['username'], credentials['password'])

        main_page.click_search_icon()

        main_page.enter_search_query("Федасов")

        main_page.click_on_user("Сергей")

        user_info = main_page.get_user_info()

        print("Информация о пользователе:")
        print("Обо мне:", user_info["about"])
        print("Дата рождения:", user_info["birthday"])

        assert "Пользователь не заполнил раздел \"О себе\"" in user_info["about"]
        assert "22 июля" in user_info["birthday"]

    def test_lk2(self, credentials):
        main_page = self.login_page.login(credentials['username'], credentials['password'])

        main_page.click_program()

        main_page.click_discipline()

        main_page.click_lessons()

        main_page.click_lesson("End-to-End тесты на Python")

        lesson_info = main_page.extract_lesson_info()

        assert lesson_info['title'] == "End-to-End тесты на Python"
        assert lesson_info['date'] == "22 октября 18:00 — 21:00 Мск"
        assert "современные инструменты для тестирования веб-приложений" in lesson_info['description']
        assert "Домашнее задание 4" in lesson_info['homework']['title']
        assert "Дедлайн 5 декабря в 18:00" in lesson_info['homework']['deadline']