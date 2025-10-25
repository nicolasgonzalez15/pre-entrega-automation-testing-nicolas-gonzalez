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
- **pytest.ini** (Configuraciones iniciales pytest)
- **conftest.py** (Fixtures para diferentes tipos de browsers / prueba de Login reutilizable)
- **utils.py** (Archivo con funciones reutilizables - login reutilizable)
- **reports/** 
  - **report.html** (Reporte de ejecuciones de tests unitarios con pytest-html)
- **tests/**
    - **test_login.py** (tests de login exitoso)
    - **test_login_error.py** (tests de login con error - validar mensaje de error)
    - **test_inventario.py**
    - **test_filtros.py** 
    - **test_carrito.py**

  # Ejecución de tests
  ## Para correr todos los tests, utilizar el siguiente comando:
  python3 -m pytest tests/ -v
  ## Para correr un test en particular:
  python3 -m pytest tests/test_login.py -v
  ## Para generar reporte html con detalles de todos los casos:
  python3 -m pytest --html=reports/report.html --self-contained-html
 
    
