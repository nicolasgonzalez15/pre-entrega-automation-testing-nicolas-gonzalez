import pytest
import time
from test_login import test_login_chrome
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

def test_carrito_aparece_un_elemento_chrome(chrome_browser):
    test_login_chrome(chrome_browser) #Importo test de login OK

    productos = chrome_browser.find_elements(By.CLASS_NAME,'inventory_item')
    primer_producto = productos[0]

    time.sleep(3)

    primer_producto.find_element(By.CLASS_NAME,'btn_inventory').click()

    time.sleep(3)

    items_carrito = chrome_browser.find_element(By.CLASS_NAME,'shopping_cart_badge')

    assert int(items_carrito.text) == 1
    assert primer_producto.find_element(By.CLASS_NAME,'btn_inventory').text == 'Remove'