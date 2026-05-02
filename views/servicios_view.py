from utils.input_utils import obtener_opcion

from views.servicios.salas_view import menu_salas
from views.servicios.equipos_view import menu_equipos
from views.servicios.asesorias_view import menu_asesorias

def menu_servicios():
    while True:
        print("\n--- Menú Servicios ---")
        print("1. Reserva de Salas")
        print("2. Alquiler de Equipos")
        print("3. Asesorías Especializadas")
        print("4. Regresar.")
        opcion = obtener_opcion( "Seleccione una opción: ",["1", "2", "3", "4"])

        if opcion == "1":
            menu_salas()
            pass
        elif opcion == "2":
            menu_equipos()
            pass
        elif opcion == "3":
            menu_asesorias()
            pass
        elif opcion == "4": 
            break