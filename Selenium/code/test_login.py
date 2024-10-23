import pytest
from _pytest.fixtures import FixtureRequest

from base_vked import BaseCaseVkEd
from ui.pages.base_page import BasePage







class TestLogin(BaseCaseVkEd):


    authorize = True

    def test_login(self, credentials_vked):
        pass # assert встроен в login
'''
class TestLK(BaseCaseVkEd):

    def test_lk1(self):
        pass


    def test_lk2(self):
        pass

    def test_lk3(self):
        pass

'''

