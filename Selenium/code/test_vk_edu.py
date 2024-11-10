import json

import pytest
from _pytest.fixtures import FixtureRequest

from vk_edu_base import BaseCase
from ui.pages.base_page import BasePage

feed_url = "https://education.vk.company/feed/"


class TestLogin(BaseCase):
    authorize = True

    @pytest.mark.usefixtures("credentials")
    def test_login(self, credentials):
        self.login_page.login(credentials["email"], credentials["password"])

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
        lesson_data = self.main_page.get_lesson()

        assert "Обеспечение качества в разработке ПО" in lesson_data
        assert "End-to-End тесты на Python" in lesson_data
