import pytest
from selenium import webdriver


@pytest.fixture(autouse=True, scope='function')
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()
