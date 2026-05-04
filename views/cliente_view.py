from utils.input_utils import obtener_opcion
from services.cliente_service import crear_cliente, obtener_clientes
from utils.logger import log_error, log_success
from utils.mensajes import mostrar_ok, mostrar_error, mostrar_info

def menu_cliente():
    while True:
        print("\n--- Menú Cliente ---")
        print("1. Crear cliente")
        print("2. Ver clientes")
        print("3. Regresar.")
        opcion = obtener_opcion( "Seleccione una opción: ",["1", "2", "3"])

        if opcion == "1":
            menu_crear_cliente()
        elif opcion == "2":
            menu_ver_clientes()
        elif opcion == "3":
            break

def menu_crear_cliente():
    print("\n--- Crear Cliente ---")

    try:
        nombre = input("Nombre: ").strip()
        email = input("Email: ").strip()
        cliente = crear_cliente(nombre, email)

        mostrar_ok(f"Cliente creado: {cliente.nombre}")
        log_success(f"Cliente creado: {cliente.email}", "CREAR_CLIENTE")

    except Exception as e:
        log_error(str(e), "CREAR_CLIENTE")
        mostrar_error(str(e))


def menu_ver_clientes():
    print("\n--- Lista de Clientes ---")

    try:
        clientes = obtener_clientes()

        if not clientes:
            mostrar_info("No hay clientes registrados.")
            return

        for i, cliente in enumerate(clientes, 1):
            print(f"{i}. {cliente['nombre']} - {cliente['email']}")

    except Exception as e:
        log_error(str(e), "VER_CLIENTES")
        mostrar_error("Error al cargar los clientes")