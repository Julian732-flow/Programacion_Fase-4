from views.menu import mostrar_menu
from views.cliente_view import menu_cliente
from views.servicios_view import menu_servicios

from utils.input_utils import obtener_opcion

def main():
    while True:
        mostrar_menu()
        opcion = obtener_opcion("Seleccione una opción: ", ["1", "2", "3"])
        if opcion == "1":
            menu_cliente()
            pass
        elif opcion == "2":
            menu_servicios()
            pass
        elif opcion == "3":
             print("Saliendo del programa...")
             break

if __name__ == "__main__":
    main()