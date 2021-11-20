import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from Funciones import Funciones_globales

t = 0.3


def test_login_datos_invalidos():
    # global driver, f
    driver = webdriver.Chrome(executable_path=r".\driver\chromedriver.exe")
    f = Funciones_globales(driver)
    f.navergar("https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F", t)
    f.insertar_texto_valida("id", "Email", "Agustin", t)
    f.insertar_texto_valida("id", "Password", "123456", t)
    f.click_elemento_valida("xpath", "//button[@type='submit']", t)
    f.texto_validar("id", "Email-error", "Wrong email", t)
    time.sleep(2)
    driver.close()


def test_login_datos_validos():
    # global driver, f
    driver = webdriver.Chrome(executable_path=r".\driver\chromedriver.exe")
    f = Funciones_globales(driver)
    f.navergar("https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F", t)
    f.insertar_texto_valida("id", "Email", "admin@yourstore.com", t)
    f.insertar_texto_valida("id", "Password", "admin", t)
    f.click_elemento_valida("xpath", "//button[@type='submit']", t)
    f.click_elemento_valida("xpath", "//p[contains(text(),' Dashboard')]", t)
    driver.close()


def test_buscar_product_name():
    # global driver, f
    driver = webdriver.Chrome(executable_path=r".\driver\chromedriver.exe")
    f = Funciones_globales(driver)
    f.navergar("https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F", t)
    f.insertar_texto_valida("id", "Email", "admin@yourstore.com", t)
    f.insertar_texto_valida("id", "Password", "admin", t)
    f.click_elemento_valida("xpath", "//button[@type='submit']", t)
    # f.click_elemento_valida("xpath", "//i[@class='fa fa-bars']", t)
    f.click_elemento_valida("xpath", "//i[@class='right fas fa-angle-left '][1]", t)
    f.click_elemento_valida("xpath", "(//p[contains(.,'Products')])[1]", t)
    f.insertar_texto_valida("id", "SearchProductName", "Build your own computer", t)
    time.sleep(3)
    driver.close()
