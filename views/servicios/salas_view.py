from utils.input_utils import obtener_opcion
from utils.logger import log_error, log_success
from utils.mensajes import mostrar_ok, mostrar_error, mostrar_info, mostrar_warning
from services.sala_service import crear_sala, obtener_salas, eliminar_sala, reservar_sala

def menu_salas():
    while True:
        print("\n--- Menú de Salas ---")
        print("1. Reservar Sala")
        print("2. Ver Salas")
        print("3. Crear Sala")
        print("4. Eliminar Sala")
        print("5. Volver al menú principal")

        opcion = obtener_opcion(
            "Seleccione una opción: ",
            ["1", "2", "3", "4", "5"]
        )

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



def menu_crear_sala():
    print("\n--- Crear Sala ---")
    try:
        nombre = input("Nombre de la sala: ").strip()
        capacidad = int(input("Capacidad de personas: ").strip())
        precio_por_hora = float(input("Precio por hora: ").strip())
        sala = crear_sala(
            nombre,
            capacidad,
            precio_por_hora
        )
        mostrar_ok(
            f"Sala creada correctamente: {sala['nombre']}"
        )
        log_success(
            f"Sala creada: {sala['nombre']}",
            "CREAR_SALA"
        )

    except ValueError as e:
        log_error(str(e), "CREAR_SALA")
        mostrar_error(str(e))

    except Exception as e:
        log_error(str(e), "CREAR_SALA")
        mostrar_error("Ocurrió un error inesperado al crear la sala")


def menu_ver_salas():
    print("\n--- Lista de Salas ---")

    try:
        salas = obtener_salas()
        if not salas:
            mostrar_info("No hay salas registradas.")
            return

        for i, sala in enumerate(salas, 1):
            print(
                f"{i}. "
                f"Nombre: {sala['nombre']} | "
                f"Capacidad: {sala['capacidad']} | "
                f"Precio/Hora: ${sala['precio_por_hora']}"
            )
    except Exception as e:
        log_error(str(e), "VER_SALAS")
        mostrar_error("Error al obtener las salas")


def menu_eliminar_sala():
    print("\n--- Eliminar Sala ---")

    try:
        salas = obtener_salas()

        menu_ver_salas()

        indice = input(
            "\nIngrese el número de la sala a eliminar: "
        ).strip()

        eliminar_sala(int(indice) - 1)
        mostrar_ok("Sala eliminada correctamente")
        log_success(f"Sala eliminada. Índice: {indice}","ELIMINAR_SALA")

    except Exception as e:
        log_error(str(e), "ELIMINAR_SALA")
        mostrar_error(str(e))


def menu_reservar_sala():
    print("\n--- Reservar Sala ---")
    try:
        salas = obtener_salas()
        menu_ver_salas()
        indice = input(
            "\nSeleccione el número de la sala: "
        ).strip()

        sala = salas[int(indice) - 1]
        horas = input("Cantidad de horas: ").strip()
        total = int(horas) * sala["precio_por_hora"]

        mostrar_ok(f"Reserva realizada correctamente. " f"Total: ${total}")

        log_success(f"Reserva de sala realizada: {sala['nombre']}","RESERVAR_SALA")

    except Exception as e:
        log_error(str(e), "RESERVAR_SALA")
        mostrar_error(str(e))