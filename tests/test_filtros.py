import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

def test_filtrar_high_low(login_driver):
    driver = login_driver  # Importo test de login OK

    # Valido que los filtros sean visibles luego del click
    dropdown_element = driver.find_element(By.CLASS_NAME, 'product_sort_container')
    dropdown_element.click()
    dropdown = Select(dropdown_element)
    time.sleep(3)  # Espera breve para asegurar que el dropdown esté activo

    # Selecciono opción por texto visible
    #dropdown.select_by_visible_text("Price (high to low)")
    dropdown.select_by_value("hilo")
    time.sleep(2)  # Espera para que se actualicen los productos

    # Validar que los productos están ordenados correctamente
    productos = driver.find_elements(By.CLASS_NAME, "inventory_item_price")
    precios = [float(producto.text.replace("$", "")) for producto in productos]
    
    # Verificar que los precios estén en orden descendente
    assert precios == sorted(precios, reverse=True), "Los productos no están ordenados de mayor a menor precio."

def test_filtrar_low_high(login_driver):
    driver = login_driver  # Importo test de login OK

    # Valido que los filtros sean visibles luego del click
    dropdown_element = driver.find_element(By.CLASS_NAME, 'product_sort_container')
    dropdown_element.click()
    dropdown = Select(dropdown_element)
    time.sleep(3)  # Espera breve para asegurar que el dropdown esté activo

    # Selecciono opción por texto visible
    #dropdown.select_by_visible_text("Price (high to low)")
    dropdown.select_by_value("lohi")
    time.sleep(2)  # Espera para que se actualicen los productos

    # Validar que los productos están ordenados correctamente
    productos = driver.find_elements(By.CLASS_NAME, "inventory_item_price")
    precios = [float(producto.text.replace("$", "")) for producto in productos]
    
    # Verificar que los precios estén en orden ascendente
    assert precios == sorted(precios, reverse=False), "Los productos no están ordenados de menor a mayor precio."

def test_filtrar_z_a(login_driver):

    driver = login_driver  # Usar el driver proporcionado por el fixture

    # Valido que los filtros sean visibles luego del click
    dropdown_element = driver.find_element(By.CLASS_NAME, 'product_sort_container')
    dropdown_element.click()
    dropdown = Select(dropdown_element)
    time.sleep(1)  # Espera breve para asegurar que el dropdown esté activo

    # Selecciono opción por valor "za" (de Z a A)
    dropdown.select_by_value("za")
    time.sleep(2)  # Espera para que se actualicen los productos

    # Validar que los productos están ordenados correctamente por nombre
    productos = driver.find_elements(By.CLASS_NAME, "inventory_item_label")
    nombres = [producto.text for producto in productos]

    # Verificar que los nombres estén en orden descendente (de Z a A)
    assert nombres == sorted(nombres, reverse=True), "Los productos no están ordenados de Z a A."

def test_filtrar_a_z(login_driver):

    driver = login_driver  # Usar el driver proporcionado por el fixture

    # Valido que los filtros sean visibles luego del click
    dropdown_element = driver.find_element(By.CLASS_NAME, 'product_sort_container')
    dropdown_element.click()
    dropdown = Select(dropdown_element)
    time.sleep(1)  # Espera breve para asegurar que el dropdown esté activo

    # Selecciono opción por valor "za" (de Z a A)
    dropdown.select_by_value("az")
    time.sleep(2)  # Espera para que se actualicen los productos

    # Validar que los productos están ordenados correctamente por nombre
    productos = driver.find_elements(By.CLASS_NAME, "inventory_item_label")
    nombres = [producto.text for producto in productos]

    # Verificar que los nombres estén en orden descendente (de Z a A)
    assert nombres == sorted(nombres, reverse=False), "Los productos no están ordenados de A a Z."