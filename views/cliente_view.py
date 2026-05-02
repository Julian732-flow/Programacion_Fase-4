from utils.input_utils import obtener_opcion

def menu_cliente():
    while True:
        print("\n--- Menú Cliente ---")
        print("1. Crear cliente")
        print("2. Ver clientes")
        print("3. Regresar.")
        opcion = obtener_opcion( "Seleccione una opción: ",["1", "2", "3"])

        if opcion == "1":
            menu_crear_cliente()
            pass
        elif opcion == "2":
            menu_ver_clientes()
            pass
        elif opcion == "3":
            break
        
        
def menu_crear_cliente():
    print("\n--- Crear Cliente ---")
    # Aquí se implementaría la lógica para crear un cliente (pendiente de implementación)
    return

def menu_ver_clientes():
    print("\n--- Lista de Clientes ---")
    # Aquí se mostrarían los clientes registrados (pendiente de implementación) 
    return

