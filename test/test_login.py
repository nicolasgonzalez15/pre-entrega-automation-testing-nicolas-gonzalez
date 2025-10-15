import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException

# 🔹 Lista de usuarios y contraseñas a probar
@pytest.mark.parametrize("usuario,password", [
    ("standard_user", "secret_sauce"),
    ("locked_out_user", "secret_sauce"),
    ("problem_user", "secret_sauce"),
    ("performance_glitch_user", "secret_sauce"),
])
def test_login(usuario, password):
    """
    Prueba parametrizada para login en https://www.saucedemo.com/
    Valida que los usuarios con credenciales correctas entren al inventario
    y los bloqueados no.
    """

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

        # Verificamos si llegó al inventario (login exitoso)
        if "inventory" in driver.current_url:
            print(f"✅ Login exitoso con {usuario}")
            assert True
        else:
            print(f"❌ Login fallido con {usuario}")
            # Si aparece mensaje de error, lo imprimimos
            try:
                error = driver.find_element(By.CSS_SELECTOR, "[data-test='error']").text
                print(f"Mensaje de error: {error}")
            except:
                print("No se encontró mensaje de error.")
            assert "locked_out_user" in usuario  # el único que debe fallar

    except WebDriverException as e:
        pytest.fail(f"Error del WebDriver: {e}")

    finally:
        driver.quit()


# Login OK - Chrome como browser
def test_login_chrome(chrome_browser):
    #redirigo a página demoblaze
    chrome_browser.get("https://www.saucedemo.com/")

    #espero 3 segundos
    time.sleep(3)

    #completo login con datos existentes
    usuario = chrome_browser.find_element(By.ID,'user-name')
    usuario.send_keys('standard_user')

    clave = chrome_browser.find_element(By.ID,'password')
    clave.send_keys('secret_sauce')

    #espero 3 segundos
    time.sleep(3)

    #click en Login
    chrome_browser.find_element(By.ID,'login-button').click()

    #espero 3 segundos
    time.sleep(3)


# Login OK - Firefox
def test_login_firefox(firefox_browser):
    #redirigo a página demoblaze
    firefox_browser.get("https://www.saucedemo.com/")

    #espero 3 segundos
    time.sleep(3)

    #completo login con datos existentes
    usuario = firefox_browser.find_element(By.ID,'user-name')
    usuario.send_keys('standard_user')

    clave = firefox_browser.find_element(By.ID,'password')
    clave.send_keys('secret_sauce')

    #espero 3 segundos
    time.sleep(3)

    #click en Login
    firefox_browser.find_element(By.ID,'login-button').click()

    #espero 3 segundos
    time.sleep(3)

    sitio_web = firefox_browser.current_url
    assert sitio_web == "https://www.saucedemo.com/inventory.html"


# Login OK - Safari
def test_login_safari(safari_browser):
    #redirigo a página demoblaze
    safari_browser.get("https://www.saucedemo.com/")

    #espero 3 segundos
    time.sleep(3)

    #completo login con datos existentes
    usuario = safari_browser.find_element(By.ID,'user-name')
    usuario.send_keys('standard_user')

    clave = safari_browser.find_element(By.ID,'password')
    clave.send_keys('secret_sauce')

    #espero 3 segundos
    time.sleep(3)

    #click en Login
    safari_browser.find_element(By.ID,'login-button').click()

    #espero 3 segundos
    time.sleep(3)

    sitio_web = safari_browser.current_url
    assert sitio_web == "https://www.saucedemo.com/inventory.html"


