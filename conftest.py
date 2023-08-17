import pytest
import os
from datetime import datetime
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import ChromiumOptions


@pytest.fixture(autouse=True, scope='function')
def driver():
    # driver = webdriver.Chrome(ChromeDriverManager().install())
    # driver.maximize_window()
    # yield driver
    # driver.quit()
#-------------------------------------test-------------------------------------
    # chrome_options = ChromiumOptions()
    #
    # service = Service(ChromeDriverManager().install())
    #
    # driver = webdriver.Chrome(chrome_options=chrome_options, service=service)
    # driver.get("http://www.python.org")
    driver = webdriver.Chrome()
    # s = Service('driver/chromedriver')
    # driver = webdriver.Chrome(service=s)
    driver.maximize_window()
    yield driver
    driver.quit()
#--------------------------------------end test----------------------------------

# def pytest_configure(conf):
#     os.environ["REPORTING_RUN_DISPLAY_NAME"] = f"Rozetka_pytest - {datetime.now().date()}"
