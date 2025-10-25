import pytest

# fuera de la carpeta de los tests
# ruta relativa de los archivos

test_files = [

    "tests/test_login.py",
    "tests/test_login_error.py",
    "tests/test_inventory.py",
    "tests/test_carrito.py"
]

#Argumentos para ejecutar las pruebas: archivos + reporte html
pytest_args = test_files + ["--html=reports/report.html","--self-contained-html","-v"]

pytest.main(pytest_args)

# python3 run_tests.py