from utils.input_utils import obtener_opcion

def menu_salas():
    print("-- Menú de Salas")
    print("1. Reservar Sala")
    print("2. Ver Salas")
    print("3. Crear Sala")
    print("4. Eliminar Sala")
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