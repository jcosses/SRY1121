# Código de ejemplos de ingreso datos

print("EJEMPLOS DE CODIGO EN PYTHON")
print("---------------------------------\n")
vNom = input("Ingrese su Nombre: ")
while True:
    try:
        vEdad = int(input("Ingrese su Edad: "))
        break
    except:
        print("Debe ingresar Datos Númericos")

print("==============================")
print(f"Su Nombre es: {vNom}")
print(f"Su Edad es: {vEdad}")

print("Programa Finalizado")