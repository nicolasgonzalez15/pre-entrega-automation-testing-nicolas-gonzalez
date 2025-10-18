# QA Automation - Sauce Demo - Pre-entrega
Proyecto de QA Automation Testing, basado en el sitio de Sauce Demo, utilizando pytest, selenium webdriver y Python

## Propósito del proyecto
Con el fin de ahorrar tiempo y recursos, se quiere automatizar flujos críticos de módulos de:
 - Pantalla de Login, utilizando datos válidos e inválidos
 - Menú principal, con submenues, filtros, y catálogo de productos
 - Carrito de compras, al agregar productos al mismo

## Tecnologías usadas
* Python
* Selenium webdriver (Levantar browser automatizado)
* pytest (test unitarios)
  

## Estructura de carpetas

- **README.md**
- **pytest.ini/** (Configuraciones iniciales pytest)
- **test/**
    - **conftest.py** (Fixtures para diferentes tipos de browsers)
    - **test_login.py**
    - **test_error.py**
    - **test_inventario.py**
    - **test_carrito.py**
    - **reportes/** 
        - **report.html**

  # Ejecución de tests
  ## Para correr todos los tests, utilizar el siguiente comando:
  python3 -m pytest test/ -v
  ## Para correr un test en particular:
  python3 -m pytest test/test_login.py -v
  ## Para generar reporte html con detalles de todos los casos:
  * python3 -m pytest --html=reportes/report.html --self-contained-html
 
    
