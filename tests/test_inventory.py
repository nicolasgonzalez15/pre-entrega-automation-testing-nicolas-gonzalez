import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

# 1) Test de inventory, con al menos 1 producto para desplegar - webdriver Chrome
def test_inventory(login_driver):
    try:
        driver = login_driver
        assert driver.title == "Swag Labs"

        products = driver.find_elements(By.CLASS_NAME,'inventory_item')
        assert len(products)>0, "No hay productos visibles en la página"
    
    except Exception as e:
        print(f"Error en  test_inventory: {e}")
        raise

    finally:
        driver.quit()


# 2) Mostrar hamburger menu visible
def test_validar_menu_hamburger(login_driver):
    driver = login_driver #Importo driver de Chrome con Login válido

    # Valido que el menú hamburger sea visible luego del click
    driver.find_element(By.ID,'react-burger-menu-btn').click() #Click en menu hamburger
    time.sleep(3) # Espero 3 segundos
    assert driver.find_element(By.CLASS_NAME,'bm-item-list').is_displayed() == True #Verifico que el menú sea visible

# 3) Mostrar hamburger menu visible


def test_validar_datos_primer_producto(login_driver):
    driver = login_driver #Importo test de login OK

    productos = driver.find_elements(By.CLASS_NAME,'inventory_item') #Productos con filtros default
    primer_producto = productos[0]

    time.sleep(3)

    titulo = primer_producto.find_element(By.CLASS_NAME,'inventory_item_name')
    assert titulo.text == 'Sauce Labs Backpack'

    descripcion = primer_producto.find_element(By.CLASS_NAME,'inventory_item_desc')
    assert descripcion.text == 'carry.allTheThings() with the sleek, streamlined Sly Pack that melds uncompromising style with unequaled laptop and tablet protection.'

    precio = primer_producto.find_element(By.CLASS_NAME,'inventory_item_price')
    assert precio.text == '$29.99'

    imagen = primer_producto.find_element(By.CLASS_NAME,'inventory_item_img')
    assert imagen.is_displayed() == True
