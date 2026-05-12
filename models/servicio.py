from abc import ABC, abstractmethod


# Clase abstracta base para todos los servicios
# Define los métodos que deben implementar
# las clases hijas
class Servicio(ABC):

    # Método abstracto para calcular
    # el costo del servicio
    @abstractmethod
    def calcular_costo(self):
        pass

    # Método abstracto para retornar
    # una descripción del servicio
    @abstractmethod
    def descripcion(self):
        pass