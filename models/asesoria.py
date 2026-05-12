from models.servicio import Servicio


class ServicioAsesoria(Servicio):
    """Representa una asesoría especializada basada en sesiones.

    Attributes:
        sesiones (int): Número de sesiones de la asesoría.
        precio_por_sesion (float): Costo de cada sesión.
    """

    def __init__(self, sesiones, precio_por_sesion):
        self.sesiones = sesiones
        self.precio_por_sesion = precio_por_sesion

    # Calcula el costo total de la asesoría
    def calcular_costo(self):
        return self.sesiones * self.precio_por_sesion

    # Retorna una descripción básica del servicio
    def descripcion(self):
        return f"Asesoría por {self.sesiones} sesiones"