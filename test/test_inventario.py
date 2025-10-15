import pytest
import time
from test_login import test_login_chrome
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

def test_titulo_valido_chrome(chrome_browser):
    test_login_chrome(chrome_browser) #Importo test de login OK

    #Valido titulo de sección Products
    titulo_products = chrome_browser.find_element(By.CSS_SELECTOR,'div.header_secondary_container .title').text
    assert titulo_products == "Products"

def test_existe_al_menos_un_producto_chrome(chrome_browser):
    test_login_chrome(chrome_browser) #Importo test de login OK

    productos = chrome_browser.find_elements(By.CLASS_NAME,'inventory_item')
    cantidad = len(productos)

    assert cantidad >= 1


def test_validar_menu_hamburger_visible_chrome(chrome_browser):
    test_login_chrome(chrome_browser) #Importo test de login OK

    # Valido que el menú hamburger sea visible luego del click
    chrome_browser.find_element(By.ID,'react-burger-menu-btn').click() #Click en menu hamburger
    time.sleep(3) # Espero 3 segundos
    assert chrome_browser.find_element(By.CLASS_NAME,'bm-item-list').is_displayed() == True #Verifico que el menú sea visible

@pytest.mark.skip(reason="Inconvenientes con el select")
def test_validar_filtro_visible_chrome(chrome_browser):
    test_login_chrome(chrome_browser) #Importo test de login OK

    # Valido que los filtros sean visibles luego del click
    dropdown_element = chrome_browser.find_element(By.CLASS_NAME,'select_container').click()
    dropdown = Select(dropdown_element)
    time.sleep(3) # Espero 3 segundos

    # Seleccion opción por texto visible
    dropdown.select_by_visible_text("Price(high to low)")

    time.sleep(3) # Espero 3 segundos

    selected_option = dropdown.first_selected_option
    assert selected_option.text == "Price(high to low)"
    #assert chrome_browser.find_element(By.CLASS_NAME,'active_option').text == "Price(high to low)"


def test_validar_datos_primer_producto_chrome(chrome_browser):
    test_login_chrome(chrome_browser) #Importo test de login OK

    productos = chrome_browser.find_elements(By.CLASS_NAME,'inventory_item') #Productos con filtros default
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
