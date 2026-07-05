from selenium.common import WebDriverException
from src.Function.Inicializar import Inicializar
from selenium import webdriver

#Librerias Webdrivers Services de los navegadores
from selenium.webdriver.chrome.service import Service as ChromeService 
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
#Librerias Webdrivers options de los navegadores
from selenium.webdriver.chrome.options import Options as OpcionesChrome
from selenium.webdriver.firefox.options import Options as OpcionesFirefox
from selenium.webdriver.edge.options import Options as OpcionesEdge
#Librerias Webdrivers Manager de los navegadores
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

class DriverFactory():
    
    # Constructor de la clase DriverFactory. Los parámetros con valores por defecto, se pueden configurar en el archivo Inicializar.py. Asi mismo, se pueden utilizar valores diferentes al llamar a la clase.
    # Estos parámetros permiten configurar el navagador a utilizar, si se desea ejecutar de manera local o remota (con un Selenium Grid en local o en Docker con la URL y puerto del Selenium Grid).
    def __init__(self, navegador=Inicializar.Navegador, URL_Sel_Grid = Inicializar.URL_SeleniumGrid, PortSelGrid = Inicializar.PortSelGrid):
        self.Navegador = navegador
        self.Grid_URL = URL_Sel_Grid # URL del llamado a Selenium Grid
        self.PortSelGrid = PortSelGrid # Puerto del llamado a Selenium Grid
        self.driver = None

        # Diccionario que mapea los nombres de los navegadores a sus funciones de creación correspondientes, sean locales o remotos (selenium grid local o docker)
        self.DRIVER_CREATORS = {
            "Chrome": lambda: self._create_chrome_driver(),
            "Firefox": lambda: self._create_firefox_driver(),
            "Edge": lambda: self._create_edge_driver(),
            "Chrome_Remote": lambda: self._create_chrome_remote_driver(self.Grid_URL),
            "Firefox_Remote": lambda: self._create_firefox_remote_driver(self.Grid_URL),
            "Edge_Remote": lambda: self._create_edge_remote_driver(self.Grid_URL),
        }

    #Retorna el Driver de la instancia del navegador a utilizar en las pruebas.
    def get_driver(self):
        if self.driver is None:    
            creator = self.DRIVER_CREATORS.get(self.Navegador)
            if creator is None:
                raise ValueError(f"Navegador {self.Navegador} no se encuentra soportado.") 
            
            self.driver = creator()
        return self.driver
    
    #Crea y configura el driver de Chrome usando webdriver-manager
    def _create_chrome_driver(self):
        try:
            options = OpcionesChrome()
            prefs = {
                "profile.default_content_settings.popups": 0,
                "download.default_directory": Inicializar.Ruta_Descarga,
                "directory_upgrade":True ,
                "download.prompt_for_download": False,#Para que el navegador no pregunte al descargar
                #"plugins.always_open_pdf_externally": True}) # Para que el navegador no abra el PDF en una pestaña nueva
                #"plugins.plugins_disabled" : ["Chrome PDF Viewer"]
            }
            options.add_experimental_option("prefs", prefs)
            options.add_argument('start-maximized')
            #options.add_argument("headless")
            options.add_argument("--disable-extensions")#Deshabilita extensiones innecesarias
            chrome_driver_path = ChromeDriverManager().install() #Usa webdriver-manager para obtener la última versión compatible
            self.driver = webdriver.Chrome(service=ChromeService(chrome_driver_path), options=options)
            print(self.driver)
            return self.driver
        except WebDriverException as ex:
                self._handle_driver_exception(ex)

    #Crea y configura el driver de Firefox usando webdriver-manager
    def _create_firefox_driver(self):
        try:
            options = OpcionesFirefox()
            options.add_argument('--window-size=1200,1200')# Maximiza la ventana
            self.driver = webdriver.Firefox(service = FirefoxService(GeckoDriverManager().install()),options=options) #Usa webdriver-manager para obtener la última versión compatible
            return self.driver
        except WebDriverException as ex:
                self._handle_driver_exception(ex)

    #Crea y configura el driver de Edge de manera local usando webdriver-manager
    def _create_edge_driver(self):
        try:
            options = OpcionesEdge()
            options.add_argument("--start-maximized")
            self.driver = webdriver.Edge(service =EdgeService(EdgeChromiumDriverManager().install()),options=options)
            self.driver.maximize_window()
            return self.driver
        except WebDriverException as ex:
                self._handle_driver_exception(ex)

    #Crea y configura el driver de Chrome Remote de Selenium Grid
    def _create_chrome_remote_driver(self, grid_url : str):
        try:
            options = OpcionesChrome()
            prefs = {
                "profile.default_content_settings.popups": 0,
                "download.default_directory": Inicializar.Ruta_Descarga,
                "directory_upgrade":True 
            }
            options.add_experimental_option("prefs",prefs)
            options.add_argument('start-maximized')
            self.driver = webdriver.Remote(grid_url,options=options)
            return self.driver 
        except WebDriverException as ex:
                self._handle_driver_exception(ex)

    #Crea y configura el driver de Edge Remote de Selenium Grid
    def _create_edge_remote_driver(self, grid_url : str):
        try:
            options = OpcionesEdge();
            options.add_argument("start-maximized")
            options.add_argument("inprivate")
            #options.add_argument("headless")
            self.driver = webdriver.Remote(grid_url,options=options)
            return self.driver
        except WebDriverException as ex:
                self._handle_driver_exception(ex)

    #Crea y configura el driver de Firefox Remote de Selenium Grid
    def _create_firefox_remote_driver(self, grid_url : str):
        try:
            options = OpcionesFirefox();
            options.add_argument("start-maximized")
            options.add_argument("inprivate")
            #options.add_argument("headless")
            self.driver = webdriver.Remote(grid_url,options=options)
            return self.driver
        except WebDriverException as ex:
                self._handle_driver_exception(ex)

    #Cierra el navegador
    def close_driver(self):
        if self.driver:
            self.driver.quit()
            self.driver = None
        else:
            print("No hay un driver activo para cerrar.")

    #Maneja las excepciones de WebDriver y cierra el driver si ocurre un error al abrir el navegador.
    def _handle_driver_exception(self, exception):
        print(f'No se abrio la instancia del navegador: {self.Navegador} con el error: {exception}' )
        self.close_driver()