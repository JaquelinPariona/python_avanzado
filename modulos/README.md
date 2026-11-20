# Modularidad
La `Modularidad` consiste en dividir un programa grande en archivos pequeños y reutilizables llamados `modulos`. Cada modulo es simplemente un archivo `.py`.
**Ventajas:**
- `Reutilizacion:` Escribes el codigo una vez y lo usas en muchos programas.
- `Organizacion:` Cada archivo tiene una responsabilidad clara.
- `Mantenimiento:` Es mas facil encontrar y corregir errores.
- `Trabajo en equipo:` Cada persona puede desarrollar su propio modulo.

## 1. Crear un modulo
Basta con crear un archivo con la extension `.py` por ejemplo `matematicas.py`.
## 2. Importa un modulo completo
La manera de como utilizamos los modulos es haciendo de la palabra reservada `import` esto se debe declara en el archivo donde reutilizaremos ciertas funciones o variables de un modulo.
Para importar un modulo completo usamos `impot nombre_archivo`.

`matematicas.py`
```python
def suma(a,b):
    return a+b
def resta(a,b):
    return a-b
```
`main.py`
```python
import matematicas
## para hacer uso de uno de las funciones tengo que acceder al archivo luego un punto y el nombre del dato, funcion que deseamos utilizar
matematicas.resta(5,8)
```