""" 
def mostrar_menu():
    print("=== Menú Principal ===")
    print("1. Iniciar sesión")
    print("2. Salir")
    opcion = input("Seleccione una opción: ")
    return opcion

def iniciar_sesion(estudiantes):
    usuario = input("Ingrese su nombre de usuario: ")
    if usuario in estudiantes:
        print(f"Bienvenido, {usuario}!")
        print(f"Tu nota final es: {estudiantes[usuario]}")
    else:
        print("Usuario no encontrado. Intente nuevamente.")

def main():
    estudiantes = {
        "juan": 85, 
        "maria": 92,
        "pedro": 78,
        "ana": 88
    }
    
    while True:
        opcion = mostrar_menu()
        if opcion == "1":
            iniciar_sesion(estudiantes)
        elif opcion == "2":
            print("Saliendo del programa. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    main() """


import json

# Funciones para manejar datos
def cargar_datos():
    try:
        with open("estudiantes.json", "r") as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        return {}

def guardar_datos(estudiantes):
    with open("estudiantes.json", "w") as archivo:
        json.dump(estudiantes, archivo)

# Mostrar menú principal
def mostrar_menu():
    print("\n🎓 === Menú Principal === 🎓")
    print("1. Iniciar sesión")
    print("2. Registrar usuario")
    print("3. Salir")
    opcion = input("Seleccione una opción: ")
    return opcion

# Iniciar sesión
def iniciar_sesion(estudiantes):
    usuario = input("Ingrese su nombre de usuario: ")
    if usuario in estudiantes:
        contraseña = input("Ingrese su contraseña: ")
        if estudiantes[usuario]["contraseña"] == contraseña:
            print(f"Bienvenido, {usuario}!")
            print(f"Tu nota final es: {estudiantes[usuario]['nota']}")
        else:
            print("Contraseña incorrecta. Intente nuevamente.")
    else:
        print("Usuario no encontrado. Intente nuevamente.")

# Registrar nuevo usuario
def registrar_usuario(estudiantes):
    usuario = input("Ingrese un nombre de usuario: ")
    if usuario in estudiantes:
        print("El usuario ya existe. Intente con otro nombre.")
    else:
        contraseña = input("Ingrese una contraseña: ")
        nota = int(input("Ingrese la nota del usuario: "))
        estudiantes[usuario] = {"nota": nota, "contraseña": contraseña}
        print(f"Usuario {usuario} registrado exitosamente.")
        guardar_datos(estudiantes)

# Programa principal
def main():
    estudiantes = cargar_datos()
    
    while True:
        opcion = mostrar_menu()
        if opcion == "1":
            iniciar_sesion(estudiantes)
        elif opcion == "2":
            registrar_usuario(estudiantes)
        elif opcion == "3":
            print("Saliendo del programa. ¡Hasta luego!")
            guardar_datos(estudiantes)
            break
        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    main()