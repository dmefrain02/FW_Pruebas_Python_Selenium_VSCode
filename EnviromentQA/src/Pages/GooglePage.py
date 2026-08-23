from src.Pages.BasePageObjects import BasePageObjects
class GooglePage(BasePageObjects):

    def __init__(self):
        super().__init__()

    def open_browser(self,navegador):
        self.driver = self.abrir_navegador(navegador)
        return self.driver

    def goToURL(self,URL):
        self.get_url_driver(URL)

    def close_browser(self):
        self.cerrar_driver_navegador()

    def hacer_Click(self, driver, entidad, valor_busqueda):
        self.action_selenium.Click_Element(driver,entidad,valor_busqueda)

    def SendKeys(self, driver, entidad, valor_busqueda, texto):
        self.action_selenium.SendKeys(driver,entidad,valor_busqueda,texto)

    def obtener_archivo_json(self,file):
        self.action_selenium.obtener_archivo_json(file)

    def espera_elemento(self):
        self.esperar_elemento(2)

    def send_keys_specific(self, driver, entidad, valor_busqueda, key):
        self.action_selenium.Send_Keys_Specific(driver,entidad,valor_busqueda,key)

    def limpiar_elemento(self, driver, entidad, valor_busqueda):
        self.action_selenium.Clear_Element(driver,entidad,valor_busqueda)

    def explicit_wait_element(self, driver,entidad, valor_busqueda, tiempo_espera):
        self.action_selenium.Explicit_Wait_Element(driver,entidad,valor_busqueda,tiempo_espera)

    def scroll_to_element(self, driver, entidad, valor_busqueda):
        self.action_selenium.Scroll_Element_JS(driver,entidad,valor_busqueda)

    def double_click(self, driver, entidad, valor_busqueda):
        self.action_selenium.Double_Click(driver,entidad,valor_busqueda)

    def click_derecho(self, driver, entidad, valor_busqueda):
        self.action_selenium.Click_Derecho(driver,entidad,valor_busqueda)

    def move_to_element(self, driver, entidad, valor_busqueda):
        self.action_selenium.Move_Element(driver,entidad,valor_busqueda)