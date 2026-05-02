from utils.input_utils import obtener_opcion

def menu_equipos():
    print("-- Menú de Equipos")
    print("1. Alquilar Equipo")
    print("2. Ver Equipos")
    print("3. Crear Equipo")
    print("4. Eliminar Equipo")
    print("5. Volver al menú principal")
    
    while True:
        opcion = obtener_opcion("Seleccione una opción: ", ["1", "2", "3", "4", "5"])
        if opcion == "1":
            pass
        elif opcion == "2":
            pass
        elif opcion == "3":
            pass
        elif opcion == "4":
            pass
        elif opcion == "5":
            break   