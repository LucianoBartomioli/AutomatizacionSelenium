from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains

"""Esta es la clase padre de todas las paginas"""
"""Esta contiene todos los metodos genericos para todas las paginas"""


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def click_element(self, by_locator):
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).click()
        except TimeoutException as ex:
            print(ex)
            print(f"No se encontró el elemento {by_locator}")

    def enviar_dato(self, by_locator, texto):
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).send_keys(texto)
        except TimeoutException as ex:
            print(ex)
            print(f"No se encontró el elemento {by_locator}")

    def obtener_texto(self, by_locator):
        try:
            return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).text
        except TimeoutException as ex:
            print(ex)
            print(f"No se encontró el elemento {by_locator}")

    def es_visible(self, by_locator):
        try:
            return bool(WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).text)
        except TimeoutException as ex:
            print(ex)
            print(f"No se encontró el elemento {by_locator}")

    def obtener_titulo(self, title):
        WebDriverWait(self.driver, 10).until(EC.title_is(title))
        return self.driver

