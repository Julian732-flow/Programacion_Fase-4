from models.base_model import BaseModel

class Cliente(BaseModel):
    def __init__(self, nombre, email):
        super().__init__()
        self.nombre = nombre
        self.email = email

    def __str__(self):
        return f"Cliente {self.id}: {self.nombre} - {self.email}"