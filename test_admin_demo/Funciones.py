import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException


# driver = webdriver.Chrome(executable_path=r".\driver\chromedriver.exe")
class Funciones_globales():
    """
    Clase contenedora de las funciones
    """
    def __init__(self, driver):
        self.driver = driver
        # self.driver = webdriver.Chrome(executable_path=r".\driver\chromedriver.exe")

    def navergar(self, url, t):
        self.driver.get(url)
        self.driver.maximize_window()
        return time.sleep(t)

    def insertar_texto_valida(self, tipo, elemento,  texto, t):
        """
        tipo = ESPERA EL TIPO DE SELECTOR
        """

        if tipo == "id" or tipo == "Id" or tipo == "ID":
            try:
                var = WebDriverWait(self.driver, 4).until(EC.visibility_of_element_located((By.ID, elemento)))
                var = self.driver.execute_script("arguments[0].scrollIntoView();", var)
                var = self.driver.find_element(By.ID, elemento)
                var.clear()
                var.send_keys(texto)
                return time.sleep(t)
            except TimeoutException as ex:
                print(ex)
                print(f"No se encontró el elemento {tipo} --> {elemento}")
        elif tipo == "Xpath" or tipo == "XPATH" or tipo == "xpath":
            try:
                WebDriverWait(self.driver, 4).until(EC.visibility_of_element_located((By.XPATH, elemento)))
                var = self.driver.find_element(By.XPATH, elemento)
                self.driver.execute_script("arguments[0].scrollIntoView();", var)
                var.clear()
                var.send_keys(texto)
                return time.sleep(t)
            except TimeoutException as ex:
                print(ex)
                print(f"No se encontró el elemento {tipo} --> {elemento}")

    def click_elemento_valida(self, tipo, elemento, t):
        if tipo == "id" or tipo == "Id" or tipo == "ID":
            try:
                var = WebDriverWait(self.driver, 4).until(EC.visibility_of_element_located((By.ID, elemento)))
                var = self.driver.find_element(By.ID, elemento)
                self.driver.execute_script("arguments[0].scrollIntoView();", var)
                var.click()
                return time.sleep(t)
            except TimeoutException as ex:
                print(ex)
                print(f"No se encontró el elemento {tipo} --> {elemento}")
        elif tipo == "Xpath" or tipo == "XPATH" or tipo == "xpath":
            try:
                WebDriverWait(self.driver, 4).until(EC.visibility_of_element_located((By.XPATH, elemento)))
                var = self.driver.find_element(By.XPATH, elemento)
                self.driver.execute_script("arguments[0].scrollIntoView();", var)
                var.click()
                return time.sleep(t)
            except TimeoutException as ex:
                print(ex)
                print(f"No se encontró el elemento {tipo} --> {elemento}")

    def texto_validar(self, tipo, elemento, texto_esperado, t):
        if tipo == "id" or tipo == "Id" or tipo == "ID":
            try:
                print(WebDriverWait(self.driver, 4).until(EC.visibility_of_element_located((By.ID, elemento))))
                var = self.driver.find_element(By.ID, elemento)
                self.driver.execute_script("arguments[0].scrollIntoView();", var)
                var.text
                assert var == texto_esperado, f"El texto obtenido --> {var} no corresponde al texto esperado --> {texto_esperado}"
                return time.sleep(t)
            except TimeoutException as ex:
                print(ex)
                print(f"No se encontró el elemento {tipo} --> {elemento}")
        elif tipo == "Xpath" or tipo == "XPATH" or tipo == "xpath":
            try:
                WebDriverWait(self.driver, 4).until(EC.visibility_of_element_located((By.XPATH, elemento)))
                var = self.driver.find_element(By.XPATH, elemento)
                self.driver.execute_script("arguments[0].scrollIntoView();", var)
                var.click()
                return time.sleep(t)
            except TimeoutException as ex:
                print(ex)
                print(f"No se encontró el elemento {tipo} --> {elemento}")
