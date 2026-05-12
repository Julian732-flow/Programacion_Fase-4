from utils.input_utils import obtener_opcion

# Importa funciones para registrar logs
from utils.logger import (
    log_error,
    log_success
)

# Importa funciones para mostrar mensajes
# en consola al usuario
from utils.mensajes import (
    mostrar_ok,
    mostrar_error,
    mostrar_info,
    mostrar_warning
)

# Importa la lógica de negocio relacionada
# con las asesorías
from services.asesorias_service import (
    crear_asesoria,
    obtener_asesorias,
    eliminar_asesoria,
    agendar_asesoria
)


# Menú principal de asesorías
# Controla la navegación entre opciones
def menu_asesorias():

    while True:

        print("\n--- Menú de Asesorías Especializadas ---")
        print("1. Agendar Asesoría")
        print("2. Ver Asesorías")
        print("3. Crear Asesoría")
        print("4. Eliminar Asesoría")
        print("5. Volver al menú principal")

        # Solicita una opción válida al usuario
        opcion = obtener_opcion(
            "Seleccione una opción: ",
            ["1", "2", "3", "4", "5"]
        )

        # Redirecciona según la opción elegida
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


# Menú para crear una nueva asesoría
def menu_crear_asesoria():

    print("\n--- Crear Asesoría ---")

    try:

        # Solicita datos de la asesoría
        nombre = input(
            "Nombre de la asesoría: "
        ).strip()

        especialista = input(
            "Nombre del especialista: "
        ).strip()

        precio_por_sesion = float(
            input("Precio por sesión: ").strip()
        )

        # Llama al service para crear la asesoría
        asesoria = crear_asesoria(
            nombre,
            especialista,
            precio_por_sesion
        )

        # Muestra mensaje de éxito
        mostrar_ok(
            f"Asesoría creada correctamente: "
            f"{asesoria['nombre']}"
        )

        # Registra el evento en logs
        log_success(
            f"Asesoría creada: {asesoria['nombre']}",
            "CREAR_ASESORIA"
        )

    except ValueError as e:

        # Registra errores de validación
        log_error(str(e), "CREAR_ASESORIA")
        mostrar_error(str(e))

    except Exception as e:

        # Registra errores inesperados
        log_error(str(e), "CREAR_ASESORIA")

        mostrar_error(
            "Ocurrió un error inesperado al crear la asesoría"
        )


# Menú para visualizar las asesorías registradas
def menu_ver_asesorias():

    print("\n--- Lista de Asesorías ---")

    try:

        # Obtiene las asesorías almacenadas
        asesorias = obtener_asesorias()

        # Valida si existen asesorías registradas
        if not asesorias:

            mostrar_info(
                "No hay asesorías registradas."
            )

            return

        # Recorre e imprime cada asesoría
        for i, asesoria in enumerate(asesorias, 1):

            print(
                f"{i}. "
                f"Nombre: {asesoria['nombre']} | "
                f"Especialista: {asesoria['especialista']} | "
                f"Precio/Sesión: ${asesoria['precio_por_sesion']}"
            )

    except Exception as e:

        # Registra errores al obtener asesorías
        log_error(str(e), "VER_ASESORIAS")

        mostrar_error(
            "Error al obtener las asesorías"
        )


# Menú para eliminar una asesoría
def menu_eliminar_asesoria():

    print("\n--- Eliminar Asesoría ---")

    try:

        # Obtiene las asesorías registradas
        asesorias = obtener_asesorias()

        # Valida si existen asesorías
        if not asesorias:

            mostrar_warning(
                "No existen asesorías registradas."
            )

            return

        # Muestra la lista de asesorías
        menu_ver_asesorias()

        # Solicita el índice a eliminar
        indice = input(
            "\nIngrese el número de la asesoría a eliminar: "
        ).strip()

        # Elimina la asesoría seleccionada
        eliminar_asesoria(int(indice) - 1)

        # Muestra mensaje de éxito
        mostrar_ok(
            "Asesoría eliminada correctamente"
        )

        # Registra el evento en logs
        log_success(
            f"Asesoría eliminada. Índice: {indice}",
            "ELIMINAR_ASESORIA"
        )

    except Exception as e:

        # Registra errores del proceso
        log_error(str(e), "ELIMINAR_ASESORIA")
        mostrar_error(str(e))


# Menú para agendar una asesoría
def menu_agendar_asesoria():

    print("\n--- Agendar Asesoría ---")

    try:

        # Obtiene las asesorías registradas
        asesorias = obtener_asesorias()

        # Valida si existen asesorías disponibles
        if not asesorias:

            mostrar_warning(
                "No existen asesorías disponibles."
            )

            return

        # Muestra las asesorías registradas
        menu_ver_asesorias()

        # Solicita la asesoría a seleccionar
        indice = input(
            "\nSeleccione el número de la asesoría: "
        ).strip()

        # Solicita la cantidad de sesiones
        sesiones = input(
            "Cantidad de sesiones: "
        ).strip()

        # Calcula el total del agendamiento
        resultado = agendar_asesoria(
            int(indice) - 1,
            int(sesiones)
        )

        # Muestra mensaje de éxito
        mostrar_ok(
            f"Asesoría agendada correctamente. "
            f"Total: ${resultado['total']}"
        )

        # Registra el evento en logs
        log_success(
            f"Asesoría agendada: {resultado['asesoria']}",
            "AGENDAR_ASESORIA"
        )

    except Exception as e:

        # Registra errores del proceso
        log_error(str(e), "AGENDAR_ASESORIA")
        mostrar_error(str(e))