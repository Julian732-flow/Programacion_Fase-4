from models.base_model import BaseModel


class Cliente(BaseModel):

    # Constructor de la clase Cliente
    # Hereda el ID automático desde BaseModel
    def __init__(self, nombre, email):
        super().__init__()
        self.nombre = nombre
        self.email = email

    # Retorna una representación en texto del cliente
    def __str__(self):
        return f"Cliente {self.id}: {self.nombre} - {self.email}"