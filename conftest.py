import pytest
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
#from webdriver_manager.chrome import ChromeDriverManager
import string
import random
from utils import login


# Driver de chrome por default - instanciar Login
@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    #yield webdriver instance
    yield driver  # Todo se ejecuta luego del yield
    #close webdriver instance
    driver.quit()


# Driver de chrome por default con options
@pytest.fixture()
def driver_options():
    # Configuración del navegador - driver
    options = Options()
    prefs = {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False
    }
    options.add_experimental_option("prefs", prefs)
    options.add_argument("--no-first-run")
    options.add_argument("--no-default-browser-check")

    # Iniciar el driver de Chrome
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)
    
    yield driver  # Proveer el driver a los tests

    driver.quit()  # Cerrar el driver al final del test


# Fixture para crear Login automatizado
@pytest.fixture()
def login_driver(driver):
    login(driver)
    return driver


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

#Fixture que crea instancia del safari driver
@pytest.fixture()
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