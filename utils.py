
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


def login(driver):

    driver.get("https://www.saucedemo.com") # Invoco al driver

            # Completamos login
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    
    time.sleep(2)  # pequeña espera para redirección