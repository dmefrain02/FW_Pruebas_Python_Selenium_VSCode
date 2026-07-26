from src.Function.Functions import Functions
from src.Function.Inicializar import Inicializar
from src.Function.DriverFactory import DriverFactory
from src.Function.actions_Selenium import actions_Selenium
import json
import pytest
import time

class BasePageObjects:
    def __init__(self):
        self.functions = Functions()
        self.action_selenium = actions_Selenium()

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