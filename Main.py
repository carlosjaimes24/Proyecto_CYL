# Main.py

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
    main()