from src.Pages.BasePageObjects import BasePageObjects
class GooglePage(BasePageObjects):

    
    def __init__(self):
        super().__init__()

    def open_browser(self,navegador):
        self.abrir_navegador(navegador)

    def goToURL(self,URL):
        self.get_url_driver(URL)

    def close_browser(self):
        self.cerrar_driver_navegador()

    def hacer_Click(self, entidad, valor_busqueda):
        self.action_selenium.Click_Element(entidad,valor_busqueda)

    def obtener_archivo_json(self,file):
        self.action_selenium.obtener_archivo_json(file)

    def espera_elemento(self):
        self.esperar_elemento(2)