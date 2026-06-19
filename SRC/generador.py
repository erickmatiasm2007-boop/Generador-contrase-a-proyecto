import random
import string

print("================================")
print(" GENERADOR DE CONTRASEÑAS ")
print("================================")

longitud = int(input("Ingrese la longitud de la contraseña: "))

caracteres = string.ascii_letters + string.digits

contrasena = ""

for i in range(longitud):
    contrasena += random.choice(caracteres)

print("\nContraseña generada:")
print(contrasena)
