 ## Empaquetado Posicional (*args)
## Crea una función llamada unir_frases(*args) que reciba una cantidad variable de cadenas de texto (str) y las una en una sola oración separadas por un espacio, retornando el resultado final.

def unir_frases(*args: str) -> str:
    return " ".join(args)

# Prueba de funcion
oracion = unir_frases("Python", "es", "un", "lenguaje", "versátil.")
print(oracion)