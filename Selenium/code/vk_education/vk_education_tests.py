import pytest

from vk_education_base import BaseCase

class TestLogin(BaseCase):
    authorize = False

    @pytest.mark.usefixtures('credentials')
    def test_login(self, credentials):
        self.landing_page.login(credentials['EMAIL'], credentials['PASSWORD'])
        assert self.driver.current_url == 'https://education.vk.company/feed/'


class TestLK(BaseCase):

    def test_lk_login(self):
        self.main_page.open_main()
        assert self.driver.current_url == 'https://education.vk.company/feed/'

    @pytest.mark.usefixtures('student_test_data')
    def test_lk_find_student(self, student_test_data):
        self.main_page.open_main()
        self.main_page.find_student(student_test_data['username'])
        assert self.driver.current_url == student_test_data['profile_link']

    def test_lk_find_current_lesson_info(self):
        current_window = self.driver.current_window_handle

        self.main_page.find_current_lesson_info()

        with self.switch_to_window(current=current_window, close=False):
            assert "https://education.vk.company/curriculum/program/lesson/" in self.driver.current_url