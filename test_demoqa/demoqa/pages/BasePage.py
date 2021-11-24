from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def click_elemento(self, by_locator):
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(by_locator)).click()
        except TimeoutException as ex:
            print(ex)
            print(f"No se encontró el elemento -->{by_locator}")

    def enviar_dato(self, by_locator, texto):
        try:
            elem = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(by_locator))
            elem.clear()
            elem.send_keys(texto)
        except TimeoutException as ex:
            print(ex)
            print(f"No se encontró el elemento -->{by_locator}")

    def obtener_texto(self, by_locator):
        try:
            return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(by_locator)).text
        except TimeoutException as ex:
            print(ex)
            print(f"No se encontró el elemento -->{by_locator}")

    def elemento_visible(self, by_locator):
        try:
            return bool(WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(by_locator)))
        except TimeoutException as ex:
            print(ex)
            print(f"No se encontró el elemento -->{by_locator}")

    def select_lista_por_texto_visible(self, by_locator, opcion):
        try:
            select = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(by_locator))
            ds = Select(select)
            ds.select_by_visible_text(opcion)
        except TimeoutException as ex:
            print(ex)
            print(f"No se encontró el elemento -->{by_locator}")

    def obtener_titulo(self, title):
        return bool(WebDriverWait(self.driver, 10).until(EC.title_is(title)))

    def validar_texto_contiene(self, texto_obtenido, texto_esperado):
        if texto_esperado in texto_obtenido:
            return True
        else:
            return False
