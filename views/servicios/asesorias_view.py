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

from services.asesorias_service import (
    crear_asesoria,
    obtener_asesorias,
    eliminar_asesoria,
    agendar_asesoria
)


def menu_asesorias():

    while True:

        print("\n--- Menú de Asesorías Especializadas ---")
        print("1. Agendar Asesoría")
        print("2. Ver Asesorías")
        print("3. Crear Asesoría")
        print("4. Eliminar Asesoría")
        print("5. Volver al menú principal")

        opcion = obtener_opcion(
            "Seleccione una opción: ",
            ["1", "2", "3", "4", "5"]
        )

        if opcion == "1":
            menu_agendar_asesoria()

        elif opcion == "2":
            menu_ver_asesorias()

        elif opcion == "3":
            menu_crear_asesoria()

        elif opcion == "4":
            menu_eliminar_asesoria()

        elif opcion == "5":
            break


def menu_crear_asesoria():

    print("\n--- Crear Asesoría ---")

    try:

        nombre = input(
            "Nombre de la asesoría: "
        ).strip()

        especialista = input(
            "Nombre del especialista: "
        ).strip()

        precio_por_sesion = float(
            input("Precio por sesión: ").strip()
        )

        asesoria = crear_asesoria(
            nombre,
            especialista,
            precio_por_sesion
        )

        mostrar_ok(
            f"Asesoría creada correctamente: "
            f"{asesoria['nombre']}"
        )

        log_success(
            f"Asesoría creada: {asesoria['nombre']}",
            "CREAR_ASESORIA"
        )

    except ValueError as e:

        log_error(str(e), "CREAR_ASESORIA")
        mostrar_error(str(e))

    except Exception as e:

        log_error(str(e), "CREAR_ASESORIA")

        mostrar_error(
            "Ocurrió un error inesperado al crear la asesoría"
        )


def menu_ver_asesorias():

    print("\n--- Lista de Asesorías ---")

    try:

        asesorias = obtener_asesorias()

        if not asesorias:

            mostrar_info(
                "No hay asesorías registradas."
            )

            return

        for i, asesoria in enumerate(asesorias, 1):

            print(
                f"{i}. "
                f"Nombre: {asesoria['nombre']} | "
                f"Especialista: {asesoria['especialista']} | "
                f"Precio/Sesión: ${asesoria['precio_por_sesion']}"
            )

    except Exception as e:

        log_error(str(e), "VER_ASESORIAS")

        mostrar_error(
            "Error al obtener las asesorías"
        )


def menu_eliminar_asesoria():

    print("\n--- Eliminar Asesoría ---")

    try:

        asesorias = obtener_asesorias()

        if not asesorias:

            mostrar_warning(
                "No existen asesorías registradas."
            )

            return

        menu_ver_asesorias()

        indice = input(
            "\nIngrese el número de la asesoría a eliminar: "
        ).strip()

        eliminar_asesoria(int(indice) - 1)

        mostrar_ok(
            "Asesoría eliminada correctamente"
        )

        log_success(
            f"Asesoría eliminada. Índice: {indice}",
            "ELIMINAR_ASESORIA"
        )

    except Exception as e:

        log_error(str(e), "ELIMINAR_ASESORIA")
        mostrar_error(str(e))


def menu_agendar_asesoria():

    print("\n--- Agendar Asesoría ---")

    try:

        asesorias = obtener_asesorias()

        if not asesorias:

            mostrar_warning(
                "No existen asesorías disponibles."
            )

            return

        menu_ver_asesorias()

        indice = input(
            "\nSeleccione el número de la asesoría: "
        ).strip()

        sesiones = input(
            "Cantidad de sesiones: "
        ).strip()

        resultado = agendar_asesoria(
            int(indice) - 1,
            int(sesiones)
        )

        mostrar_ok(
            f"Asesoría agendada correctamente. "
            f"Total: ${resultado['total']}"
        )

        log_success(
            f"Asesoría agendada: {resultado['asesoria']}",
            "AGENDAR_ASESORIA"
        )

    except Exception as e:

        log_error(str(e), "AGENDAR_ASESORIA")
        mostrar_error(str(e))