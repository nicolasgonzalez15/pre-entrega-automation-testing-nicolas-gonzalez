import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException


# 🔹 Lista de usuarios y contraseñas a probar
@pytest.mark.parametrize("usuario,password,mensaje_error", [
    ("", "","Epic sadface: Username is required"),
    ("standard_user", "","Epic sadface: Password is required"),
    ("", "secret_sauce","Epic sadface: Username is required"),
    ("xxxxx", "xxxx","Epic sadface: Username and password do not match any user in this service"),
])
def test_login_error(usuario, password,mensaje_error):

    # 🔧 Configuración del navegador
    options = Options()
    prefs = {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False
    }
    options.add_experimental_option("prefs", prefs)
    options.add_argument("--no-first-run")
    options.add_argument("--no-default-browser-check")

    driver = webdriver.Chrome(options=options)
    
    try:
        # Abrimos la web
        driver.get("https://www.saucedemo.com/")
        time.sleep(1)

        # Completamos login
        driver.find_element(By.ID, "user-name").send_keys(usuario)
        driver.find_element(By.ID, "password").send_keys(password)
        driver.find_element(By.ID, "login-button").click()
        time.sleep(1.5)  # pequeña espera para redirección

        error = driver.find_element(By.CSS_SELECTOR, "[data-test='error']").text
        assert error == mensaje_error
        #print(f"Mensaje de error: {error}")
    
    except:
        print("No se encontró mensaje de error.")


    finally:
        driver.quit()