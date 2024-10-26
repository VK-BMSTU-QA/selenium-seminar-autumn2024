import  os
from base_vkeducation import BaseCase
from ui.pages.base_page import BasePage
import pytest
from _pytest.fixtures import FixtureRequest
from dotenv import load_dotenv

feed_url = "https://education.vk.company/feed/"

load_dotenv()

@pytest.fixture(scope="session")
def login_and_password():
    email = os.getenv("EMAIL")
    password = os.getenv("PASSWORD")
    login_and_password_dict = {'email': email, 'password': password}

    return login_and_password_dict


@pytest.fixture(scope='session')
def student_data():
    name = os.getenv("NAME")
    surname = os.getenv("SURNAME")
    fullname = name + ' ' + surname
    student_url = os.getenv("URL")
    student_data_dict = {'name': fullname, 'url': student_url}

    return student_data_dict

class TestLogin(BaseCase):
    authorize = True

    @pytest.mark.usefixtures("login_and_password")
    def test_login(self, login_and_password):
        self.login_page.login(login_and_password["email"], login_and_password["password"])

        assert self.driver.current_url == feed_url


class TestLK(BaseCase):

    def test_feed_page(self):
        self.main_page.open()

        assert self.driver.current_url == feed_url


    @pytest.mark.usefixtures("student_data")
    def test_get_student(self, student_data):
        self.main_page.get_student(student_data["name"])

        assert self.driver.current_url == student_data["url"]

    def test_get_lesson(self):
        self.main_page.get_lesson()