from utils.input_utils import obtener_opcion

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
    mostrar_info,
    mostrar_warning
)

# Importa la lógica de negocio relacionada
# con los equipos
from services.equipos_service import (
    crear_equipo,
    obtener_equipos,
    eliminar_equipo,
    alquilar_equipo
)


# Menú principal de equipos
# Permite navegar entre las diferentes opciones
def menu_equipos():

    while True:

        print("\n--- Menú de Equipos ---")
        print("1. Alquilar Equipo")
        print("2. Ver Equipos")
        print("3. Crear Equipo")
        print("4. Eliminar Equipo")
        print("5. Volver al menú principal")

        # Solicita una opción válida al usuario
        opcion = obtener_opcion(
            "Seleccione una opción: ",
            ["1", "2", "3", "4", "5"]
        )

        # Redirecciona según la opción seleccionada
        if opcion == "1":
            menu_alquilar_equipo()

        elif opcion == "2":
            menu_ver_equipos()

        elif opcion == "3":
            menu_crear_equipo()

        elif opcion == "4":
            menu_eliminar_equipo()

        elif opcion == "5":
            break


# Menú para crear un nuevo equipo
def menu_crear_equipo():

    print("\n--- Crear Equipo ---")

    try:

        # Solicita los datos del equipo
        nombre = input(
            "Nombre del equipo: "
        ).strip()

        tipo = input(
            "Tipo de equipo: "
        ).strip()

        precio_por_dia = float(
            input("Precio por día: ").strip()
        )

        # Llama al service para crear el equipo
        equipo = crear_equipo(
            nombre,
            tipo,
            precio_por_dia
        )

        # Muestra mensaje de éxito
        mostrar_ok(
            f"Equipo creado correctamente: "
            f"{equipo['nombre']}"
        )

        # Registra el evento en logs
        log_success(
            f"Equipo creado: {equipo['nombre']}",
            "CREAR_EQUIPO"
        )

    except ValueError as e:

        # Maneja errores de validación
        log_error(str(e), "CREAR_EQUIPO")
        mostrar_error(str(e))

    except Exception as e:

        # Maneja errores inesperados
        log_error(str(e), "CREAR_EQUIPO")

        mostrar_error(
            "Ocurrió un error inesperado al crear el equipo"
        )


# Menú para visualizar los equipos registrados
def menu_ver_equipos():

    print("\n--- Lista de Equipos ---")

    try:

        # Obtiene los equipos almacenados
        equipos = obtener_equipos()

        # Valida si existen equipos registrados
        if not equipos:

            mostrar_info(
                "No hay equipos registrados."
            )

            return

        # Recorre e imprime cada equipo
        for i, equipo in enumerate(equipos, 1):

            print(
                f"{i}. "
                f"Nombre: {equipo['nombre']} | "
                f"Tipo: {equipo['tipo']} | "
                f"Precio/Día: ${equipo['precio_por_dia']}"
            )

    except Exception as e:

        # Registra errores al consultar equipos
        log_error(str(e), "VER_EQUIPOS")

        mostrar_error(
            "Error al obtener los equipos"
        )


# Menú para eliminar un equipo
def menu_eliminar_equipo():

    print("\n--- Eliminar Equipo ---")

    try:

        # Obtiene los equipos registrados
        equipos = obtener_equipos()

        # Valida si existen equipos
        if not equipos:

            mostrar_warning(
                "No existen equipos registrados."
            )

            return

        # Muestra la lista de equipos
        menu_ver_equipos()

        # Solicita el número del equipo a eliminar
        indice = input(
            "\nIngrese el número del equipo a eliminar: "
        ).strip()

        # Elimina el equipo seleccionado
        eliminar_equipo(int(indice) - 1)

        # Muestra mensaje de éxito
        mostrar_ok(
            "Equipo eliminado correctamente"
        )

        # Registra el evento en logs
        log_success(
            f"Equipo eliminado. Índice: {indice}",
            "ELIMINAR_EQUIPO"
        )

    except Exception as e:

        # Registra errores del proceso
        log_error(str(e), "ELIMINAR_EQUIPO")
        mostrar_error(str(e))


# Menú para alquilar un equipo
def menu_alquilar_equipo():

    print("\n--- Alquilar Equipo ---")

    try:

        # Obtiene los equipos registrados
        equipos = obtener_equipos()

        # Valida si existen equipos disponibles
        if not equipos:

            mostrar_warning(
                "No existen equipos disponibles."
            )

            return

        # Muestra la lista de equipos
        menu_ver_equipos()

        # Solicita el equipo a alquilar
        indice = input(
            "\nSeleccione el número del equipo: "
        ).strip()

        # Solicita la cantidad de días
        dias = input(
            "Cantidad de días: "
        ).strip()

        # Calcula el total del alquiler
        resultado = alquilar_equipo(
            int(indice) - 1,
            int(dias)
        )

        # Muestra mensaje de éxito
        mostrar_ok(
            f"Alquiler realizado correctamente. "
            f"Total: ${resultado['total']}"
        )

        # Registra el evento en logs
        log_success(
            f"Alquiler realizado: {resultado['equipo']}",
            "ALQUILAR_EQUIPO"
        )

    except Exception as e:

        # Registra errores del proceso
        log_error(str(e), "ALQUILAR_EQUIPO")
        mostrar_error(str(e))