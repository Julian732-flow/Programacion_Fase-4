class BaseModel:

    # Contador compartido entre todas las instancias
    # para generar IDs automáticos
    _id_counter = 1

    # Constructor de la clase
    # Asigna un ID único automáticamente
    def __init__(self):
        self._id = BaseModel._id_counter
        BaseModel._id_counter += 1

    # Getter del atributo id
    # Permite acceder al ID como una propiedad de solo lectura
    @property
    def id(self):
        return self._id