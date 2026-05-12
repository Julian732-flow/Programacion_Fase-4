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

    nombre = nombre.strip()

    if len(nombre) < 3:
        raise ValueError("El nombre debe tener al menos 3 caracteres")

    if len(nombre) > 50:
        raise ValueError("El nombre no puede superar los 50 caracteres")

    if not all(c.isalpha() or c.isspace()for c in nombre):

        raise ValueError("El nombre solo puede contener letras y espacios")

    if not email or not email.strip():
        raise ValueError("El email no puede estar vacío")

    email = email.strip().lower()

    patron_email = r"^[\w\.-]+@[\w\.-]+\.\w+$"

    if not re.match(patron_email, email):

        raise ValueError("El email no tiene un formato válido")

    if len(email) > 100:
        raise ValueError("El email es demasiado largo")

    clientes = _leer_clientes()

    for cliente_existente in clientes:
        if cliente_existente["email"].lower() == email:
            raise ValueError("Ya existe un cliente con ese email")

    cliente = Cliente(nombre, email)

    cliente_dict = {"nombre": cliente.nombre,"email": cliente.email}

    clientes.append(cliente_dict)

    _guardar_clientes(clientes)

    return cliente


def obtener_clientes():
    """
    Retorna la lista de clientes almacenados en clientes.json
    """
    return _leer_clientes()