import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
#from webdriver_manager.chrome import ChromeDriverManager
import string
import random

#Fixture que crea instancia del chrome driver
@pytest.fixture()
def chrome_browser():
    driver = webdriver.Chrome()

    driver.implicitly_wait(10)
    #yield webdriver instance
    yield driver
    #close webdriver instance
    driver.quit()

#Fixture que crea instancia del firefox driver
@pytest.fixture()
def firefox_browser():
    driver = webdriver.Firefox()

    driver.implicitly_wait(10)

    yield driver

    driver.quit()

@pytest.fixture()

#Fixture que crea instancia del safari driver
def safari_browser():
    driver = webdriver.Safari()

    driver.implicitly_wait(10)

    yield driver

    driver.quit()

#Fixture para crear un nombre de usuario aleatorio nuevo, ideal para caso de signup
@pytest.fixture()
def generate_username():
    characters = string.ascii_letters + string.digits + '._-'
    username = ''.join(random.choice(characters) for _ in range(random.randint(5, 32)))
    return username

