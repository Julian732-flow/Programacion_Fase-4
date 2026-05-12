import json
import os

RUTA_ASESORIAS = "data/asesorias.json"


def _leer_asesorias():
    """
    Lee las asesorías almacenadas en el archivo JSON.
    """

    if not os.path.exists(RUTA_ASESORIAS):
        return []

    with open(RUTA_ASESORIAS, "r") as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return []


def _guardar_asesorias(asesorias):
    """
    Guarda la lista de asesorías en el archivo JSON.
    """

    with open(RUTA_ASESORIAS, "w") as file:
        json.dump(asesorias, file, indent=4)


def crear_asesoria(nombre, especialista, precio_por_sesion):
    """
    Crea y guarda una nueva asesoría.
    """

    # Validaciones

    if not nombre or not nombre.strip():
        raise ValueError(
            "El nombre de la asesoría no puede estar vacío"
        )

    if not especialista or not especialista.strip():
        raise ValueError(
            "El nombre del especialista no puede estar vacío"
        )

    if precio_por_sesion <= 0:
        raise ValueError(
            "El precio por sesión debe ser mayor a 0"
        )

    asesorias = _leer_asesorias()

    # Validar nombres duplicados

    for asesoria in asesorias:

        if asesoria["nombre"].lower() == nombre.lower():

            raise ValueError(
                "Ya existe una asesoría con ese nombre"
            )

    nueva_asesoria = {
        "nombre": nombre.strip(),
        "especialista": especialista.strip(),
        "precio_por_sesion": precio_por_sesion
    }

    asesorias.append(nueva_asesoria)

    _guardar_asesorias(asesorias)

    return nueva_asesoria


def obtener_asesorias():
    """
    Retorna todas las asesorías registradas.
    """

    return _leer_asesorias()


def eliminar_asesoria(indice):
    """
    Elimina una asesoría según su índice.
    """

    asesorias = _leer_asesorias()

    if not asesorias:
        raise ValueError(
            "No existen asesorías registradas"
        )

    if indice < 0 or indice >= len(asesorias):
        raise ValueError(
            "La asesoría seleccionada no existe"
        )

    asesorias.pop(indice)

    _guardar_asesorias(asesorias)


def agendar_asesoria(indice, sesiones):
    """
    Calcula el costo de una asesoría.
    """

    asesorias = _leer_asesorias()

    if not asesorias:
        raise ValueError(
            "No existen asesorías registradas"
        )

    if indice < 0 or indice >= len(asesorias):
        raise ValueError(
            "La asesoría seleccionada no existe"
        )

    if sesiones <= 0:
        raise ValueError(
            "Las sesiones deben ser mayores a 0"
        )

    asesoria = asesorias[indice]

    total = sesiones * asesoria["precio_por_sesion"]

    return {
        "asesoria": asesoria["nombre"],
        "sesiones": sesiones,
        "total": total
    }