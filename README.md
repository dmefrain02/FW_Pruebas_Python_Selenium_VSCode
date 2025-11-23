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

/src -> Carpeta raiz del Framework
/Pages                        # Objetos de página (Page Objects). Son archivos en formato Json para manejar los localizadores utilizados en las pruebas.
/Test                         # Casos de prueba
/Function/Functions.py        # Funciones selenium y de framework para realizar las pruebas
/Function/Inicializar.py      # Configuraciones utilizadas en el Framework
/Features                     # Pruebas escritas en formato behave (formato Gherkins)
/Features/steps               # Pasos de las pruebas en formato behave (formato Gherkins)
/Drivers                      # WebDrivers de los navegadores para utilizarlos
/Docker                       # Configuraciones e imagenes docker que se quieran utilizar
/Data/Capturas                # Almacenamiento de capturas de las pruebas
/Data/Videos                  # Almacenamiento de grabaciones de las pruebas
/Data                         # Archivos con datos de pruebas
/selenium_grid                # Configuraciones para ejecutar pruebas en selenium grid tanto localmente como en Docker.
/report/reporthtmltestrunner  # Reportes con la libreria HtmlTestRunner
/report/reports               # Reportes con la libreria Allure
/report/reportBehave          # Reportes generados con Behave
/Archivos a Cargar            # Archivos cargados en las pruebas 
/Archivos Descargados         # Archivos descargados en las pruebas

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