import json
import os

# Ruta del archivo JSON donde se almacenan
# los equipos registrados
RUTA_EQUIPOS = "data/equipos.json"


def _leer_equipos():
    """
    Lee los equipos almacenados en el archivo JSON.
    """

    # Verifica si el archivo existe
    if not os.path.exists(RUTA_EQUIPOS):
        return []

    # Abre el archivo en modo lectura
    with open(RUTA_EQUIPOS, "r") as file:
        try:

            # Convierte el contenido JSON a lista de Python
            return json.load(file)

        except json.JSONDecodeError:

            # Retorna lista vacía si el JSON está vacío
            # o tiene formato inválido
            return []


def _guardar_equipos(equipos):
    """
    Guarda la lista de equipos en el archivo JSON.
    """

    # Abre el archivo en modo escritura
    with open(RUTA_EQUIPOS, "w") as file:

        # Guarda la información en formato JSON
        # con indentación para mejor lectura
        json.dump(equipos, file, indent=4)


def crear_equipo(nombre, tipo, precio_por_dia):
    """
    Crea y guarda un nuevo equipo.
    """

    # =========================
    # Validaciones
    # =========================

    # Valida que el nombre no esté vacío
    if not nombre or not nombre.strip():
        raise ValueError(
            "El nombre del equipo no puede estar vacío"
        )

    # Valida que el tipo no esté vacío
    if not tipo or not tipo.strip():
        raise ValueError(
            "El tipo de equipo no puede estar vacío"
        )

    # Valida que el precio sea mayor a 0
    if precio_por_dia <= 0:
        raise ValueError(
            "El precio por día debe ser mayor a 0"
        )

    # Obtiene los equipos registrados
    equipos = _leer_equipos()

    # =========================
    # Validar nombres duplicados
    # =========================

    for equipo in equipos:

        # Compara nombres ignorando mayúsculas/minúsculas
        if equipo["nombre"].lower() == nombre.lower():

            raise ValueError(
                "Ya existe un equipo con ese nombre"
            )

    # Crea el diccionario del nuevo equipo
    nuevo_equipo = {
        "nombre": nombre.strip(),
        "tipo": tipo.strip(),
        "precio_por_dia": precio_por_dia
    }

    # Agrega el nuevo equipo a la lista
    equipos.append(nuevo_equipo)

    # Guarda los cambios en el archivo JSON
    _guardar_equipos(equipos)

    # Retorna el equipo creado
    return nuevo_equipo


def obtener_equipos():
    """
    Retorna todos los equipos registrados.
    """

    # Retorna los equipos almacenados
    return _leer_equipos()


def eliminar_equipo(indice):
    """
    Elimina un equipo según su índice.
    """

    # Obtiene los equipos registrados
    equipos = _leer_equipos()

    # Valida que existan equipos
    if not equipos:
        raise ValueError(
            "No existen equipos registrados"
        )

    # Valida que el índice exista
    if indice < 0 or indice >= len(equipos):
        raise ValueError(
            "El equipo seleccionado no existe"
        )

    # Elimina el equipo seleccionado
    equipos.pop(indice)

    # Guarda los cambios en el archivo JSON
    _guardar_equipos(equipos)


def alquilar_equipo(indice, dias):
    """
    Calcula el costo del alquiler de un equipo.
    """

    # Obtiene los equipos registrados
    equipos = _leer_equipos()

    # Valida que existan equipos
    if not equipos:
        raise ValueError(
            "No existen equipos registrados"
        )

    # Valida que el índice exista
    if indice < 0 or indice >= len(equipos):
        raise ValueError(
            "El equipo seleccionado no existe"
        )

    # Valida que los días sean mayores a 0
    if dias <= 0:
        raise ValueError(
            "Los días deben ser mayores a 0"
        )

    # Obtiene el equipo seleccionado
    equipo = equipos[indice]

    # Calcula el costo total del alquiler
    total = dias * equipo["precio_por_dia"]

    # Retorna la información del alquiler
    return {
        "equipo": equipo["nombre"],
        "dias": dias,
        "total": total
    }