## Parametros Nominales y por Defecto
# Crea una funcion llamada calcular_precio_final que calcule el precio de un producto aplicando un impuesto y un descuento opcional.

def calcular_precio_final(precio_base, impuesto=0.18, descuento=0.0):
    precio_con_descuento = precio_base * (1 - descuento)
    precio_total = precio_con_descuento * (1 + impuesto)
    return round(precio_total, 2)

# Prueba de funcion
## Llamada usando argumentos nominales para modificar solo el descuento
total = calcular_precio_final(100, descuento=0.05)
print(f"Precio final: {total}")  # Resultado: 112.1