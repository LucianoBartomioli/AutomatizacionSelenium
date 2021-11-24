
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains

from POM.Config.config import DatosPrueba
from POM.Pages.BasePage import BasePage


class LoginPage(BasePage):

    """Estos son los localizadores"""
    EMAIL = (By.ID, "username")
    PASSWORD = (By.ID, "password")
    BOTON_LOGIN = (By.ID, "loginBtn")
    REGISTRARSE_LINK = (By.LINK_TEXT, "Registrarse")

    """Constructor de la clase"""
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(DatosPrueba.BASE_URL)
        self.driver.maximize_window()

    def obtener_titulo_login_page(self, tituto):
        return self.obtener_titulo(tituto)

    def existencia_link_registrarse(self):
        return self.es_visible(self.REGISTRARSE_LINK)

    def iniciar_sesion(self, username, password):
        self.enviar_dato(self.EMAIL, username)
        self.enviar_dato(self.PASSWORD, password)
        self.click_element(self.BOTON_LOGIN)
