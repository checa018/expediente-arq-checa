from abc import ABC, abstractmethod

class EstrategiaTransporte(ABC):
    @abstractmethod
    def transportar(self, encomienda):
        pass


class TransporteAereo(EstrategiaTransporte):
    def transportar(self, encomienda):
        print(f"Transportando encomienda {encomienda['codigo_seguimiento']} por vía AÉREA (Tiempo estimado: 24 horas).")


class TransporteTerrestre(EstrategiaTransporte):
    def transportar(self, encomienda):
        print(f"Transportando encomienda {encomienda['codigo_seguimiento']} por vía TERRESTRE (Tiempo estimado: 3 días).")


class ContextoEnvio:
    def __init__(self, estrategia: EstrategiaTransporte):
        self.estrategia = estrategia

    def set_estrategia(self, estrategia: EstrategiaTransporte):
        self.estrategia = estrategia

    def ejecutar_envio(self, encomienda):
        self.estrategia.transportar(encomienda)


# Ejemplo de uso
if __name__ == "__main__":
    encomienda = {"codigo_seguimiento": "ENC-2002", "peso": 12.0}
    envio = ContextoEnvio(TransporteTerrestre())
    envio.ejecutar_envio(encomienda)

    # Cambio dinámico de estrategia
    envio.set_estrategia(TransporteAereo())
    envio.ejecutar_envio(encomienda)
