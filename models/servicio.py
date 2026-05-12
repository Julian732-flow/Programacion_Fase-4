from abc import ABC, abstractmethod

class Servicio(ABC):

    @abstractmethod
    def calcular_costo(self):
        pass

    @abstractmethod
    def descripcion(self):
        pass