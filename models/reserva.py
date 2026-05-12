class Reserva:

    # Inicializa una reserva asociando
    # un cliente y un servicio
    def __init__(self, cliente, servicio):
        self.cliente = cliente
        self.servicio = servicio
        self.estado = "pendiente"

    # Cambia el estado de la reserva a confirmada
    def confirmar(self):
        self.estado = "confirmada"

    # Cambia el estado de la reserva a cancelada
    def cancelar(self):
        self.estado = "cancelada"