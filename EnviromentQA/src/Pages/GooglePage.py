from src.Pages.BasePageObjects import BasePageObjects
class GooglePage(BasePageObjects):

    def __init__(self):
        super().__init__()

    def open_browser(self,navegador):
        self.functions.abrir_navegador(navegador)

    def goToURL(self,URL):
        self.Functions.get_url_driver(URL)

    def close_browser(self):
        self.functions.cerrar_driver_navegador()