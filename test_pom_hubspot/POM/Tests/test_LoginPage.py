import pytest

from POM.Config.config import DatosPrueba
from POM.Pages.LoginPage import LoginPage
from POM.Tests.test_base import BaseTest


class Test_Login(BaseTest):

    def test_link_registrarse_es_visible(self):
        self.loginPage = LoginPage(self.driver)
        bandera = self.loginPage.existencia_link_registrarse()
        assert bandera, "El link de registrarse no está visible"

    def test_login_page_titulo(self):
        self.loginPage = LoginPage(self.driver)
        titulo = self.loginPage.obtener_titulo_login_page(DatosPrueba.TITULO_PAGINA_LOGIN)
        assert titulo == DatosPrueba.TITULO_PAGINA_LOGIN, "El título de la pagina de inicio de sesion no coincide con el esperado"

    def test_login(self):
        self.loginPage = LoginPage(self.driver)
        self.loginPage.iniciar_sesion(DatosPrueba.USER_NAME, DatosPrueba.PASSWORD)
