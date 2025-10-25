import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# 1) Validar que aparece en carrito un elemento
def test_carrito_aparece_un_elemento(login_driver):
    driver = login_driver #Importo test de login OK

    productos = driver.find_elements(By.CLASS_NAME,'inventory_item')
    primer_producto = productos[0]

    time.sleep(3)

    primer_producto.find_element(By.CLASS_NAME,'btn_inventory').click()

    time.sleep(3)

    items_carrito = driver.find_element(By.CLASS_NAME,'shopping_cart_badge')

    assert int(items_carrito.text) == 1
    assert primer_producto.find_element(By.CLASS_NAME,'btn_inventory').text == 'Remove'

# 2) Validar que aparece en checkout un elemento agregado
def test_carrito_verificar_checkout_productos(login_driver):

    driver = login_driver #Importo test de login OK
    
    time.sleep(2)
    
    test_carrito_aparece_un_elemento(driver) #Importo el test de carrito de 1 elemento

    time.sleep(2)

    botonCarrito = driver.find_element(By.CLASS_NAME,'shopping_cart_link').click()

    time.sleep(2)

    items_cart = driver.find_elements(By.CLASS_NAME,'cart_list')

    first_product = items_cart[0]

    time.sleep(2)

    first_quantity = first_product.find_element(By.CLASS_NAME,'cart_quantity').text
    assert int(first_quantity) == 1

    first_name = first_product.find_element(By.ID,'item_4_title_link').text
    assert first_name == "Sauce Labs Backpack"
