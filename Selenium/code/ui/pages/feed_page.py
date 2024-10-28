from conftest import Config
from ui.pages.base_page import BasePage


class FeedPage(BasePage):
    # По заданию первую страницу тестировать не нужно, так что этот класс используется только для получения url
    url = Config.URL_VK_EDU_FEED
