import os

import allure

from base_vked import BaseCaseVkEd
from ui.locators.vked_locators import FeedPageLocators, AuthPageLocators


@allure.story("Авторизация и проверка профиля")
class TestLogin(BaseCaseVkEd):
    authorize = True

    @allure.title("Проверка авторизации")
    def test_login(self, credentials_vked):
        fio = self.login_page.get_text(AuthPageLocators.PROFILE_FIO_LOC, 10)
        assert fio == self.profile_fi, f"Ожидалось: '{self.profile_fi}', но было получено: '{fio}'"


@allure.story("Работа с личным кабинетом")
class TestLK(BaseCaseVkEd):
    authorize = True

    @allure.title("Поиск пользователя по имени и фамилии")
    def test_lk_find_user(self):
        name_to_find = os.getenv('name_to_find')
        surname_to_find = os.getenv('surname_to_find')
        field_enter = surname_to_find + " " + name_to_find

        self.login_page.click(FeedPageLocators.PEOPLE_BTN_LOC, 10)
        self.login_page.enter_field_return(FeedPageLocators.SEARCH_FIELD_LOC, field_enter, 10)
        got_name = self.login_page.get_text(FeedPageLocators.SPAN_NAME_LOC, 10)
        assert name_to_find == got_name, f"Ожидалось: '{name_to_find}', но было получено: '{got_name}'"

        got_surname = self.login_page.get_text(FeedPageLocators.SPAN_SURNAME_LOC, 10)
        assert surname_to_find == got_surname, f"Ожидалось: '{surname_to_find}', но было получено: '{got_surname}'"

    @allure.title("Поиск информации о семинаре")
    def test_find_seminar_info(self):
        sem_name = os.getenv('sem_name')
        sem_place = os.getenv('sem_place')
        sem_datetime = os.getenv('sem_datetime')

        self.login_page.click(FeedPageLocators.PROGRAM_BTN_LOC, 10)
        self.login_page.click(FeedPageLocators.COURSE_NAME_HREF_LOC, 10)
        self.login_page.click(FeedPageLocators.LESSONS_BTN_LOC, 10)
        got_sem_name = self.login_page.get_text(FeedPageLocators.LESSON_NAME_FIELD_LOC, 10)
        assert sem_name == got_sem_name, f"Ожидалось: '{sem_name}', но было получено: '{got_sem_name}'"

        got_sem_datetime = self.login_page.get_text(FeedPageLocators.DATETIME_FIELD_LOC, 20)
        assert sem_datetime == got_sem_datetime, f"Ожидалось: '{sem_datetime}', но было получено: '{got_sem_datetime}'"

        got_sem_place = self.login_page.get_text(FeedPageLocators.VENUE_FIELD_LOC, 20)
        assert sem_place == got_sem_place, f"Ожидалось: '{sem_place}', но было получено: '{got_sem_place}'"
