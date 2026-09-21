class Encomienda:
    def __init__(self, codigo_seguimiento, peso, origen, destino, estado="REGISTRADO", fecha_estimada_llegada=None):
        self.codigo_seguimiento = codigo_seguimiento
        self.peso = peso
        self.origen = origen
        self.destino = destino
        self.estado = estado
        self.fecha_estimada_llegada = fecha_estimada_llegada

    def cambiar_estado(self, nuevo_estado):
        self.estado = nuevo_estado
        print(f"Encomienda {self.codigo_seguimiento} cambió a estado: {this.estado}" if hasattr(self, 'this') else f"Encomienda {self.codigo_seguimiento} cambió a estado: {self.estado}")

    def consultar_estado(self):
        return f"Encomienda [{self.codigo_seguimiento}]: {self.estado} (Destino: {self.destino})"
