class Encomienda:
    def __init__(self, codigo_seguimiento, peso, origen, destino):
        self.codigo_seguimiento = codigo_seguimiento
        self.peso = peso
        self.origen = origen
        self.destino = destino
        self.estado = "REGISTRADO"
        self.observadores = []

    def suscribir(self, observador):
        self.observadores.append(observador)

    def cambiar_estado(self, nuevo_estado):
        self.estado = nuevo_estado
        print(f"\n[EVENTO] Encomienda {self.codigo_seguimiento} cambió a: {nuevo_estado}")
        self.notificar()

    def notificar(self):
        for obs in self.observadores:
            obs.actualizar(self)


class ClienteObservador:
    def __init__(self, nombre):
        self.nombre = nombre

    def actualizar(self, encomienda):
        print(f"Notificación para Cliente {self.nombre}: Su encomienda {encomienda.codigo_seguimiento} está {encomienda.estado}.")


# Ejemplo de uso
if __name__ == "__main__":
    encomienda = Encomienda("ENC-1001", 5.5, "La Paz", "Santa Cruz")
    cliente = ClienteObservador("Carlos Pérez")

    encomienda.suscribir(cliente)
    encomienda.cambiar_estado("EN_TRANSITO")
    encomienda.cambiar_estado("ENTREGADO")
