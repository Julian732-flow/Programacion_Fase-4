from models.servicio import Servicio


class ServicioEquipo(Servicio):

    # Inicializa un servicio de alquiler de equipos
    # con cantidad de días y precio por día
    def __init__(self, dias, precio_por_dia):
        self.dias = dias
        self.precio_por_dia = precio_por_dia

    # Calcula el costo total del alquiler
    def calcular_costo(self):
        return self.dias * self.precio_por_dia

    # Retorna una descripción básica del servicio
    def descripcion(self):
        return f"Equipo por {self.dias} días"