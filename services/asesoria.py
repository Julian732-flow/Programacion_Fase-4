from services.servicio import Servicio

class ServicioAsesoria(Servicio):
    def __init__(self, sesiones, precio_por_sesion):
        self.sesiones = sesiones
        self.precio_por_sesion = precio_por_sesion

    def calcular_costo(self):
        return self.sesiones * self.precio_por_sesion

    def descripcion(self):
        return f"Asesoría por {self.sesiones} sesiones"