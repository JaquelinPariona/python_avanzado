# Haciendo uso de lambda crear una funcion que me muestre un mensaje personalizado.



# Crear una funcion para calcular el area de un rectangulo, siendo la formula la siguiente area=base*altura.
area_rectangular=lambda b,h: b*h
base = float(input("Ingrese la base del rectacgulo: "))
altura = float(input("Ingrese la altura del rectacgulo: "))
print(f"El area del rectangulo es: {area_rectangular(base,altura)}")


# Crear una funcion que verifique si un numero es par o impar 
# Primera forma
es_par=lambda n: n%2 == 0

if es_par(4):
    print("es par")
else:
    print("es inpar")
# Segunda forma
si_es_par=lambda n:"es par" if n%2==0 else "es inpar"
print(si_es_par(100))