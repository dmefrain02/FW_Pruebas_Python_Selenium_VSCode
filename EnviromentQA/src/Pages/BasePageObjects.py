from src.Function.Functions import Functions
from src.Function.Inicializar import Inicializar
from src.Function.DriverFactory import DriverFactory
from src.Function.Actions_Selenium import Actions_Selenium
import os # para capturas
import allure
import json
import pytest
import time

class BasePageObjects:
    def __init__(self):
        self.functions = Functions()
        self.action_selenium = Actions_Selenium()
        self.Nav_utilizado_capturas = None

    # Método para abrir el navegador según la configuración de Inicializar, el parámetro navegador y la opción de Selenium Grid seleccionada. Se puede abrir un navegador local, en docker o selenium grid local según la configuración.
    def abrir_navegador(self,navegador=Inicializar.Navegador, URL_SeleniumGrid = Inicializar.URL_SeleniumGrid,PortSelGrid=Inicializar.PortSelGrid):
        print(u"Directorio Base:" + Inicializar.BaseDir)
        print("-------------------------------------------")
        print(navegador)
        print("-------------------------------------------")
        self.Nav_utilizado_capturas = navegador   

        # Crear una instancia de DriverFactory con la URL y el puerto de Selenium Grid
        self.DriverFactory = DriverFactory(navegador)
        # Obtener el driver del navegador especificado
        self.driver = self.DriverFactory.get_driver()
        print(f"Se abrio el navegador {navegador} correctamente.")
        return self.driver  

    #Ir a la URL del sitio  
    def get_url_driver(self,URL):
        return self.driver.get(URL)

    #Cerrar la instancia del navegador
    def cerrar_driver_navegador(self):
        if self.driver:
            self.driver.quit()
            print(f'Se cerro del navegador')
        else:
            print("No hay un driver activo para cerrar.")

    #Espera informal
    def esperar_elemento(self,tiempo_espera = Inicializar.Tiempo_Espera):
        print("Inicia Espera: " +str(tiempo_espera))
        try:
            totalWait = 0
            while(totalWait < tiempo_espera):
                time.sleep(1)
                totalWait = totalWait + 1
                print("Tiempo total actual de espera: " + str(totalWait))
        finally:
            print("Espera: Carga Finalizada")

     #Crear ruta para capturas de pantallas
    
        #Obtener fecha actual
    
    #Obtener fecha actual
    def obtener_fecha_actual(self):
        self.fecha = time.strftime(Inicializar.DateFormat)#Formato Fecha
        return self.fecha
    
    #Obtener hora actual
    def obtener_hora_actual(self):
        self.hora = time.strftime(Inicializar.HourFormat)#Formato 24Hrs
        return self.hora

    #Crear ruta para capturas de pantallas
    def crear_path(self):
        fecha = self.obtener_fecha_actual()
        GeneralPath = Inicializar.Path_Evidencias
        print(f'Ruta General de las Capturas: {GeneralPath}')
        DriverTest = self.Nav_utilizado_capturas            
        TestCase =self.__class__.__name__

        HoraActual = self.obtener_hora_actual()
        
        if((Inicializar.TestCase_x_Context =="S") and (GeneralPath != "")):
            path = f"{GeneralPath}\{fecha}\Pruebas\{TestCase}\{DriverTest}\{HoraActual}"
            print(f"Ruta Contruida para guardar las capturas: {path}")
        elif((Inicializar.TestCase_x_Context == "N") and (GeneralPath != "")):
            path =f"{GeneralPath}\{fecha}\{TestCase}\{DriverTest}\{HoraActual}"
            print(f"Ruta Contruida para guardar las capturas: {path}")
        elif(((Inicializar.TestCase_x_Context == "N") or (Inicializar.TestCase_x_Context == "S")) and (GeneralPath == "")):
            path = f'{Inicializar.BaseDir}\Capturas\{fecha}\{TestCase}\{DriverTest}\{HoraActual}'
            print(f'No se encuentra establecida la ruta para guardar la captura de pantalla, se guardara en la carpeta raiz del framework de pruebas.\nEn: {path}')
        elif(((Inicializar.TestCase_x_Context !="S") or (Inicializar.TestCase_x_Context !="N") or (Inicializar.TestCase_x_Context == "")) and (GeneralPath == "")): 
            path = ""
            print(f'No se logro crear el path para guardar la captura de pantalla. Variables de "TestCase_x_Context" y "GeneralPath" no se han configurado correctamente: Tienen el valor: {GeneralPath} y {Inicializar.TestCase_x_Context}')

        if (path != ""):
            if not os.path.exists(path):
                os.makedirs(path)

        return path

    #Realizar captura de pantalla
    def capturar_pantalla(self, descripcion="", captura_allure=False):
        path = self.crear_path()
        
        if captura_allure:
            allure.attach(self.driver.get_screenshot_as_png(),descripcion,allure.attachment_type.PNG)
        elif path:
            img = os.path.join(
                path,
                f'({self.obtener_fecha_actual()} - {self.obtener_hora_actual()}).png',
            )
            print(f'Se realizo captura de pantalla de la prueba: {img}')
            return self.driver.get_screenshot_as_file(img)
        else:
            print(Inicializar.Warning_Evidencias)
    
    #Realizar captura de pantalla en reporte Allure
    def captura_pantalla_allure(self,Descripcion):
        allure.attach(self.driver.get_screenshot_as_png(),Descripcion,allure.attachment_type.PNG)