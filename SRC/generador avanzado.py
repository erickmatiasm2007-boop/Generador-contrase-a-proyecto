import random
import string

# Función para generar la contraseña
def generar_contrasena(longitud, usar_numeros):

    # Caracteres básicos (letras)
    caracteres = string.ascii_letters

    # Si el usuario desea números, se agregan
    if usar_numeros:
        caracteres += string.digits

    contrasena = ""

    # Construcción de la contraseña
    for i in range(longitud):
        contrasena += random.choice(caracteres)

    return contrasena


print("================================")
print(" GENERADOR DE CONTRASEÑAS ")
print("================================")

# Solicitar longitud
longitud = int(input("Ingrese la longitud de la contraseña: "))

# Solicitar si desea números
respuesta = input("¿Desea incluir números? (s/n): ")

usar_numeros = False

if respuesta.lower() == "s":
    usar_numeros = True

# Generar contraseña
resultado = generar_contrasena(longitud, usar_numeros)

print("\nContraseña generada:")
print(resultado)
