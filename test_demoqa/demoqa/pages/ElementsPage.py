from selenium.webdriver.common.by import By

from demoqa.pages.BasePage import BasePage


class ElementsPage(BasePage):
    BOTON_ELEMENTS = (By.ID, "")
    """LOCALIZADORES DE LA SECCION TEXTBOX"""
    BOTON_TEXT_BOX = (By.ID, "item-0")
    CAMPO_USERNAME = (By.ID, "userName")
    CAMPO_EMAIL = (By.ID, "userEmail")
    CAMPO_DIRECCION_ACTUAL = (By.ID, "currentAddress")
    CAMPO_DIRECCION_PERMANENTE = (By.ID, "permanentAddress")
    BOTON_SUBMIT = (By.ID, "submit")
    """LOCALIZADORES DE LA SECCION CHECKBOX"""
    BOTON_CHECK_BOX = (By.ID, "item-1")
    BOTON_HOME = (By.XPATH, "//span[@class='rct-title'][contains(.,'Home')]")

    BOTON_RADIO_BUTTON = (By.ID, "item-2")
    RADIO_BUTTON_YES = (By.XPATH, "//label[contains(.,'Yes')]")
    RADIO_BUTTON_IMPRESSIVE = (By.XPATH, "//label[contains(.,'Impressive')]")
    RADIO_BUTTON_NO = (By.XPATH, "//label[contains(.,'No')]")

    BOTON_WEB_TABLES = (By.ID, "item-3")

    BOTON_BUTTONS = (By.ID, "item-4")

    BOTON_LINKS = (By.ID, "item-5")

    BOTON_BROKEN_LINKS = (By.ID, "item-6")

    BOTON_UPLOAD_DOWNLOAD = (By.ID, "item-7")

    BOTON_DYNAMIC_PROPERTIES = (By.ID, "item-8")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get("https://demoqa.com/text-box")
        self.driver.maximize_window()

    def text_box(self, full_name, email, add_current, add_permanent):
        self.click_elemento(self.BOTON_TEXT_BOX)
        self.enviar_dato(self.CAMPO_USERNAME, full_name)
        self.enviar_dato(self.CAMPO_EMAIL, email)
        self.enviar_dato(self.CAMPO_DIRECCION_ACTUAL, add_current)
        self.enviar_dato(self.CAMPO_DIRECCION_PERMANENTE, add_permanent)
        self.click_elemento(self.BOTON_SUBMIT)

    def check_box(self):
        self.click_elemento(self.BOTON_HOME)

    def radio_button_yes(self):
        self.click_elemento(self.BOTON_RADIO_BUTTON)
        self.click_elemento(self.RADIO_BUTTON_YES)
        self.click_elemento(self.RADIO_BUTTON_IMPRESSIVE)
        self.click_elemento(self.RADIO_BUTTON_NO)












