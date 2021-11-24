import time

import pytest
from selenium.webdriver.common.by import By

from demoqa.config.config import DatosPrueba
from demoqa.pages.BasePage import BasePage
from demoqa.pages.ElementsPage import ElementsPage
from demoqa.test.test_base import BaseTest


class Test_ElementsPage(BaseTest):
    def test__titulo_text_box_page(self):
        self.ElementsPage = ElementsPage(self.driver)
        flag = self.ElementsPage.obtener_titulo(DatosPrueba.TITULO_PAGINA)
        assert flag, f"El titulo de la pagina no coincide con {DatosPrueba.TITULO_PAGINA}"

    def test_text_box(self):
        self.ElementPage = ElementsPage(self.driver)
        self.ElementPage.text_box(
            DatosPrueba.USERNAME,
            DatosPrueba.EMAIL,
            DatosPrueba.DIRECCION_ACTUAL,
            DatosPrueba.DIRECCION_PERMANENTE
        )
        texto_devuelto_nombre = self.ElementPage.obtener_texto((By.ID, "name"))
        texto_devuelto_email = self.ElementPage.obtener_texto((By.ID, "email"))
        texto_devuelto_current_address = self.ElementPage.obtener_texto((By.ID, "currentAddress"))
        print(texto_devuelto_current_address)
        texto_devuelto_permanent_address = self.ElementPage.obtener_texto((By.ID, "permanentAddress"))
        assert self.ElementPage.validar_texto_contiene(texto_devuelto_nombre, DatosPrueba.USERNAME)
        assert self.ElementPage.validar_texto_contiene(texto_devuelto_email, DatosPrueba.EMAIL)

        # assert DatosPrueba.USERNAME in texto_devuelto_nombre, "El nombre obtenido no coincide con el ingresado."
        # assert DatosPrueba.EMAIL in texto_devuelto_email, "El email obtenido no coincide con el ingresado."
        # assert DatosPrueba.DIRECCION_ACTUAL in texto_devuelto_current_address, "La direccion actual obtenida " \
        #                                                                        "no coincide con la ingresada."
        # assert DatosPrueba.DIRECCION_PERMANENTE in texto_devuelto_permanent_address, "La direccion permanente " \
        #                                                                              "obtenida no coincide con la " \
        #                                                                              "ingresada."

    def test_text_box_vacio(self):
        self.ElementPage = ElementsPage(self.driver)
        self.ElementPage.text_box(
            "",
            "",
            "",
            ""
        )

    def test_email_invalido(self):
        self.ElementPage = ElementsPage(self.driver)
        self.ElementPage.text_box(
            "",
            "123asdas",
            "",
            ""
        )
