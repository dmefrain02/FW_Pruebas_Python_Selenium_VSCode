# FW_Pruebas_Python_Selenium
Este es un Framework de Automatización de pruebas web con **Python** y **Selenium**, se encuentra diseñado como un framework escalable y mantenible para proyectos de calidad (QA).

# Tabla de Contenidos
1.  [Descripción](#Descripción)  
2.  [Motivación](#Motivación)  
3.  [Arquitectura](#Arquitectura)  
4.  [Tecnologías](#Tecnologías)  
5.  [Requisitos del Framework](#Requisitos)  
6.  [Instalación del Framework](#Instalación)  
7.  [Requisitos De Desarrollo](#Desarrollo) 
8.  [Configuración](#Configuración)  
9.  [Diagramas](#Diagramas)
10. [Roadmap De Mejoras en Progreso](#RoadMap) 
11.  [Ejecutar Pruebas Python](#Ejecutar-pruebas-pyhon)
12. [Ejecutar Pruebas Python Behave](#Ejecutar-pruebas-pyhon-behave)
13. [Evidencias](#Evidencias-pruebas)
14. [Docker](#Ejecutar-pruebas-Docker)
15. [Integración Continua Jenkins](#CI-CD-Jenkins)
16. [Reportes](#Reportes)  
17. [Contribuir](#Contribuir)  
18. [Licencia](#Licencia)  
19. [Autor](#Autor)  
20. [Versión del Framework](#Versión)

# Descripción
En este framework se proporciona una base organizada para automatizar pruebas web utilizando Selenium y Python mediante buenas prácticas como: Page Object Model, manejo automático de versiones de los navegadores, posibilidad de utilizar contenedores Docker con Tecnologia VNC para visualizar las ejecuciones de pruebas, escribir/ejecutar pruebas en formato Behave y generacion de distintos tipos de reportes (Allure, Reportes Behave y Reporte Html-TestRunner).

# Motivación
- Evitar scripts desorganizados y difíciles de mantener.
- Proveer un marco homogéneo para la automatización web del equipo.
- Facilitar la escalabilidad: agregar nuevas pruebas, páginas o utilidades sin romper la estructura existente. 
- Generar reportes legibles y tener logging estructurado.
- Tener integracion con herramientas de CI/CD.

# Arquitectura
Descripción de alto nivel de cómo se encuentra organizado el framework:
| Ruta                               | Descripción                                                                                                   |
|------------------------------------|---------------------------------------------------------------------------------------------------------------|
| `/src`                             | Carpeta raíz del framework                                                                                    |
| `/src/Pages`                       | Objetos de página (Page Objects) con las acciones de las Pages y de donde se leen los elementos <br/>         | 
                                       en la paginas através de archivos JSON que contienen los localizadores  de los elementos <br/>                |
                                       (en proceso de refactorización).                                                                              |
| `/src/Test`                        | Scripts de Pruebas creados                                                                                    |
| `/src/Function/Functions.py`       | Funciones Selenium y médotos utilitarios del Framework (en proceso de refactorización).                       |
| `src/Function/Inicializar.py`      | Configuraciones generales del framework (rutas utilzadas y demás configuraciones)                             |
| `src/Function/DriversFactory.py`   | Manejo y creación de los Drivers                                                                              |
| `src/Features`                     | Escenarios de Pruebas escritos en formato Gherkin                                                             |
| `src/Features/steps`               | Steps de los escenarios de pruebas escritos en formato Gherkin                                                |
| `src/Drivers`                      | Drivers de los navegadores                                                                                    |
| `src/Docker`                       | Configuraciones e imágenes Docker para ejecución                                                              |
| `src/Data/Capturas`                | Capturas de pantalla tomadas durante las pruebas                                                              |
| `src/Data/Videos`                  | Grabaciones realizadas durante las pruebas                                                                    |
| `src/Data`                         | Archivos de datos del framework                                                                               |
| `src/selenium_grid`                | Configuraciones para ejecución en Selenium Grid local o en Docker                                             | 
| `src/reports/Report_HtmlTestRunner`| Reportes HtmlTestRunner                                                                                       |
| `src/reports/Report_Allure`        | Reportes Allure                                                                                               |
| `src/reports/Report_Behave`        | Reportes Generados con Behave                                                                                 |
| `src/Selenium IDE`                 | Scripts de Pruebas Generados con Selenium IDE                                                                 |
| `src/Archivos a Cargar`            | Archivos utilizados para pruebas                                                                              |
| `src/Archivos Descargados`         | Archivos descargados durante las pruebas                                                                      |
| `src/Localizadores`                | Archivos JSON que contienen los localizadores de los elmentos de las páginas de los scripts de pruebas.       |
|------------------------------------|---------------------------------------------------------------------------------------------------------------|

# Tecnologías
- Python
- Selenium WebDriver
- Unittest / Behave
- Docker
- Selenium Grid

# Requisitos
1. Python ≥ 3.X  
2. WebDrivers de los navegadores que se utilizarán (Edge, Chrome, Firefox, etc.) o bien tenerlos instalados para usar el manejo automatico de versiones de los navegadores (Webdriver-manager) 
3. Paquetes de Python listados en `requirements.txt`  
4. Variables de entorno Python configuradas

# Instalación
1. Clonar el siguiente repositorio en la rama main:
   git clone https://github.com/dmefrain02/FW_Pruebas_Python_Selenium_VSCode

# Desarrollo
1. Descargar Python de la pagina oficial: https://www.python.org/downloads/
2. Instalar Python en el equipo local en una carpeta personalizada, para un mejor manejo de la instalación y las variables de entorno.
3. Descargar Visual Studio Code de la pagina oficial: https://code.visualstudio.com/Download
4. Instalar Visual Studio Code en el equipo local
5. En el Visual Studio Code, instalar las extensiones requeridas para faclitar el uso de VS Code al escribir/ejecutar scripts de pruebas. Entre algunas a instalar se encuentran:
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
7. Crear las variables de entorno de Python:
   - C:\Python\python.exe
   - C:\Python
   - C:\Python\Lib
   - C:\Python\libs
   - C:\Python\Lib\site-packages
   - C:\Python\Scripts
   - C:\Python\Scripts\pip.exe
8. Descargar las librerias para generar reportes Allure localmente: https://repo1.maven.org/maven2/io/qameta/allure/allure-commandline/2.39.0/
    Nota: Hay versiones más recientes de Allure (de 2.40 a 2.44), estás todavía no se encuentran validadas en su funcinamiento en el framework.
    Pueden generar errores. Se estarán validando, actualizando y habilitando    proximamente.
9. Crear las variables de entorno de Allure:
   - C:\Allure
   - C:\Allure\bin
   - C:\Allure\bin\allure.bat
   - C:\Allure\lib
   - C:\Allure\config
   - C:\Allure\plugins

# Configuración
1. Abrir el folder clonado del repositorio GitHub en Visual Studio Code
2. En la terminal en Visual Studio Code, instalar la libreria virtualenv para activar el entorno virtual del Framework
3. En la terminal en Visual Studio Code, activar el entorno virtual del Framework con el archivo activate ubicado en la carpeta Scripts del Enviroment.
4. Instalar las librerias con el archivo 'requirements.txt' en la carpeta raiz del Framework en el entorno virtual activado.
5. Realizar las configuraciones necesarias para utilizar el Framework, las mismas se realizan en el archivo **src/Function/Inicializar.py**. Las configuraciones a realizar son las siguientes:
    
    **Directorio Base - Obtiene la ruta del directorio src del proyecto**</br>
    Esta variable obtiene el directorio raíz del proyecto, que es la direccion a partir de donde se construyen las demás rutas que  se utilizan en el Framework.
    BaseDir = os.path.abspath(os.path.join(__file__,"../.."))

    **Carpeta para guarda videos**</br>
    Ruta donde se almancenaran los videos que se guarden como evidencias de rutas.
    - Carpeta_Videos = BaseDir + u'\Data\Videos'

    **Si se utiliza Selenium Grid, se debe configurar el puerto y la URL utilizado en la configuración del Hub de Selenium Grid.**</br>
    Configuración para ejecutar pruebas utilizando selenium grid.
    - PortSelGrid = "4444" 
    - URL_SeleniumGrid = r"http://localhost:"+PortSelGrid+"/wd/hub"

    **Configurar el arreglo de navegadores según los navegadores que se quieran utilizar en las pruebas, y siguiendo la nomenclatura de navegadores dada en el metodo abrir_navegador para cada navegador.**
    **Si no se configura este arrreglo, se puede utilizar el parametro: Navegador**</br>
    Arreglo para utilizar multi-browers en la ejecución de las pruebas.
    **Ejemplos:**
    - Navegadores_Sel_Grid = ["Chrome_Remote","Firefox_Remote","Edge_Remote"] -> Navegadores en Selenium Grid Local o en Docker
    - Navegadores_Sel_Grid = ["Chrome","Firefox","Edge]                       -> Navegadores Locales

    **Parámetro que define el navegador a utilizarn en la ejecución de pruebas**
    - Navegador = 'Edge' | 'Chrome' | 'Firefox'

   **Function\Functions.py clase que maneja las funcionaes de Selenim y métodos utilitarios**

    **Function\DriverFactory.py clase para la creación de los Drivers de los navegadores ya sea locales o selenium grid local o en docker**
    - self.DRIVER_CREATORS
      Diccionario de navegadores que maneja la creación de los navegadores a utilizar en las pruebas apartir del valor enviado en el parámetro **self.Navegador** ya sea como **parámetro individual o através del arreglo de navegadores.**
    
    **Tiempo de espera utilizado dentro del Framework**</br>
    Parámetro para realizar tiempos de espera informales en la ejecución de las pruebas.
    - Tiempo_Espera = 1
    
    **Pagina en nuevo tab abierto**</br>
    Parámetro para definir el nombre del tab al abrir nuevos tab en la ejecución de las pruebas.
    - Page_Tab = 'about:blank'
    
    **Rutas utilizadas dentro del Framework**</br> 
    Estás rutas permiten guardar archivos o tomar archivos durante la ejecución de pruebas.
    - Archivo_Cargar = BaseDir + r'\Archivos a Cargar\software-quality.png'
    - Ruta_Descarga = BaseDir + r'\Archivos Descargados'
    - Archivo_Descargado = "requirements.txt"
    - Bitacora= BaseDir + r'\Archivos Descargados\Pruebas Descargas Archivos.txt'
    - Imagenes_Cortadas = BaseDir + r'\Data\Imagenes Cortadas'
    
    **Rutas y Configuraciones para la captura de evidencias en las pruebas, esta es la configuración para manejar la toma de capturas de pantallas en las pruebas**</br> 
    Estás rutas y parámetros permiten realizar la configuración para poder tomar capturas de pantalla durante la ejecución de pruebas.
    - Path_Evidencias = BaseDir + r'\Data\Capturas'
    - Path_Evidencias = ""
    - TestCase_x_Context = "S" #S o N
    - Warning_Capturas = "Warning: Sin configurar el Path y el contexto para las capturas de pantalla."
        
    **Directorios de archivos Json**</br> 
    Ruta donde se almacenan los archivos JSON de las clases Pages con los localizadores de las páginas de pruebas.
    - Json = BaseDir + r'\Localizadores'
    - JsonRespondata = BaseDir + r'\Data\Json'
    
    **Formato Hora y Fecha**</br>
    Configuración de los formatos de fecha y hora que seran utilizados por el Framework
    - DateFormat = '%d-%m-%Y'
    - HourFormat = '%H%M%S'

    **Ruta Excel para escribir resultados o leer datos**</br> 
    Variable para leer un archivo Excel con datos de pruebas.
    - Excel_Leer_Escribir = BaseDir + r'\Data\Pruebas1.xlsx'
    
    **Ruta Excel para crear excel**</br>
    Variable para crear un archivo excel que se pueda utilizar en las pruebas.
    - Excel_Crear = BaseDir + r'\Data'
    
    **Configuraciones para ambientes de pruebas con conexion a Base de Datos**</br>
    Para hacer uso de bases de datos tomando datos de tablas, se requiere configurar alguna de las secciones de conexión a bases de de datos.
    #Enviroment == 'Dev':
    URL_Dev = f'' #La f solo va si requerimos pasarle parametros en el link
    USER_Dev = ''
    Cadena_Conexion_Dev = 'DRIVER={ODBC Driver 17 for SQL Server}; SERVER=[Servidor BD];DATABASE=[Base de Datos];UID=[User Base de Datos];PWD=[Contraseña Base de Datos]'

    #Enviroment == 'QA':    
    URL_QA = f'' #La f solo va si requerimos pasarle parametros en el link
    USER_QA = '' 
    Cadena_Conexion_QA = 'DRIVER={ODBC Driver 17 for SQL Server}; SERVER=[Servidor BD];DATABASE=[Base de Datos];UID=[User Base de Datos];PWD=[Contraseña Base de Datos]

    #Enviroment == 'UAT':
    URL_UAT = f'' #La f solo va si requerimos pasarle parametros en el link
    USER_UAT = ''
    Cadena_Conexion_UAT = 'DRIVER={ODBC Driver 17 for SQL Server}; SERVER=[Servidor BD];DATABASE=[Base de Datos];UID=[User Base de Datos];PWD=[Contraseña Base de Datos]

    #Enviroment == 'PROD':
    URL_PROD = f'' #La f solo va si requerimos pasarle parametros en el link
    USER_PROD = ''
    Cadena_Conexion_Prod = 'DRIVER={ODBC Driver 17 for SQL Server}; SERVER=[Servidor BD];DATABASE=[Base de Datos];UID=[User Base de Datos];PWD=[Contraseña Base de Datos]

# Diagramas
**Organización del Proyecto**
src
│
├── Pages
├── Test
├── Drivers
├── Docker
├── Features
│   └── steps
├── Localizadores
├── Data
├── Reports
├── Function
│
└── Inicializar.py

**Organización de los Datos**
Tests
   │
   ├───────────────┐
   ▼               ▼
Pages          JSON Locators
   │
   ▼
Functions
   │
   ▼
DriverFactory

**Organización Operativa del Framework**
           Tests
             │
             ▼
        Page Objects
             │
             ▼
         Functions

             │
             ▼
          DriverFactory

# RoadMap 
| **Estado**  |	**Mejora**                |
|     ✅	   |  *JSON Locators*             |
|     ✅	   |  *DriverFactory*             |
|     🔄	    |  *Refactorización Functions* |
|     🔄	    |  *Refactorización Pages*     |
|     ⏳	   |  *Utility Classes*           |
|     ⏳	   |  *Base Page*                 |
|     ⏳	   |  *Common Components*         |
|     ⏳	   |  *GitHub Actions*            |
|     ⏳	   |  *Jenkins*                   |
|     ⏳	   |  *SonarCloud*                |

# Versión
  📌 La versión actual del framework es: **3.1.0**  

# Licencia
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE) </br>
Este Framework de automatizacion de prueba se encuentra bajo licencia de uso MIT.
https://github.com/dmefrain02/FW_Pruebas_Python_Selenium_VSCode

# Autor
**Ing. en Sistemas Efraín Castañeda Delgado, Cartago, Costa Rica**
