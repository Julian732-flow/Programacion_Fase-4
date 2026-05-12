import json
import os
import re

# Importa el modelo Cliente
from models.cliente import Cliente

# Ruta del archivo JSON donde se almacenan
# los clientes registrados
RUTA_CLIENTES = "data/clientes.json"


def _leer_clientes():

    # Verifica si el archivo existe
    if not os.path.exists(RUTA_CLIENTES):
        return []

    # Abre el archivo en modo lectura
    with open(RUTA_CLIENTES, "r") as file:
        try:

            # Convierte el contenido JSON a lista de Python
            return json.load(file)

        except json.JSONDecodeError:

            # Retorna lista vacía si el JSON está vacío
            # o tiene formato inválido
            return []


def _guardar_clientes(clientes):

    # Abre el archivo en modo escritura
    with open(RUTA_CLIENTES, "w") as file:

        # Guarda la información en formato JSON
        # con indentación para mejor lectura
        json.dump(clientes, file, indent=4)



def crear_cliente(nombre, email):
    """
    Crea y guarda un cliente en clientes.json
    """

    # =========================
    # Validaciones de nombre
    # =========================

    # Valida que el nombre no esté vacío
    if not nombre or not nombre.strip():
        raise ValueError("El nombre no puede estar vacío")

    # Elimina espacios innecesarios
    nombre = nombre.strip()

    # Valida longitud mínima del nombre
    if len(nombre) < 3:
        raise ValueError("El nombre debe tener al menos 3 caracteres")

    # Valida longitud máxima del nombre
    if len(nombre) > 50:
        raise ValueError("El nombre no puede superar los 50 caracteres")

    # Valida que solo existan letras y espacios
    if not all(c.isalpha() or c.isspace()for c in nombre):

        raise ValueError(
            "El nombre solo puede contener letras y espacios"
        )

    # =========================
    # Validaciones de email
    # =========================

    # Valida que el email no esté vacío
    if not email or not email.strip():
        raise ValueError("El email no puede estar vacío")

    # Limpia espacios y convierte a minúsculas
    email = email.strip().lower()

    # Expresión regular para validar email
    patron_email = r"^[\w\.-]+@[\w\.-]+\.\w+$"

    # Valida formato del email
    if not re.match(patron_email, email):

        raise ValueError("El email no tiene un formato válido")

    # Valida longitud máxima del email
    if len(email) > 100:
        raise ValueError("El email es demasiado largo")

    # Obtiene los clientes registrados
    clientes = _leer_clientes()

    # =========================
    # Validar email duplicado
    # =========================

    for cliente_existente in clientes:

        # Compara emails ignorando mayúsculas/minúsculas
        if cliente_existente["email"].lower() == email:

            raise ValueError(
                "Ya existe un cliente con ese email"
            )

    # Crea la instancia del cliente
    cliente = Cliente(nombre, email)

    # Convierte el cliente a diccionario
    cliente_dict = {
        "nombre": cliente.nombre,
        "email": cliente.email
    }

    # Agrega el cliente a la lista
    clientes.append(cliente_dict)

    # Guarda los cambios en el archivo JSON
    _guardar_clientes(clientes)

    # Retorna el cliente creado
    return cliente


def obtener_clientes():
    """
    Retorna la lista de clientes almacenados en clientes.json
    """

    # Retorna todos los clientes registrados
    return _leer_clientes()