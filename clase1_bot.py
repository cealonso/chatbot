"""
CLASE 1 - Nace el bot (version 0)
Temas: variables, tipos de datos, input(), print(), f-strings

El bot todavia no "piensa" nada: solo lee lo que escribimos
y responde de forma fija. La idea es que vean que ya con esto
tenemos algo interactivo.
"""

# Variables: guardan informacion para usarla despues
print("=== Mi primer chatbot ===")

nombre = input("¿Cómo te llamás? ")
edad = input("¿Cuántos años tenés? ")

# f-strings: forma moderna de meter variables dentro de un texto
print(f"¡Hola {nombre}! Soy tu primer chatbot 🤖")
print(f"Así que tenés {edad} años, ¡genial!")

# edad llega como texto (str), la convertimos a numero (int) para poder operar
edad = int(edad)
anio_actual = 2026
anio_100 = anio_actual + (100 - edad)

print(f"En el año {anio_100} vas a cumplir 100 años.")

# Ejercicio para practicar en clase:
# 1) Pedir también el color favorito del usuario y devolvérselo en el saludo.
# 2) Calcular en qué año el usuario cumple 18 (si ya los tiene, decir hace cuántos años los cumplió).
