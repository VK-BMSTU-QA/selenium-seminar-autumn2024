import time

import pytest
from _pytest.fixtures import FixtureRequest

from base_vked import BaseCaseVkEd
from ui.pages.base_page import BasePage
from ui.locators.vked_locators import FeedPageLocators
import json






class TestLogin(BaseCaseVkEd):

    authorize = True

    def test_login(self, credentials_vked):
        pass  # assert встроен в login



class TestLK(BaseCaseVkEd):
    authorize = True

    def test_lk_find_user(self):
        with open('files/userdata.json', 'r') as f:
            userdata = json.load(f)
        name_to_find = userdata['name_to_find']
        surname_to_find = userdata['surname_to_find']
        field_enter = surname_to_find + " " + name_to_find

        self.login_page.click(FeedPageLocators.PEOPLE_BTN_LOC,10)
        self.login_page.enter_field_return(FeedPageLocators.SEARCH_FIELD_LOC, field_enter, 10)
        self.login_page.enter_field_return(FeedPageLocators.SEARCH_FIELD_LOC, field_enter, 10)
        self.login_page.check_text(FeedPageLocators.SPAN_NAME_LOC, name_to_find, 10)
        self.login_page.check_text(FeedPageLocators.SPAN_SURNAME_LOC, surname_to_find, 10)

    def test_find_seminar_info(self):
        with open('files/userdata.json', 'r') as f:
            userdata = json.load(f)
        sem_name = userdata['sem_name']
        sem_place = userdata['sem_place']
        sem_datetime = userdata['sem_datetime']

        self.login_page.click(FeedPageLocators.PROGRAM_BTN_LOC, 10)
        self.login_page.click(FeedPageLocators.COURSE_NAME_HREF_LOC, 10)
        self.login_page.click(FeedPageLocators.LESSONS_BTN_LOC, 10)
        self.login_page.check_text(FeedPageLocators.LESSON_NAME_FIELD_LOC, sem_name, 10)
        self.login_page.check_text(FeedPageLocators.DATETIME_FIELD_LOC, sem_datetime, 20)
        self.login_page.check_text(FeedPageLocators.VENUE_FIELD_LOC, sem_place, 20)
