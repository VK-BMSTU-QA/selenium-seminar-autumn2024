import pytest
from selenium import webdriver


@pytest.fixture()
def driver(config):
    url = config['url']
    driver = webdriver.Chrome()
    driver.get(url)
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture()
def credentials():
    return ("TP_EMAIL", 'TP_PASSWORD')
