import json
import os
from models.cliente import Cliente

RUTA_CLIENTES = "data/clientes.json"

def _leer_clientes():
    if not os.path.exists(RUTA_CLIENTES):
        return []

    with open(RUTA_CLIENTES, "r") as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return []


def _guardar_clientes(clientes):
    with open(RUTA_CLIENTES, "w") as file:
        json.dump(clientes, file, indent=4)


def crear_cliente(nombre, email):
    """
    Crea y guarda un cliente en clientes.json
    """

    if not nombre or not nombre.strip():
        raise ValueError("El nombre no puede estar vacío")
    if not email or not email.strip():
        raise ValueError("El email no puede estar vacío")
    if "@" not in email or "." not in email:
        raise ValueError("El email no tiene un formato válido")

    clientes = _leer_clientes()

    for c in clientes:
        if c["email"] == email:
            raise ValueError("Ya existe un cliente con ese email")

    cliente = Cliente(nombre.strip(), email.strip())

    cliente_dict = {
        "nombre": cliente.nombre,
        "email": cliente.email
    }

    clientes.append(cliente_dict)
    _guardar_clientes(clientes)

    return cliente

def obtener_clientes():
    """
    Retorna la lista de clientes almacenados en clientes.json
    """
    return _leer_clientes()