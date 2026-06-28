# -*- coding: utf-8 -*- 
import unittest
from src.Function.Functions import Functions as Selenium
from src.Function.Inicializar import Inicializar

class Test(unittest.TestCase):

    def setUp(self):
        Selenium.obtener_archivo_json(self, 'Localizadores_Mercado_Libre')
        Selenium.abrir_navegador(self,"Edge_Docker",True,False,Inicializar.URL_SeleniumGrid,Inicializar.PortSelGrid)
        self.functions = Selenium() 
        #self.functions.configurar_entorno_grabacion()

    def Test_01(self):
        for Nav_Sel_Grid in Inicializar.Navegadores_Sel_Grid:
            Selenium.abrir_navegador(self,Nav_Sel_Grid, True)
            Selenium.get_url_driver(self,"https://demoqa.com/alerts")
            Selenium.WebdriverWait(self,2)
            Selenium.click_en_elemento(self, "btn-accept")
            Selenium.alert_navegadores(self,0,"You clicked a button","No se muestra el mensaje correcto")
            Selenium.WebdriverWait(self,2)
            Selenium.cerrar_driver_navegador(self)
        
    def Test_02(self): 
        Selenium.get_url_driver(self,"https://demoqa.com/alerts")
        Selenium.WebdriverWait(self,2)
        Selenium.click_en_elemento(self, "btn-time")
        Selenium.esperar_elemento(self, 5)
        Selenium.alert_navegadores(self,1,"This alert appeared after 5 seconds","No se muestra el mensaje correcto")
        Selenium.esperar_elemento(self, 5)

    def test_08(self):
        Selenium.get_url_driver(self,"https://www.google.com/")
        Selenium.Click_Element(self, "Google","txt_busqueda_google")
        Selenium.esperar_elemento(self, 3)
        Selenium.SendKeys(self, "Google","txt_busqueda_google", "Selenium")
        Selenium.Clear_Element(self, "Google","txt_busqueda_google")
        Selenium.Scroll_Element_JS(self, "Google","txt_busqueda_google")
        Selenium.SendKeys(self, "Google","txt_busqueda_google", "Selenium 2") 
        Selenium.Double_Click(self, "Google","txt_busqueda_google")
        Selenium.Click_Derecho(self, "Google","txt_busqueda_google")
        Selenium.Explicit_Wait_Element(self, "Google","txt_busqueda_google", 15)
        Selenium.Move_Element(self, "Google","txt_busqueda_google")
        Selenium.esperar_elemento(self, 3)

    def Test_03(self):
        for Nav_Sel_Grid in Inicializar.Navegadores_Sel_Grid:
            Selenium.abrir_navegador(self,Nav_Sel_Grid, True)
            Selenium.get_url_driver(self,"https://demoqa.com/alerts")
            Selenium.WebdriverWait(self,2)
            Selenium.click_en_elemento(self, "btn-OK-cancel")
            Selenium.WebdriverWait(self,2)
            Selenium.alert_navegadores(self,2,"You selected Ok","No se muestra el mensaje correcto","","texto-OK")
            Selenium.esperar_elemento(self, 2)
            Selenium.cerrar_driver_navegador(self)
        
    def Test_04(self):
        for Nav_Sel_Grid in Inicializar.Navegadores_Sel_Grid:
            Selenium.abrir_navegador(self,Nav_Sel_Grid, True)
            Selenium.get_url_driver(self,"https://demoqa.com/alerts")
            Selenium.WebdriverWait(self,2)
            Selenium.click_en_elemento(self, "btn-OK-cancel")
            Selenium.WebdriverWait(self,2)
            Selenium.alert_navegadores(self,3,"You selected Cancel","No se muestra el mensaje correcto","","texto-Cancel")
            Selenium.WebdriverWait(self,2)
            Selenium.cerrar_driver_navegador(self)
        
    def Test_05(self):
        Selenium.abrir_navegador(self,"Chrome")
        Selenium.get_url_driver(self,"https://demoqa.com/alerts")
        Selenium.WebdriverWait(self,2)
        Selenium.click_en_elemento(self, "btn-txt-ing")
        Selenium.esperar_elemento(self, 2)
        Selenium.alert_navegadores(self,4,"","","You entered","texto-ing", "Test")
        Selenium.WebdriverWait(self,2)
        Selenium.cerrar_driver_navegador(self)
        
    def Test_06(self):
        for Nav_Sel_Grid in Inicializar.Navegadores_Sel_Grid:
            Selenium.abrir_navegador(self,Nav_Sel_Grid, True)
            Selenium.get_url_driver(self,"https://demoqa.com/alerts")
            Selenium.WebdriverWait(self,2)
            Selenium.click_en_elemento(self, "btn-accept")
            Selenium.alert_navegadores(self,0,"You clicked a button","No se muestra el mensaje correcto")
            Selenium.WebdriverWait(self,2)
            Selenium.cerrar_driver_navegador(self)

    def Test_07(self):
        Selenium.abrir_navegador(self,"Chrome")
        Selenium.get_url_driver(self,"https://www.mercadolibre.co.cr/")
        Selenium.obtener_elemento(self, "Home", "Busqueda_Mercado_Libre")
        Selenium.click_en_elemento(self, "Home", "Busqueda_Mercado_Libre")
        Selenium.obtener_Texto(self, "Home", "Busqueda_Mercado_Libre")
        Selenium.escribir_texto(self, "Home", "Busqueda_Mercado_Libre", texto="Laptop")
        Selenium.envio_teclas_especificas(self, "Home", "Busqueda_Mercado_Libre", key="enter")
        #Selenium.limpiar_elemento(self, "Home", "Busqueda_Mercado_Libre")
        Selenium.espera_explicita_elemento(self, "Home", "Busqueda_Mercado_Libre")
        #Selenium.obtener_elemento_select(self, "Home", "Busqueda_Mercado_Libre")
        #Selenium.obtener_elemento_select_texto(self, "Home", "Busqueda_Mercado_Libre", "Apple")
        Selenium.Double_Click(self, "Home", "Busqueda_Mercado_Libre")
        Selenium.Click_Derecho(self, "Home", "Busqueda_Mercado_Libre")
        Selenium.Mover_Mouse_x_App_Web(self, "Home", "Busqueda_Mercado_Libre")
        Selenium.download_file(self, "Home", "Busqueda_Mercado_Libre")
        #Selenium.Mover_Mouse(self, "Home", "Busqueda_Mercado_Libre", "Home", "Busqueda_Mercado_Libre")

    def tearDown(self):
        #self.functions.detener_grabacion()      
        Selenium.cerrar_driver_navegador(self)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()