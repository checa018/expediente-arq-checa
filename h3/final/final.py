from abc import ABC, abstractmethod

# 1STRATEGY (Estrategias de Transporte)
class EstrategiaTransporte(ABC):
    @abstractmethod
    def transportar(self, encomienda):
        pass


class TransporteAereo(EstrategiaTransporte):
    def transportar(self, encomienda):
        print(f"[TRANSPORTE] Encomienda {encomienda.codigo_seguimiento} despachada por VÍA AÉREA.")


class TransporteTerrestre(EstrategiaTransporte):
    def transportar(self, encomienda):
        print(f"[TRANSPORTE] Encomienda {encomienda.codigo_seguimiento} despachada por VÍA TERRESTRE.")


# 2. OBSERVER (Notificaciones)
class Cliente:
    def __init__(self, nombre):
        self.nombre = nombre

    def actualizar(self, encomienda):
        print(f"[NOTIFICACIÓN CLIENTE] {self.nombre}: La encomienda {encomienda.codigo_seguimiento} cambió a estado '{encomienda.estado}'.")


class Supervisor:
    def __init__(self, nombre):
        self.nombre = nombre

    def actualizar(self, encomienda):
        print(f"[NOTIFICACIÓN SUPERVISOR] {self.nombre}: Registro de auditoría para {encomienda.codigo_seguimiento} -> Estado: {encomienda.estado}.")


# 3 bCLASE INTEGRADA (GestorEncomienda + Encomienda)
class Encomienda:
    def __init__(self, codigo_seguimiento, peso, estrategia_transporte: EstrategiaTransporte):
        self.codigo_seguimiento = codigo_seguimiento
        self.peso = peso
        self.estado = "REGISTRADO"
        self.estrategia_transporte = estrategia_transporte
        self.observadores = []

    def suscribir(self, observador):
        self.observadores.append(observador)

    def despachar(self):
        self.cambiar_estado("EN_TRANSITO")
        self.estrategia_transporte.transportar(self)

    def cambiar_estado(self, nuevo_estado):
        self.estado = nuevo_estado
        self.notificar()

    def notificar(self):
        for obs in self.observadores:
            obs.actualizar(self)


#  EJECUCIÓN / DEMO DE LA FUSIÓN 
if __name__ == "__main__":
    print("=== SISTEMA DE GESTIÓN DE ENCOMIENDAS (STRATEGY + OBSERVER) ===")

    # Instanciar actores
    cliente = Cliente("María Delgado")
    supervisor = Supervisor("Ing. Roberto")

    # Crear encomienda con Estrategia Terrestre por defecto
    encomienda1 = Encomienda("ENC-9001", 8.5, TransporteTerrestre())

    # Suscribir observadores
    encomienda1.suscribir(cliente)
    encomienda1.suscribir(supervisor)

    # Flujo de operaciones
    encomienda1.despachar()
    encomienda1.cambiar_estado("ENTREGADO")
