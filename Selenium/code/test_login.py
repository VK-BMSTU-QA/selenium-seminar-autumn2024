from base import BaseCase


class TestLogin(BaseCase):
    authorize = False

    def test_login(self, request):
        credentials = request.getfixturevalue("credentials")
        self.login_page.login(*credentials)
        assert "Лента" in self.driver.title


class TestLK(BaseCase):
    authorize = True

    # def test_user_about_info(self):
    #     # Открываем страницу "Люди"
    #     self.people_page = self.main_page.go_to_people_page()
    #
    #     # Открываем страницу пользователя с фамилией "Михалёв"
    #     self.user_page = self.people_page.find_user("Михалёв")
    #     about = self.user_page.get_about()
    #     assert "Студент 4 курса ИУ5\nМладший фронтенд-разработчик в Облаке Mail" in about

    def test_audience(self):
        # Открываем страницу занятия 22 октября
        self.lesson_page = self.main_page.open_lesson("пн, 14 октября")

        # Проверяем аудиторию
        audition = self.lesson_page.get_audition()
        assert "Онлайн" in audition
