from selenium.webdriver.common.by import By
from demoqa.config.config import DatosPrueba
from demoqa.pages.BasePage import BasePage
import pytest


class HomePage(BasePage):
    """Localizadores de la página principal"""
    ELEMENTS_BOTON = (By.XPATH, "//h5[contains(.,'Elements')]")
    FORMS_BOTON = (By.XPATH, "//div[@class='card-body']/h5[contains(.,'Forms')]")
    ALERTS_FRAME_WINDOWS_BOTON = (By.XPATH, "//h5[contains(.,'Alerts, Frame & Windows')]")
    WIDGETS_BOTON = (By.XPATH, "//h5[contains(.,'Widgets')]")
    INTERACTIONS_BOTON = (By.XPATH, "//h5[contains(.,'Interactions')]")
    BOOK_STORE_APPLICATION = (By.XPATH, "//h5[contains(.,'Book Store Application')]")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(DatosPrueba.URL)
        self.driver.maximize_window()

    def obtener_titulo_pagina(self, titulo):
        return self.obtener_titulo(titulo)

    def click_boton_elements(self):
        self.click_elemento(self.ELEMENTS_BOTON)

    def click_boton_forms(self):
        self.click_elemento(self.FORMS_BOTON)

    def click_boton_alerts_frame_wind(self):
        self.click_elemento(self.ALERTS_FRAME_WINDOWS_BOTON)

    def click_boton_widgets(self):
        self.click_elemento(self.WIDGETS_BOTON)

    def click_boton_interactions(self):
        self.click_elemento(self.INTERACTIONS_BOTON)

    def click_boton_book_store_aplication(self):
        self.click_elemento(self.BOOK_STORE_APPLICATION)

