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
# con las salas
from services.sala_service import (
    crear_sala,
    obtener_salas,
    eliminar_sala,
    reservar_sala
)


# Menú principal de salas
# Permite navegar entre las diferentes opciones
def menu_salas():

    while True:

        print("\n--- Menú de Salas ---")
        print("1. Reservar Sala")
        print("2. Ver Salas")
        print("3. Crear Sala")
        print("4. Eliminar Sala")
        print("5. Volver al menú principal")

        # Solicita una opción válida al usuario
        opcion = obtener_opcion(
            "Seleccione una opción: ",
            ["1", "2", "3", "4", "5"]
        )

        # Redirecciona según la opción seleccionada
        if opcion == "1":
            menu_reservar_sala()

        elif opcion == "2":
            menu_ver_salas()

        elif opcion == "3":
            menu_crear_sala()

        elif opcion == "4":
            menu_eliminar_sala()

        elif opcion == "5":
            break


# Menú para crear una nueva sala
def menu_crear_sala():

    print("\n--- Crear Sala ---")

    try:

        # Solicita los datos de la sala
        nombre = input(
            "Nombre de la sala: "
        ).strip()

        capacidad = int(
            input("Capacidad de personas: ").strip()
        )

        precio_por_hora = float(
            input("Precio por hora: ").strip()
        )

        # Llama al service para crear la sala
        sala = crear_sala(
            nombre,
            capacidad,
            precio_por_hora
        )

        # Muestra mensaje de éxito
        mostrar_ok(
            f"Sala creada correctamente: {sala['nombre']}"
        )

        # Registra el evento en logs
        log_success(
            f"Sala creada: {sala['nombre']}",
            "CREAR_SALA"
        )

    except ValueError as e:

        # Maneja errores de validación
        log_error(str(e), "CREAR_SALA")
        mostrar_error(str(e))

    except Exception as e:

        # Maneja errores inesperados
        log_error(str(e), "CREAR_SALA")

        mostrar_error(
            "Ocurrió un error inesperado al crear la sala"
        )


# Menú para visualizar las salas registradas
def menu_ver_salas():

    print("\n--- Lista de Salas ---")

    try:

        # Obtiene las salas almacenadas
        salas = obtener_salas()

        # Valida si existen salas registradas
        if not salas:

            mostrar_info(
                "No hay salas registradas."
            )

            return

        # Recorre e imprime cada sala
        for i, sala in enumerate(salas, 1):

            print(
                f"{i}. "
                f"Nombre: {sala['nombre']} | "
                f"Capacidad: {sala['capacidad']} | "
                f"Precio/Hora: ${sala['precio_por_hora']}"
            )

    except Exception as e:

        # Registra errores al consultar salas
        log_error(str(e), "VER_SALAS")

        mostrar_error(
            "Error al obtener las salas"
        )


# Menú para eliminar una sala
def menu_eliminar_sala():

    print("\n--- Eliminar Sala ---")

    try:

        # Obtiene las salas registradas
        salas = obtener_salas()

        # Valida si existen salas
        if not salas:

            mostrar_warning(
                "No existen salas registradas."
            )

            return

        # Muestra la lista de salas
        menu_ver_salas()

        # Solicita el número de la sala a eliminar
        indice = input(
            "\nIngrese el número de la sala a eliminar: "
        ).strip()

        # Elimina la sala seleccionada
        eliminar_sala(int(indice) - 1)

        # Muestra mensaje de éxito
        mostrar_ok(
            "Sala eliminada correctamente"
        )

        # Registra el evento en logs
        log_success(
            f"Sala eliminada. Índice: {indice}",
            "ELIMINAR_SALA"
        )

    except Exception as e:

        # Registra errores del proceso
        log_error(str(e), "ELIMINAR_SALA")
        mostrar_error(str(e))


# Menú para reservar una sala
def menu_reservar_sala():

    print("\n--- Reservar Sala ---")

    try:

        # Obtiene las salas registradas
        salas = obtener_salas()

        # Valida si existen salas disponibles
        if not salas:

            mostrar_warning(
                "No existen salas disponibles."
            )

            return

        # Muestra la lista de salas
        menu_ver_salas()

        # Solicita la sala a reservar
        indice = input(
            "\nSeleccione el número de la sala: "
        ).strip()

        # Obtiene la sala seleccionada
        sala = salas[int(indice) - 1]

        # Solicita la cantidad de horas
        horas = input(
            "Cantidad de horas: "
        ).strip()

        # Calcula el costo total de la reserva
        total = int(horas) * sala["precio_por_hora"]

        # Muestra mensaje de éxito
        mostrar_ok(
            f"Reserva realizada correctamente. "
            f"Total: ${total}"
        )

        # Registra el evento en logs
        log_success(
            f"Reserva de sala realizada: {sala['nombre']}",
            "RESERVAR_SALA"
        )

    except Exception as e:

        # Registra errores del proceso
        log_error(str(e), "RESERVAR_SALA")
        mostrar_error(str(e))