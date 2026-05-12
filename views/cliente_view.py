from utils.input_utils import obtener_opcion

# Importa la lógica de negocio relacionada
# con los clientes
from services.cliente_service import (
    crear_cliente,
    obtener_clientes
)

# Importa funciones para registrar logs
from utils.logger import (
    log_error,
    log_success
)

# Importa funciones para mostrar mensajes
# informativos en consola
from utils.mensajes import (
    mostrar_ok,
    mostrar_error,
    mostrar_info
)


# Menú principal de clientes
# Permite navegar entre las diferentes opciones
def menu_cliente():

    while True:

        print("\n--- Menú Cliente ---")
        print("1. Crear cliente")
        print("2. Ver clientes")
        print("3. Regresar.")

        # Solicita una opción válida al usuario
        opcion = obtener_opcion(
            "Seleccione una opción: ",
            ["1", "2", "3"]
        )

        # Redirecciona según la opción seleccionada
        if opcion == "1":
            menu_crear_cliente()

        elif opcion == "2":
            menu_ver_clientes()

        elif opcion == "3":
            break


# Menú para crear un nuevo cliente
def menu_crear_cliente():

    print("\n--- Crear Cliente ---")

    try:

        # Solicita los datos del cliente
        nombre = input("Nombre: ").strip()
        email = input("Email: ").strip()

        # Llama al service para crear el cliente
        cliente = crear_cliente(nombre, email)

        # Muestra mensaje de éxito
        mostrar_ok(
            f"Cliente creado: {cliente.nombre}"
        )

        # Registra el evento en logs
        log_success(
            f"Cliente creado: {cliente.email}",
            "CREAR_CLIENTE"
        )

    except Exception as e:

        # Registra errores del proceso
        log_error(str(e), "CREAR_CLIENTE")
        mostrar_error(str(e))


# Menú para visualizar los clientes registrados
def menu_ver_clientes():

    print("\n--- Lista de Clientes ---")

    try:

        # Obtiene los clientes almacenados
        clientes = obtener_clientes()

        # Valida si existen clientes registrados
        if not clientes:

            mostrar_info(
                "No hay clientes registrados."
            )

            return

        # Recorre e imprime cada cliente
        for i, cliente in enumerate(clientes, 1):

            print(
                f"{i}. "
                f"{cliente['nombre']} - "
                f"{cliente['email']}"
            )

    except Exception as e:

        # Registra errores al consultar clientes
        log_error(str(e), "VER_CLIENTES")

        mostrar_error(
            "Error al cargar los clientes"
        )