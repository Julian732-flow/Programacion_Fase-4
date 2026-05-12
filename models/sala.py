from models.servicio import Servicio

class ServicioSala(Servicio):
    def __init__(self, horas, precio_por_hora):
        self.horas = horas
        self.precio_por_hora = precio_por_hora

    def calcular_costo(self):
        return self.horas * self.precio_por_hora

    def descripcion(self):
        return f"Sala por {self.horas} horas"
    
    
