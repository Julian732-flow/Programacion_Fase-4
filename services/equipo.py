from services.servicio import Servicio

class ServicioEquipo(Servicio):
    def __init__(self, dias, precio_por_dia):
        self.dias = dias
        self.precio_por_dia = precio_por_dia

    def calcular_costo(self):
        return self.dias * self.precio_por_dia

    def descripcion(self):
        return f"Equipo por {self.dias} días"