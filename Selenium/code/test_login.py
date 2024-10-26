import pytest

from vk_education_base import BaseCase

class TestLogin(BaseCase):
    authorize = False

    @pytest.mark.usefixtures('credentials')
    def test_login(self, credentials):
        self.login_page.login(credentials['email'], credentials['password'])
        assert self.driver.current_url == 'https://education.vk.company/feed/'


class TestLK(BaseCase):

    def test_lk1_login(self):
        self.main_page.open_main()
        assert self.driver.current_url == 'https://education.vk.company/feed/'

    @pytest.mark.usefixtures('find_student_test_data')
    def test_lk2_find_student(self, find_student_test_data):
        self.main_page.open_main()
        self.main_page.find_student(find_student_test_data['username'])
        assert self.driver.current_url == find_student_test_data['profile_link']

    def test_lk3_find_current_lesson_info(self):
        current_window = self.driver.current_window_handle
        lesson_data = self.main_page.find_current_lesson_info()

        assert lesson_data != None

        with self.switch_to_window(current=current_window, close=False):
            assert "https://education.vk.company/curriculum/program/lesson/" in self.driver.current_url
