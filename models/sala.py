from models.servicio import Servicio

class ServicioSala(Servicio):

    # Inicializa un servicio de reserva de salas
    # con cantidad de horas y precio por hora
    def __init__(self, horas, precio_por_hora):
        self.horas = horas
        self.precio_por_hora = precio_por_hora

    # Calcula el costo total de la reserva
    def calcular_costo(self):
        return self.horas * self.precio_por_hora

    # Retorna una descripción básica del servicio
    def descripcion(self):
        return f"Sala por {self.horas} horas"
