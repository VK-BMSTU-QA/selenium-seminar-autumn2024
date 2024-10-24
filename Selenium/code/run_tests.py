from base import BaseCase


class TestLogin(BaseCase):
    def test_login(self, request):
        credentials = request.getfixturevalue("credentials")
        self.login_page.login(*credentials)
        assert "Лента" in self.driver.title


class TestUserInfo(BaseCase):
    def test_user_about_info(self, request):
        credentials = request.getfixturevalue("credentials")
        self.main_page = self.login_page.login(*credentials)

        # Открываем страницу "Люди"
        self.people_page = self.main_page.go_to_people_page()

        # Открываем страницу пользователя с фамилией "Михалёв"
        self.user_page = self.people_page.find_user("Михалёв")
        about = self.user_page.get_about()
        assert "Студент 4 курса ИУ5\nМладший фронтенд-разработчик в Облаке Mail" in about


class TestAudience(BaseCase):
    def test_audience(self, request):
        credentials = request.getfixturevalue("credentials")
        self.main_page = self.login_page.login(*credentials)

        # Открываем страницу занятия 22 октября
        self.lesson_page = self.main_page.open_lesson("вт, 22 октября")

        # Проверяем аудиторию
        audition = self.lesson_page.get_audition()
        assert "Аудитория ауд.395" in audition
