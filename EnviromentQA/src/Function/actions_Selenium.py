#Librerias Webdrivers funcionalidades
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.remote.webelement import isDisplayed_js
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.alert import Alert
from src.Function.Inicializar import Inicializar
from selenium.common.exceptions import NoSuchElementException,NoAlertPresentException,NoSuchWindowException,TimeoutException, UnexpectedAlertPresentException, WebDriverException
import json
import pytest

class actions_Selenium:

    # Diccionario para mapear las estrategias de búsqueda a los valores de By
    BY = {
        "ID": By.ID,
        "NAME": By.NAME,
        "XPATH": By.XPATH,
        "CSS": By.CSS_SELECTOR,
        "CLASS": By.CLASS_NAME,
        "LINK": By.LINK_TEXT,
        "TAG": By.TAG_NAME
    }

    def obtener_archivo_json(self,file):
        json_ruta = Inicializar.Json + "/"+file+'.json'
        try:
            with open(json_ruta,'r')as read_file:
                self.json_strings = json.loads(read_file.read())
                print(u'Se obtuvo el archivo Json: ' + file)
                print(u"Obtener Archivo Json: " + json_ruta)
                print(self.json_strings)
                return self.json_strings
            
        except FileNotFoundError:
            self.json_strings =False
            pytest.skip(u'Obtener Archivo Json: No se encontro el archivo json' + file)
            Functions.cerrar_driver_navegador(self)

    #Metodo para encontrar elementos en el DOM
    def Find_Element_On_DOM(self,estrategia_busqueda, valor_busqueda, driver=None):
        try:
            elemento = driver.find_element(self.BY[estrategia_busqueda], valor_busqueda)
            print(u'Find Element: Se esta interactuando con el elemento ' + valor_busqueda)
            return elemento
        except TimeoutException:
            print(u'El elemento esperado no se encontro: ' + valor_busqueda)
        except NoSuchElementException:
            print(u'El elemento esperado no se encontro: ' + valor_busqueda)
     
    #Obtener entidad de elemento en el archivo JSON       
    def Get_Entity(self,page, elemento):
        try:
            if self.json_strings is False:
                print(u'Define el archivo JSON de la prueba')
            else:
                entidad = self.json_strings[page][elemento]
                print(f"Se encontraron los valores en el JSON para la entidad utilizada: " + str(elemento) + " con los valores " + str(entidad))
                return entidad
                
        except KeyError as e:
            pytest.skip(
                f"Obtener Entidad: no se encontro la Key a la cual se hace referencia {elemento} en el archivo JSON de la pagina {page}. Error: {e}"
            )         
            
    # Método genérico para obtener un elemento a partir del archivo JSON
    def Get_Element(self,page, elemento, driver=None):
        GetEntity = actions_Selenium.Get_Entity(self, page, elemento)
        if GetEntity is None:
            print(u'No se encontro el valor de la entidad buscada en el archivo .Json')
        else:
            try:
                elemento = actions_Selenium.Find_Element_On_DOM(self,GetEntity["GetFieldBy"].upper(), GetEntity["ValueToFind"],driver) 
                print(u'Obtener Elemento: se encontro el elemento: ' + GetEntity["GetFieldBy"] + ' con el valor: ' + GetEntity["ValueToFind"])
                return elemento
            except NoSuchElementException:
                print(u'Obtener Elemento: no se encontro el elemento ' + GetEntity["GetFieldBy"] + ' con el valor: ' + GetEntity["ValueToFind"])
            except TimeoutException:
                print(u'Obtener Elemento: no se encontro el elemento ' + GetEntity["GetFieldBy"] + ' con el valor: ' + GetEntity["ValueToFind"])       
    
    # Método para obtener el texto de un elemento a partir de la entidad del archivo JSON
    def Get_Text(self,page, elemento):
        GetEntity = actions_Selenium.Get_Element(self, page, elemento)
        try:
            print(u'Obtener Texto: Texto en el elemento ' + str(elemento))
            return GetEntity.text
        except NoSuchElementException:
            print(u'Obtener Texto: No se logro obtener el texto del elemento ' + str(elemento))
        except TimeoutException:
            print(u'Obtener Texto: No se logro obtener el texto del elemento ' + str(elemento))

    # Método para hacer click en un elemento a partir de la entidad del archivo JSON 
    def Click_Element(self,driver,page, elemento):
        GetEntity = actions_Selenium.Get_Element(self, page, elemento, driver)
        try:
            print(u'Se realizo click en el elemento ' + str(elemento))
            return GetEntity.click()
        except NoSuchElementException:
            print(u'Elemento click: no se encontro el elemento ' + str(elemento) + u' para hacer click')
        except TimeoutException:
            print(u'Elemento click, no se encontro el elemento ' + str(elemento) + u' para hacer click')
    
    # Método para enviar texto a un elemento a partir de la entidad del archivo JSON
    def SendKeys(self,driver, page,elemento,texto):
        GetEntity = actions_Selenium.Get_Element(self, page, elemento, driver)
        try:
            print(f'Escribir texto: se escribio el texto {texto} en el elemento {elemento}')
            return GetEntity.send_keys(texto)
        except NoSuchElementException:
            print(u'Escribir Texto: No se encontro el elemento ' + str(elemento) + u' para escrbir el valor: {texto}') 
        except TimeoutException:
            print(u'Escribir Texto: No se encontro el elemento ' + str(elemento) + u' para escribir el valor: {texto}')
    
    # Método para enviar teclas específicas a un elemento a partir de la entidad del archivo JSON
    def Send_Keys_Specific(self,driver, page,elemento,key):
        try:
            if key.lower()=='enter':
                actions_Selenium.Get_Element(self,page,elemento,driver).send_keys(Keys.ENTER)
                print(u'Se presiono la tecla ' + key + ' en el elemento indicado: ' + str(elemento))
            if key.lower()=='tab':
                actions_Selenium.Get_Element(self,page,elemento,driver).send_keys(Keys.TAB)
                print(u'Se presiono la tecla ' + key + ' en el elemento indicado: ' + str(elemento))
            if key.lower()=='space':
                actions_Selenium.Get_Element(self,page,elemento,driver).send_keys(Keys.SPACE)   
                print(u'Se presiono la tecla ' + key + ' en el elemento indicado: ' + str(elemento))
                
        except TimeoutException:  
            print(u'No se logro realizar la acción con la tecla indicada ' + key + " en el elemento indicado: " + str(elemento))  

    # Método para limpiar el texto de un elemento a partir de la entidad del archivo JSON
    def Clear_Element(self,driver,page, elemento):  
        GetEntity = actions_Selenium.Get_Element(self, page, elemento, driver)
        try:
            print(u'Limpiar Elemento: Se limpio el elemento ' + str(elemento))
            return GetEntity.clear()
        except NoSuchElementException:
            print(u'Limpiar Elemento: no se logro limpiar el elemento ' + str(elemento))
        except TimeoutException:
            print(u'Limpiar Elemento: no se logro limpiar el elemento ' + str(elemento))

    # Método para obtener un elemento select a partir de la entidad del archivo JSON
    def Get_Element_Select(self,page, elemento):
        GetEntity = actions_Selenium.Get_Entity(self, page, elemento)
        if GetEntity is None:
            print(u'No se encontro el valor de la entidad buscada en el archivo .Json')
        else:
            try:
                select = Select(self.driver.find_element(actions_Selenium.BY[GetEntity["GetFieldBy"].upper()],GetEntity["ValueToFind"]))
                print(u"get elements: " + GetEntity["ValueToFind"]) 
                return select
            except NoSuchElementException:
                print(u"Select_Element: No presente " + GetEntity["ValueToFind"])
            except TimeoutException:
                print(u"Select_Element: No presente " + GetEntity["ValueToFind"])

    # Método para seleccionar un elemento de un select por su texto visible a partir de la entidad del archivo JSON  
    def obtener_elemento_select_texto(self,page, elemento, texto):
        select = actions_Selenium.Get_Element_Select(self, page, elemento)
        select.select_by_visible_text(texto)
    
    # Método para esperar explícitamente a que un elemento sea visible y clickeable a partir de la entidad del archivo JSON          
    def Explicit_Wait_Element(self,driver,page, elemento, tiempo_espera):  
        GetEntity = actions_Selenium.Get_Entity(self, page, elemento)
        if GetEntity is None:
            print(u'No se encontro el valor de la entidad buscada en el archivo .Json')
        else:
            try:
                wait =WebDriverWait(driver,tiempo_espera)
                wait.until(EC.visibility_of_element_located((actions_Selenium.BY[GetEntity["GetFieldBy"].upper()],GetEntity["ValueToFind"])))
                wait.until(EC.element_to_be_clickable((actions_Selenium.BY[GetEntity["GetFieldBy"].upper()],GetEntity["ValueToFind"])))   
                print(u'Espera explicita: se visualizo el elemento ' + str(page) + ' con el valor ' + GetEntity["ValueToFind"])
                return True
            except NoSuchElementException:
                print(u'Esperar explicita: no se encontro o no se visualizo el elemento luego de la espera ' + str(page) + ' con el valor ' + GetEntity["ValueToFind"])
            except TimeoutException:
                print(u'Esperar explicita: no se encontro o no se visualizo el elemento luego de la espera ' + str(page) + ' con el valor ' + GetEntity["ValueToFind"])

    # Método para realizar scroll hasta un elemento a partir de la entidad del archivo JSON
    def Scroll_Element_JS(self, driver, page, elemento):
        GetEntity = actions_Selenium.Get_Element(self, page, elemento, driver)
        try: 
            driver.execute_script("arguments[0].scrollIntoView();", GetEntity)
            print(u'JS Scroll: Se realizo scroll_to hasta el elemento ' + str(page) + ' con el valor ' + elemento)
            return True
        except TimeoutException:
            print(u'JS Scroll: No se logro realizar hacia el elemento ' + str(page) + ' con el valor ' + elemento)

    # Método para hacer doble click en un elemento a partir de la entidad del archivo JSON
    def Double_Click(self, driver, page, elemento):
        action =ActionChains(driver)
        element = actions_Selenium.Get_Element(self, page, elemento, driver)
        try:
            action.double_click(element).perform()
            print(f'Double Click: se realizo doble click en el elemento ' + str(page) + ' con el valor ' + str(elemento))

        except NoSuchElementException:
            print(u'Double Click: no se logro realizar doble click en el elemento ' + str(page) + ' con el valor ' + str(elemento))
        except TimeoutException:
            print(u'Double Click: no se logro realizar doble click en el elemento ' + str(page) + ' con el valor ' + str(elemento))

    # Método para hacer click derecho en un elemento a partir de la entidad del archivo JSON    
    def Click_Derecho(self, driver,page, elemento):
        action =ActionChains(driver)
        element = actions_Selenium.Get_Element(self, page, elemento, driver)
        try:
            action.context_click(element).perform()
            print(f'Click Derecho: se realizo click derecho en el elemento ' + str(page) + ' con el valor ' + str(elemento))
        except NoSuchElementException:
            print(u'Click Derecho: no se logro realizar click derecho en el elemento ' + str(page) + ' con el valor ' + str(elemento))
        except TimeoutException:
            print(u'Click Derecho: no se logro realizar click derecho en el elemento ' + str(page) + ' con el valor ' + str(elemento))

    # Método para mover el mouse a un elemento a partir de la entidad del archivo JSON
    def Move_Element(self, driver, page, elemento):
        action = ActionChains(driver)
        element = actions_Selenium.Get_Element(self, page, elemento, driver)
        try:
            action.move_to_element(element).perform()
            print(f'Mover Mouse: se movio el mouse al elemento ' + str(page) + ' con el valor ' + str(elemento))
        except NoSuchElementException:
            print(u'Mover_mouse: no se encontro el elemento ' + str(page) + ' con el valor ' + str(elemento))
        except TimeoutException:
            print(u'Mover_mouse: no se encontro el elemento ' + str(page) + ' con el valor ' + str(elemento))