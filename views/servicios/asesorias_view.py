from utils.input_utils import obtener_opcion

def menu_asesorias():
    print("-- Menú de Asesorías Especializadas")
    print("1. Agendar Asesoría")
    print("2. Ver Asesorías")
    print("3. Crear Asesorías")
    print("4. Eliminar Asesorías")
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