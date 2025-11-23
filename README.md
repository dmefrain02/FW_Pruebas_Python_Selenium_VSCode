# FW_Pruebas_Python_Selenium
Este es un Framework de Automatización de pruebas web con **Python** y **Selenium**, se encuentra diseñado como un framework escalable y mantenible para proyectos de calidad (QA).

## Tabla de Contenidos

1. [Descripción](#descripción)  
2. [Motivación](#motivación)  
3. [Arquitectura](#arquitectura)  
4. [Tecnologías](#tecnologías)  
5. [Requisitos del Framework](#requisitos)  
6. [Instalación del Framework](#instalación)  
7. [Configuración del Framework](#configuración)  
8. [Ejecutar Pruebas](#ejecutar-pruebas)  
9. [Estructura del Proyecto](#estructura-del-proyecto)  
10. [Cómo Extender / Agregar Nuevas Pruebas](#cómo-extender--agregar-nuevas-pruebas)  
11. [Reporte y Logs](#reporte-y-logs)  
12. [Contribuir](#contribuir)  
13. [Licencia](#licencia)  
14. [Autores](#autores)  

---
## Descripción
En este framework se proporciona una base organizada para automatizar pruebas web con Selenium y Python. Utilizando buenas prácticas tales como: Page Object Model, manejo automático de versiones de los navegadores, posibilidad de utilizar contenedores Docker con Tecnologia VNC para visualizar las ejecuciones de pruebas, poder escribir/ejecutar pruebas en formato Behave y generacion de distintos tipos de reportes (Allure, Reportes Behave y Reporte Html-TestRunner)). Además, permite claridad y reusabilidad, se encuentra diseñado para integrarse en ambientes de testing avanzados (CI, diferentes entornos).

---
## Motivación
- Evitar scripts desorganizados y difíciles de mantener.  
- Proveer un marco homogéneo para la automatización web del equipo.  
- Facilitar la escalabilidad: agregar nuevas pruebas, páginas o utilidades sin romper la estructura existente.  
- Generar reportes legibles y tener logging estructurado.
- Tener integracion con herramientas de CI/CD

---
## Arquitectura
Descripción de alto nivel de cómo está organizado el framework:
- **/src** → Carpeta raíz del Framework  
- **/Pages** → Objetos de página (Page Objects). Archivos JSON con localizadores.  
- **/Test** → Casos de prueba  
- **/Function/Functions.py** → Funciones Selenium y utilidades del framework  
- **/Function/Inicializar.py** → Configuraciones generales del framework (rutas utilzadas y demás configuraciones)
- **/Features** → Pruebas escritas en formato Behave (Gherkin)  
- **/Features/steps** → Pasos (steps) de pruebas Behave  
- **/Drivers** → WebDrivers de los navegadores  
- **/Docker** → Configuraciones e imágenes Docker para ejecución  
- **/Data/Capturas** → Capturas de pantalla de pruebas  
- **/Data/Videos** → Grabaciones de pruebas  
- **/Data** → Archivos de datos del framework  
- **/selenium_grid** → Configuraciones para ejecución en Selenium Grid local o Docker  
- **/report/reportHtmltestrunner** → Reportes HtmlTestRunner  
- **/report/reports** → Reportes Allure  
- **/report/reportBehave** → Reportes generados por Behave  
- **/Archivos a Cargar** → Archivos utilizados para pruebas  
- **/Archivos Descargados** → Archivos descargados durante las pruebas  
- **Page Objects**: encapsulan la lógica de interacción con páginas web. En este framework se maneja en archivos en formato JSON. 

---
## Tecnologías
- Python
- Selenium WebDriver
- Unittest / Behave
- Docker
- Selenium Grid

---
## Requisitos
1. Python ≥ 3.X  
2. WebDriver para el navegador que usarás (Chrome, Firefox, etc.) o bien tenerlos instalados para usarlos desde el manejo automatico de versiones de los navegadores (Webdriver-manager) 
3. Paquetes de Python listados en `requirements.txt`  
4. Variables de entorno Python

---
## Instalación
1. Clona este repositorio:
   git clone https://github.com/dmefrain02/FW_Pruebas_Python_Selenium_VSCode.git

# Configuración
1. Descargar Python de la pagina oficial: https://www.python.org/downloads/
2. Instalar Python en el equipo local.
3. Descargar Visual Studio Code de la pagina oficial: https://code.visualstudio.com/Download
4. Instalar Visual Studio Code en el equipo local
5. En el Visual Studio Code, instalar las extensiones requeridas para faclitar el uso. Entre algunas a instalar se encuentran:
   - Bracket Pair Color DLW
   - Code Runner
   - Cucumber
   - Docker
   - ESLint
   - GitHub Actions
   - GitHub Copilot
   - GitHub Copilot Chat
   - Live Server
   - NPM
   - Material Icono Theme
   - Playwright Test VS for Code
   - Prettier - Code formatter
   - Pylance
   - Python
   - Python Debugger
   - Python Enviroments
7. Crear las siguientes variables de entorno de Python:
   - C:\Python\python.exe
   - C:\Python
   - C:\Python\Lib
   - C:\Python\libs
   - C:\Python\Lib\site-packages
   - C:\Python\Scripts
   - C:\Python\Scripts\pip.exe
8. Crear las siguientes variables de entorno de Allure:
   - C:\Allure 2_9_0
   - C:\Allure 2_9_0\bin
   - C:\Allure 2_9_0\bin\allure.bat
   - C:\Allure 2_9_0\lib
   - C:\Allure 2_9_0\config
   - C:\Allure 2_9_0\plugins
9. Abrir el folder clonado del repositorio GitHub en Visual Studio Code
10. En la terminal en Visual Studio Code, instalar la libreria virtualenv para activar el entorno virtual del Framework
11. En la terminal en Visual Studio Code, activar el entorno virtual del Framework con el archivo activate en la carpeta Scripts del Enviroment.
12. Instalar las librerias con el archivo 'requirements.txt' en la carpeta raiz del Framework en el entorno virtual activado.
13. Realizar las configuracione necessrias para utilizar el Framework, las mismas se realizan en src/Function/Inicializar.py. Las configuraciones a realizar son las siguientes:
    
    # Carpeta para guarda videos
    - Carpeta_Videos = BaseDir + u'\Data\Videos'

    # Si se utilizara Selenium Grid, se debe configurar el puerto y la URL utilizado en la configuración del Hub de Selenium Grid sea que se encuentre instalado localmente o en una imagen de Docker.
    - PortSelGrid = "4444" 
    URL_SeleniumGrid = r"http://localhost:"+PortSelGrid+"/wd/hub"

    # Configurar este arreglo de navegadores según los navegadores que se quieran utilizar para las pruebas, y siguiendo la nomenclatura de navegadores dada en el metodo abrir_navegador para cada navegador.
    Ejemplos:
    - Navegadores_Sel_Grid = ["Chrome_Docker","Firefox_Docker"] -> Navegadores en Selenium Grid en Docker
    - Navegadores_Sel_Grid = ["Chrome_Remote","Firefox_Remote"] -> Navegadores en Selenium Grid Local
    - Navegadores_Sel_Grid = ["Chrome","Firefox"]               -> Navegadores Locales
    
    # Tiempo de espera utilizado dentro del Framework
    - Tiempo_Espera = 1
    
    # Pagina en nuevo tab abierto
    - Page_Tab = 'about:blank'
    
    # Rutas utilizadas dentro del Framework
    - Archivo_Cargar = BaseDir + r'\Archivos a Cargar\software-quality.png'
    - Ruta_Descarga = BaseDir + r'\Archivos Descargados'
    - Archivo_Descargado = "requirements.txt"
    - Bitacora= BaseDir + r'\Archivos Descargados\Pruebas Descargas Archivos.txt'
    - Imagenes_Cortadas = BaseDir + r'\Data\Imagenes Cortadas'
    
    # Rutas y Configuraciones para la captura de evidencias en las pruebas, esta es la configuración para manejar la toma de capturas de pantallas en las pruebas
    - Path_Evidencias = BaseDir + r'\Data\Capturas'
    - Path_Evidencias = ""
    - TestCase_x_Context = "S" #S o N
    - Warning_Capturas = "Warning: Sin configurar el Path y el contexto para las capturas de pantalla."
      
    # Directorios de archivos Json
    - Json = BaseDir + r'\Pages'
    - JsonRespondata = BaseDir + r'\Data\Json'
    
    # Formato Hora y Fecha
    - DateFormat = '%d-%m-%Y'
    - HourFormat = '%H%M%S'
    
    # Navegador a Utilizar
    - Navegador = 'Edge'
    
    # Ruta Excel para escribir resultados o leer datos
    - Excel_Leer_Escribir = BaseDir + r'\Data\Pruebas1.xlsx'
    
    # Ruta Excel para crear excel
    - Excel_Crear = BaseDir + r'\Data'
    
    # Configuraciones para ambientes de pruebas con conexion a Base de Datos
    Enviroment == 'Dev':
    - URL_Dev = f'' #La f solo va si requerimos pasarle parametros en el link
    - USER_Dev = ''
    - Cadena_Conexion_Dev = 'DRIVER={ODBC Driver 17 for SQL Server}; SERVER=EFRAIN-CD\EFRAINCD;DATABASE=Pruebas_Automatizadas_Python_DEV;UID=EFRAIN_ACD;PWD=114660137'
    - Se puede replicar estas 3 variables para ambientes de QA, UAT y Produccion.