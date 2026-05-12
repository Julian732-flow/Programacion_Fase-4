import json
import os

RUTA_EQUIPOS = "data/equipos.json"

def _leer_equipos():
    """
    Lee los equipos almacenados en el archivo JSON.
    """

    if not os.path.exists(RUTA_EQUIPOS):
        return []

    with open(RUTA_EQUIPOS, "r") as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return []


def _guardar_equipos(equipos):
    """
    Guarda la lista de equipos en el archivo JSON.
    """

    with open(RUTA_EQUIPOS, "w") as file:
        json.dump(equipos, file, indent=4)


def crear_equipo(nombre, tipo, precio_por_dia):
    """
    Crea y guarda un nuevo equipo.
    """

    # Validaciones
    if not nombre or not nombre.strip():
        raise ValueError(
            "El nombre del equipo no puede estar vacío"
        )

    if not tipo or not tipo.strip():
        raise ValueError(
            "El tipo de equipo no puede estar vacío"
        )

    if precio_por_dia <= 0:
        raise ValueError(
            "El precio por día debe ser mayor a 0"
        )

    equipos = _leer_equipos()

    # Validar nombres duplicados

    for equipo in equipos:

        if equipo["nombre"].lower() == nombre.lower():

            raise ValueError(
                "Ya existe un equipo con ese nombre"
            )

    nuevo_equipo = {
        "nombre": nombre.strip(),
        "tipo": tipo.strip(),
        "precio_por_dia": precio_por_dia
    }

    equipos.append(nuevo_equipo)

    _guardar_equipos(equipos)

    return nuevo_equipo


def obtener_equipos():
    """
    Retorna todos los equipos registrados.
    """

    return _leer_equipos()


def eliminar_equipo(indice):
    """
    Elimina un equipo según su índice.
    """

    equipos = _leer_equipos()

    if not equipos:
        raise ValueError(
            "No existen equipos registrados"
        )

    if indice < 0 or indice >= len(equipos):
        raise ValueError(
            "El equipo seleccionado no existe"
        )

    equipos.pop(indice)

    _guardar_equipos(equipos)


def alquilar_equipo(indice, dias):
    """
    Calcula el costo del alquiler de un equipo.
    """

    equipos = _leer_equipos()

    if not equipos:
        raise ValueError(
            "No existen equipos registrados"
        )

    if indice < 0 or indice >= len(equipos):
        raise ValueError(
            "El equipo seleccionado no existe"
        )

    if dias <= 0:
        raise ValueError(
            "Los días deben ser mayores a 0"
        )

    equipo = equipos[indice]

    total = dias * equipo["precio_por_dia"]

    return {
        "equipo": equipo["nombre"],
        "dias": dias,
        "total": total
    }