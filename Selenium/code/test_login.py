import pytest
from _pytest.fixtures import FixtureRequest

from base import BaseCase


class TestLogin(BaseCase):
    authorize = False

    @pytest.mark.usefixtures('credentials')
    def test_login(self, credentials):
        self.base_page.login(credentials['EMAIL'], credentials['PASSWORD'])
        assert self.driver.current_url == 'https://education.vk.company/feed/'