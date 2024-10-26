import pytest
import time
import os
from _pytest.fixtures import FixtureRequest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from ui.pages.base_page import BasePage


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
        "username": os.getenv("username"),
        "password": os.getenv("password")
    }


@pytest.fixture(scope='session')
def cookies(credentials, config):
        pass


class LoginPage(BasePage):
    url = 'https://education.vk.company/'

    def login(self, user, password):
        self.driver.get(self.url)

        button = WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, '//button[normalize-space()="вход / регистрация"]')))
        button.click()

        button = WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, '//button[normalize-space()="Продолжить с помощью почты и пароля"]')))
        button.click()

        email_input_box = WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located((By.ID, "email")))
        email_input_box.send_keys(user)

        email_input_box = WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located((By.ID, "password")))
        email_input_box.send_keys(password)

        button = WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, '//button[normalize-space()="Войти с паролем"]')))
        button.click()
        return MainPage(self.driver)


class MainPage(BasePage):
    url = 'https://education.vk.company/feed/'

    def click_people_icon(self):
        people_link = WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, "//li[contains(@class, 'technopark__menu__item_159')]//a")))
        people_link.click()

    def search_input(self, search_queries):
        search_input_box = WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located((By.NAME, "q")))
        search_input_box.send_keys(search_queries)

    def click_search_button(self):
        search_button = WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, '//input[@value="Найти"]')))
        search_button.click()

    def click_user(self):
        profile_link = WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, "//p[@class='realname']/a")))
        profile_link.click()

    def get_user_info(self):
        username = WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "profile-username"))).text
        about = WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH, "//div[@class='profile-about-text']"))).text
        birthday = WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH, "//div[contains(@class, 'profile-about-text')][2]"))).text

        return {
            "username": username,
            "about": about,
            "birthday": birthday
        }

    def click_program_icon(self):
        people_link = WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, "//li[contains(@class, 'technopark__menu__item_160')]//a")))
        people_link.click()

    def click_program(self):
        discipline_button = WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH,"//a[contains(@class, 'discipline-card') and contains(., '#2291: Обеспечение качества в разработке ПО')]")))
        discipline_button.click()

    def click_lesson(self):
        lessons_button = WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located((By.LINK_TEXT, 'Занятия')))
        lessons_button.click()

    def click_selected_lesson(self):
        lesson_link = WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located((By.PARTIAL_LINK_TEXT, 'End-to-End тесты на Python')))
        lesson_link.click()

    def get_lesson_info(self):
        date_info = WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH,"//div[contains(@class, 'info-pair')]/strong[text()='Дата проведения']/following-sibling::span"))).text
        location_info = WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH,"//div[contains(@class, 'info-pair')]/strong[text()='Место проведения']/following-sibling::span"))).text

        return {
            "date": date_info,
            "location": location_info
        }


class TestLogin(BaseCase):
    authorize = True

    def test_login(self, credentials):
        main_page = self.login_page.login(credentials["username"], credentials["password"])
        assert main_page.url == MainPage.url, "Login successful!"

class TestLK(BaseCase):
    def test_lk1(self, credentials):
        main_page = self.login_page.login(credentials['username'], credentials['password'])

        main_page.click_people_icon()

        main_page.search_input("Иван Карпов")

        main_page.click_search_button()

        main_page.click_user()

        user_info = main_page.get_user_info()

        assert "Учусь на СГН3-71Б 😎" in user_info["about"]
        assert "17 октября" in user_info["birthday"]

    def test_lk2(self, credentials):
        main_page = self.login_page.login(credentials['username'], credentials['password'])

        main_page.click_program_icon()

        main_page.click_program()

        main_page.click_lesson()

        main_page.click_selected_lesson()

        lesson_info = main_page.get_lesson_info()

        assert "22 октября 18:00 — 21:00 Мск" in lesson_info["date"]
        assert "Аудитория ауд.395 - зал 3 (МГТУ) и Онлайн (ссылки пока нет)" in lesson_info["location"]



    #def test_lk3(self):
    #    pass
