# FW_Pruebas_Python_Selenium
Este es un Framework de Automatización de pruebas web con **Python** y **Selenium**, se encuentra diseñado como un framework escalable y mantenible para proyectos de calidad (QA).

## Tabla de Contenidos

1. [Descripción](#descripción)  
2. [Motivación](#motivación)  
3. [Arquitectura](#arquitectura)  
4. [Tecnologías](#tecnologías)  
5. [Requisitos](#requisitos)  
6. [Instalación](#instalación)  
7. [Configuración](#configuración)  
8. [Ejecutar Pruebas](#ejecutar-pruebas)  
9. [Estructura del Proyecto](#estructura-del-proyecto)  
10. [Cómo Extender / Agregar Nuevas Pruebas](#cómo-extender--agregar-nuevas-pruebas)  
11. [Reporte y Logs](#reporte-y-logs)  
12. [Contribuir](#contribuir)  
13. [Licencia](#licencia)  
14. [Autores](#autores)  

---

## Descripción

Este framework proporciona una base organizada para automatizar pruebas web con Selenium y Python. Utiliza buenas prácticas (por ejemplo, Page Object Model), permite claridad y reusabilidad, y está diseñado para integrarse en ambientes de testing avanzados (CI, diferentes entornos).

---

## Motivación

- Evitar scripts desorganizados y difíciles de mantener.  
- Proveer un marco homogéneo para toda la automatización web del equipo.  
- Facilitar la escalabilidad: agregar nuevas pruebas, páginas o utilidades sin romper la estructura existente.  
- Generar reportes legibles y tener logging estructurado.

---

## Arquitectura

Descripción de alto nivel de cómo está organizado el framework:

/src
/pages # Objetos de página (Page Objects)
/tests # Casos de prueba
/utils # Funciones utilitarias (esperas, screenshots, logging)
/config # Archivos de configuración (por ejemplo, para entornos)
/drivers # WebDrivers o helpers para controlarlos

yaml
Copiar código

- **Page Objects**: encapsulan la lógica de interacción con páginas web.  
- **Utils**: helpers comunes reutilizables.  
- **Config**: manejo de distintos ambientes (QA, producción, staging).  

---

## Tecnologías

- Python (versión X.X)  
- Selenium WebDriver  
- pytest / unittest / (lo que uses)  
- (otras librerías: por ejemplo, `selenium-webdriver`, `webdriver-manager`, `pytest-html`, etc.)

---

## Requisitos

1. Python ≥ 3.X  
2. WebDriver para el navegador que usarás (Chrome, Firefox, etc.)  
3. Paquetes de Python listados en `requirements.txt`  
4. Variables de entorno (si aplica): por ejemplo, `BASE_URL`, `ENV`, `BROWSER`

---

## Instalación

1. Clona este repositorio:
   ```bash
   git clone https://github.com/dmefrain02/FW_Pruebas_Python_Selenium_VSCode.git
   cd FW_Pruebas_Python_Selenium_VSCode/EnviromentQA/src