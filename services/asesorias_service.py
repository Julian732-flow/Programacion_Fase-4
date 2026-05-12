import json
import os

# Ruta del archivo JSON donde se almacenan
# las asesorías registradas
RUTA_ASESORIAS = "data/asesorias.json"


def _leer_asesorias():
    """
    Lee las asesorías almacenadas en el archivo JSON.
    """

    # Verifica si el archivo existe
    if not os.path.exists(RUTA_ASESORIAS):
        return []

    # Abre el archivo en modo lectura
    with open(RUTA_ASESORIAS, "r") as file:
        try:

            # Convierte el contenido JSON a lista de Python
            return json.load(file)

        except json.JSONDecodeError:

            # Retorna lista vacía si el JSON está vacío
            # o tiene formato inválido
            return []


def _guardar_asesorias(asesorias):
    """
    Guarda la lista de asesorías en el archivo JSON.
    """

    # Abre el archivo en modo escritura
    with open(RUTA_ASESORIAS, "w") as file:

        # Guarda la información en formato JSON
        # con indentación para mejor lectura
        json.dump(asesorias, file, indent=4)


def crear_asesoria(nombre, especialista, precio_por_sesion):
    """
    Crea y guarda una nueva asesoría.
    """

    # =========================
    # Validaciones
    # =========================

    # Valida que el nombre no esté vacío
    if not nombre or not nombre.strip():
        raise ValueError(
            "El nombre de la asesoría no puede estar vacío"
        )

    # Valida que el especialista no esté vacío
    if not especialista or not especialista.strip():
        raise ValueError(
            "El nombre del especialista no puede estar vacío"
        )

    # Valida que el precio sea mayor a 0
    if precio_por_sesion <= 0:
        raise ValueError(
            "El precio por sesión debe ser mayor a 0"
        )

    # Obtiene las asesorías existentes
    asesorias = _leer_asesorias()

    # =========================
    # Validar nombres duplicados
    # =========================

    for asesoria in asesorias:

        # Compara nombres ignorando mayúsculas/minúsculas
        if asesoria["nombre"].lower() == nombre.lower():

            raise ValueError(
                "Ya existe una asesoría con ese nombre"
            )

    # Crea el diccionario de la nueva asesoría
    nueva_asesoria = {
        "nombre": nombre.strip(),
        "especialista": especialista.strip(),
        "precio_por_sesion": precio_por_sesion
    }

    # Agrega la nueva asesoría a la lista
    asesorias.append(nueva_asesoria)

    # Guarda los cambios en el archivo JSON
    _guardar_asesorias(asesorias)

    # Retorna la asesoría creada
    return nueva_asesoria


def obtener_asesorias():
    """
    Retorna todas las asesorías registradas.
    """

    # Retorna las asesorías almacenadas
    return _leer_asesorias()


def eliminar_asesoria(indice):
    """
    Elimina una asesoría según su índice.
    """

    # Obtiene las asesorías registradas
    asesorias = _leer_asesorias()

    # Valida que existan asesorías
    if not asesorias:
        raise ValueError(
            "No existen asesorías registradas"
        )

    # Valida que el índice exista
    if indice < 0 or indice >= len(asesorias):
        raise ValueError(
            "La asesoría seleccionada no existe"
        )

    # Elimina la asesoría seleccionada
    asesorias.pop(indice)

    # Guarda los cambios en el archivo JSON
    _guardar_asesorias(asesorias)


def agendar_asesoria(indice, sesiones):
    """
    Calcula el costo de una asesoría.
    """

    # Obtiene las asesorías registradas
    asesorias = _leer_asesorias()

    # Valida que existan asesorías
    if not asesorias:
        raise ValueError(
            "No existen asesorías registradas"
        )

    # Valida que el índice exista
    if indice < 0 or indice >= len(asesorias):
        raise ValueError(
            "La asesoría seleccionada no existe"
        )

    # Valida que las sesiones sean mayores a 0
    if sesiones <= 0:
        raise ValueError(
            "Las sesiones deben ser mayores a 0"
        )

    # Obtiene la asesoría seleccionada
    asesoria = asesorias[indice]

    # Calcula el costo total
    total = sesiones * asesoria["precio_por_sesion"]

    # Retorna la información del agendamiento
    return {
        "asesoria": asesoria["nombre"],
        "sesiones": sesiones,
        "total": total
    }