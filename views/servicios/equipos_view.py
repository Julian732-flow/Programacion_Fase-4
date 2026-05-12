from utils.input_utils import obtener_opcion

from utils.logger import (
    log_error,
    log_success
)

from utils.mensajes import (
    mostrar_ok,
    mostrar_error,
    mostrar_info,
    mostrar_warning
)

from services.equipos_service import (
    crear_equipo,
    obtener_equipos,
    eliminar_equipo,
    alquilar_equipo
)


def menu_equipos():

    while True:

        print("\n--- Menú de Equipos ---")
        print("1. Alquilar Equipo")
        print("2. Ver Equipos")
        print("3. Crear Equipo")
        print("4. Eliminar Equipo")
        print("5. Volver al menú principal")

        opcion = obtener_opcion(
            "Seleccione una opción: ",
            ["1", "2", "3", "4", "5"]
        )

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


def menu_crear_equipo():

    print("\n--- Crear Equipo ---")

    try:

        nombre = input(
            "Nombre del equipo: "
        ).strip()

        tipo = input(
            "Tipo de equipo: "
        ).strip()

        precio_por_dia = float(
            input("Precio por día: ").strip()
        )

        equipo = crear_equipo(
            nombre,
            tipo,
            precio_por_dia
        )

        mostrar_ok(
            f"Equipo creado correctamente: "
            f"{equipo['nombre']}"
        )

        log_success(
            f"Equipo creado: {equipo['nombre']}",
            "CREAR_EQUIPO"
        )

    except ValueError as e:

        log_error(str(e), "CREAR_EQUIPO")
        mostrar_error(str(e))

    except Exception as e:

        log_error(str(e), "CREAR_EQUIPO")

        mostrar_error(
            "Ocurrió un error inesperado al crear el equipo"
        )


def menu_ver_equipos():

    print("\n--- Lista de Equipos ---")

    try:

        equipos = obtener_equipos()

        if not equipos:
            mostrar_info(
                "No hay equipos registrados."
            )
            return

        for i, equipo in enumerate(equipos, 1):

            print(
                f"{i}. "
                f"Nombre: {equipo['nombre']} | "
                f"Tipo: {equipo['tipo']} | "
                f"Precio/Día: ${equipo['precio_por_dia']}"
            )

    except Exception as e:

        log_error(str(e), "VER_EQUIPOS")

        mostrar_error(
            "Error al obtener los equipos"
        )


def menu_eliminar_equipo():

    print("\n--- Eliminar Equipo ---")

    try:

        equipos = obtener_equipos()

        if not equipos:

            mostrar_warning(
                "No existen equipos registrados."
            )

            return

        menu_ver_equipos()

        indice = input(
            "\nIngrese el número del equipo a eliminar: "
        ).strip()

        eliminar_equipo(int(indice) - 1)

        mostrar_ok(
            "Equipo eliminado correctamente"
        )

        log_success(
            f"Equipo eliminado. Índice: {indice}",
            "ELIMINAR_EQUIPO"
        )

    except Exception as e:

        log_error(str(e), "ELIMINAR_EQUIPO")
        mostrar_error(str(e))


def menu_alquilar_equipo():

    print("\n--- Alquilar Equipo ---")

    try:

        equipos = obtener_equipos()

        if not equipos:

            mostrar_warning(
                "No existen equipos disponibles."
            )

            return

        menu_ver_equipos()

        indice = input(
            "\nSeleccione el número del equipo: "
        ).strip()

        dias = input(
            "Cantidad de días: "
        ).strip()

        resultado = alquilar_equipo(
            int(indice) - 1,
            int(dias)
        )

        mostrar_ok(
            f"Alquiler realizado correctamente. "
            f"Total: ${resultado['total']}"
        )

        log_success(
            f"Alquiler realizado: {resultado['equipo']}",
            "ALQUILAR_EQUIPO"
        )

    except Exception as e:

        log_error(str(e), "ALQUILAR_EQUIPO")
        mostrar_error(str(e))