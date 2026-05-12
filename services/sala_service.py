import json
import os

RUTA_SALAS = "data/salas.json"


def _leer_salas():
    """
    Lee las salas almacenadas en el archivo JSON.
    """
    if not os.path.exists(RUTA_SALAS):
        return []

    with open(RUTA_SALAS, "r") as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return []


def _guardar_salas(salas):
    """
    Guarda la lista de salas en el archivo JSON.
    """

    with open(RUTA_SALAS, "w") as file:
        json.dump(salas, file, indent=4)


def crear_sala(nombre, capacidad, precio_por_hora):
    """
    Crea y guarda una nueva sala.
    """

    # Validaciones

    if not nombre or not nombre.strip():
        raise ValueError(
            "El nombre de la sala no puede estar vacío"
        )

    if capacidad <= 0:
        raise ValueError(
            "La capacidad debe ser mayor a 0"
        )

    if precio_por_hora <= 0:
        raise ValueError(
            "El precio por hora debe ser mayor a 0"
        )

    salas = _leer_salas()

    # Validar nombres duplicados

    for sala in salas:
        if sala["nombre"].lower() == nombre.lower():
            raise ValueError(
                "Ya existe una sala con ese nombre"
            )

    nueva_sala = {
        "nombre": nombre.strip(),
        "capacidad": capacidad,
        "precio_por_hora": precio_por_hora
    }

    salas.append(nueva_sala)

    _guardar_salas(salas)

    return nueva_sala


def obtener_salas():
    """
    Retorna todas las salas registradas.
    """
    return _leer_salas()


def eliminar_sala(indice):
    """
    Elimina una sala según su índice.
    """

    salas = _leer_salas()

    if not salas:
        raise ValueError(
            "No existen salas registradas"
        )

    if indice < 0 or indice >= len(salas):
        raise ValueError(
            "La sala seleccionada no existe"
        )

    salas.pop(indice)

    _guardar_salas(salas)


def reservar_sala(indice, horas):
    """
    Calcula el costo de una reserva de sala.
    """

    salas = _leer_salas()

    if not salas:
        raise ValueError(
            "No existen salas registradas"
        )

    if indice < 0 or indice >= len(salas):
        raise ValueError(
            "La sala seleccionada no existe"
        )

    if horas <= 0:
        raise ValueError(
            "Las horas deben ser mayores a 0"
        )

    sala = salas[indice]

    total = horas * sala["precio_por_hora"]

    return {
        "sala": sala["nombre"],
        "horas": horas,
        "total": total
    }