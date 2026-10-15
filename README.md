# Práctica de Python en Azure

## Objetivo
Crear, ejecutar, probar y versionar un proyecto Python.

## Requisitos
- Python 3
- Git

## Instalación
```bash
python3 -m venv .venv
```

Activar el entorno virtual:

- Bash (Azure Cloud Shell / Linux): `source .venv/bin/activate`
- PowerShell (Windows): `.\.venv\Scripts\Activate.ps1`
  - Si PowerShell bloquea la activación: `.\.venv\Scripts\python.exe main.py`

Instalar dependencias:
```bash
python -m pip install -r requirements.txt
```

## Ejecución
```bash
python main.py
```

## Pruebas
```bash
python -m py_compile src/calculos.py main.py
python -m unittest discover -s tests -v
```

## Error provocado y corregido
Se modificó `sumar()` para que devolviera `a - b`. La prueba `test_sumar` falló
(`AssertionError: -2 != 10`). Se restauró `return a + b` y las cuatro pruebas volvieron a pasar.

## Entorno
Azure Cloud Shell o PowerShell local.

## Autor
Alex Vazquez
