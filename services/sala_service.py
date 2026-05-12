import json
import os

# Ruta del archivo JSON donde se almacenan
# las salas registradas
RUTA_SALAS = "data/salas.json"


def _leer_salas():
    """
    Lee las salas almacenadas en el archivo JSON.
    """

    # Verifica si el archivo existe
    if not os.path.exists(RUTA_SALAS):
        return []

    # Abre el archivo en modo lectura
    with open(RUTA_SALAS, "r") as file:
        try:

            # Convierte el contenido JSON a lista de Python
            return json.load(file)

        except json.JSONDecodeError:

            # Retorna lista vacía si el JSON está vacío
            # o tiene formato inválido
            return []


def _guardar_salas(salas):
    """
    Guarda la lista de salas en el archivo JSON.
    """

    # Abre el archivo en modo escritura
    with open(RUTA_SALAS, "w") as file:

        # Guarda la información en formato JSON
        # con indentación para mejor lectura
        json.dump(salas, file, indent=4)


def crear_sala(nombre, capacidad, precio_por_hora):
    """
    Crea y guarda una nueva sala.
    """

    # =========================
    # Validaciones
    # =========================

    # Valida que el nombre no esté vacío
    if not nombre or not nombre.strip():
        raise ValueError(
            "El nombre de la sala no puede estar vacío"
        )

    # Valida que la capacidad sea mayor a 0
    if capacidad <= 0:
        raise ValueError(
            "La capacidad debe ser mayor a 0"
        )

    # Valida que el precio por hora sea mayor a 0
    if precio_por_hora <= 0:
        raise ValueError(
            "El precio por hora debe ser mayor a 0"
        )

    # Obtiene las salas registradas
    salas = _leer_salas()

    # =========================
    # Validar nombres duplicados
    # =========================

    for sala in salas:

        # Compara nombres ignorando mayúsculas/minúsculas
        if sala["nombre"].lower() == nombre.lower():

            raise ValueError(
                "Ya existe una sala con ese nombre"
            )

    # Crea el diccionario de la nueva sala
    nueva_sala = {
        "nombre": nombre.strip(),
        "capacidad": capacidad,
        "precio_por_hora": precio_por_hora
    }

    # Agrega la nueva sala a la lista
    salas.append(nueva_sala)

    # Guarda los cambios en el archivo JSON
    _guardar_salas(salas)

    # Retorna la sala creada
    return nueva_sala


def obtener_salas():
    """
    Retorna todas las salas registradas.
    """

    # Retorna las salas almacenadas
    return _leer_salas()


def eliminar_sala(indice):
    """
    Elimina una sala según su índice.
    """

    # Obtiene las salas registradas
    salas = _leer_salas()

    # Valida que existan salas
    if not salas:
        raise ValueError(
            "No existen salas registradas"
        )

    # Valida que el índice exista
    if indice < 0 or indice >= len(salas):
        raise ValueError(
            "La sala seleccionada no existe"
        )

    # Elimina la sala seleccionada
    salas.pop(indice)

    # Guarda los cambios en el archivo JSON
    _guardar_salas(salas)


def reservar_sala(indice, horas):
    """
    Calcula el costo de una reserva de sala.
    """

    # Obtiene las salas registradas
    salas = _leer_salas()

    # Valida que existan salas
    if not salas:
        raise ValueError(
            "No existen salas registradas"
        )

    # Valida que el índice exista
    if indice < 0 or indice >= len(salas):
        raise ValueError(
            "La sala seleccionada no existe"
        )

    # Valida que las horas sean mayores a 0
    if horas <= 0:
        raise ValueError(
            "Las horas deben ser mayores a 0"
        )

    # Obtiene la sala seleccionada
    sala = salas[indice]

    # Calcula el costo total de la reserva
    total = horas * sala["precio_por_hora"]

    # Retorna la información de la reserva
    return {
        "sala": sala["nombre"],
        "horas": horas,
        "total": total
    }