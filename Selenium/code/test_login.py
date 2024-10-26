import time

import pytest
from _pytest.fixtures import FixtureRequest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from ui.pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC

class BaseCase:
    authorize = True

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver, config, request: FixtureRequest):
        self.driver = driver
        self.config = config

        self.login_page = LoginPage(driver)


@pytest.fixture(scope='session')
def credentials():
    return {
        'user': '', # сюда данные для успешной работы тестов
        'password': ''
    }


@pytest.fixture(scope='session')
def cookies(credentials, config):
        pass


class LoginPage(BasePage):
    url = 'https://education.vk.company/'

    def login(self, credentials):
        self.driver.maximize_window()
        auth_botton = self.driver.find_element(By.XPATH, "//a[text()='вход / регистрация']")
        auth_botton.click()
        time.sleep(3)
        continue_without_VK = self.driver.find_element(By.XPATH,
                                                       "//button[text()='Продолжить с помощью почты и пароля']")
        continue_without_VK.click()
        time.sleep(3)
        email = self.driver.find_element(By.ID, "email")
        password = self.driver.find_element(By.ID, "password")
        user_input = credentials.get('user', '')
        password_input = credentials.get('password', '')
        email.send_keys(user_input)
        password.send_keys(password_input)
        submit_botton = self.driver.find_element(By.XPATH, "//button[text()='Войти с паролем']")
        submit_botton.click()
        time.sleep(5)


class MainPage(BasePage):
    url = 'https://education.vk.company/feed/'


class TestLogin(BaseCase):
    authorize = True

    def test_login(self, credentials):
        pass


class TestLK(BaseCase):

    def test_login(self, credentials):
        login_page = LoginPage(self.driver)
        login_page.login(credentials)

    def test_friend(self, credentials):
        login_page = LoginPage(self.driver)
        login_page.login(credentials)

        profile = self.driver.find_element(By.XPATH, "//a[@class='full_name']")
        href_profile = profile.get_attribute('href')
        self.driver.get(href_profile)

        friends = self.driver.find_element(By.XPATH, "//a[text()='Друзья']")
        href_friends = friends.get_attribute('href')
        self.driver.get(href_friends)

        friend = self.driver.find_elements(By.XPATH, "(//div[contains(@class, 'friends_item')])")[0]
        username_element = friend.find_element(By.XPATH, ".//p[@class='username']/a")
        username = username_element.text  # Искомый юзернейм
        print("\nusername: " + username)
        time.sleep(5)

    def test_lesson(self, credentials):
        login_page = LoginPage(self.driver)
        login_page.login(credentials)

        self.driver.get("https://education.vk.company/schedule/")

        semestr = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'li[intervalid="semester"]'))
        )

        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'li[intervalid="semester"]'))
        )

        time.sleep(1)

        self.driver.execute_script("arguments[0].click();", semestr)

        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'tr#schedule_item_1729544400 a.schedule-show-info'))
        )

        href_leson = element.get_attribute('href')

        self.driver.get(href_leson)
        time.sleep(5)

        description = self.driver.find_element(By.XPATH, "//div[@class='description']")
        text_description = description.find_elements(By.XPATH, "//div[@class='section-text text']")[1]
        print("\nlesson description: " + text_description.text)

