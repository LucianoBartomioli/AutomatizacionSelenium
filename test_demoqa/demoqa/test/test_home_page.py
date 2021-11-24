import time

import pytest
from selenium.webdriver.common.by import By

from demoqa.config.config import DatosPrueba
from demoqa.pages.HomePage import HomePage
from demoqa.test.test_base import BaseTest


class Test_Homepage(BaseTest):

    def test_home_page_titulo(self):
        self.homePage = HomePage(self.driver)
        flag = self.homePage.obtener_titulo(DatosPrueba.TITULO_PAGINA)
        assert flag, f"El titulo de la pagina no coincide con {DatosPrueba.TITULO_PAGINA}"

    def test_click_boton_element(self):
        self.homePage = HomePage(self.driver)
        self.homePage.click_boton_elements()
        assert self.driver.current_url == "https://demoqa.com/elements", "La url no es correcta"

    def test_click_boton_forms(self):
        self.homePage = HomePage(self.driver)
        self.homePage.click_boton_forms()
        assert self.driver.current_url == "https://demoqa.com/forms", "La url no es correcta"

    def test_click_boton_widgets(self):
        self.homePage = HomePage(self.driver)
        self.homePage.click_boton_widgets()
        assert self.driver.current_url == "https://demoqa.com/widgets", "La url no es correcta"



