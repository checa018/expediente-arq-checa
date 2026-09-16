# Solucion: <MARCO ANTONIO CHECA MAMANI>
# Situacion 2: Calculo de tarifas usando el patron Strategy.

from abc import ABC, abstractmethod


# Contrato comun para los calculos de tarifa
class ITarifaStrategy(ABC):
    @abstractmethod
    def calcular_monto_total(
        self, tarifa_base: float, horas: float
    ) -> float:
        pass


# Tarifa de la Manana: Tarifa normal completa
class TarifaMananaStrategy(ITarifaStrategy):
    def calcular_monto_total(
        self, tarifa_base: float, horas: float
    ) -> float:
        return tarifa_base * horas


# Tarifa de la Noche: Recargo del 20%
class TarifaNocheStrategy(ITarifaStrategy):
    def calcular_monto_total(
        self, tarifa_base: float, horas: float
    ) -> float:
        return (tarifa_base * horas) * 1.20


# Tarifa de Fin de Semana: 30% descuento y maximo 3 horas
class TarifaFinDeSemanaStrategy(ITarifaStrategy):
    def calcular_monto_total(
        self, tarifa_base: float, horas: float
    ) -> float:
        horas_efectivas = min(horas, 3.0)
        subtotal = tarifa_base * horas_efectivas
        return subtotal * 0.70


# Clase que maneja y aplica la estrategia actual
class CalculadorTarifaContext:
    def __init__(self, estrategia_inicial: ITarifaStrategy):
        self._estrategia = estrategia_inicial

    def establecer_estrategia(self, nueva_estrategia: ITarifaStrategy):
        self._estrategia = nueva_estrategia

    def obtener_cobro(self, tarifa_base: float, horas: float) -> float:
        return self._estrategia.calcular_monto_total(tarifa_base, horas)


# Ejemplo de uso en el Gimnasio Fuerza Andina
if __name__ == "__main__":
    tarifa_base_hora = 20.0  # Bs. 20 la h

    # Usar tarifa de la manana por defecto
    calculador = CalculadorTarifaContext(TarifaMananaStrategy())
    cobro_manana = calculador.obtener_cobro(tarifa_base_hora, 2.0)
    print(f"Cobro Manana (2 hrs): Bs. {cobro_manana:.2f}")

    # Cambiar a tarifa de la noche
    calculador.establecer_estrategia(TarifaNocheStrategy())
    cobro_noche = calculador.obtener_cobro(tarifa_base_hora, 2.0)
    print(f"Cobro Noche (2 hrs): Bs. {cobro_noche:.2f}")

    # Cambiar a tarifa de fin de semana
    calculador.establecer_estrategia(TarifaFinDeSemanaStrategy())
    cobro_fds = calculador.obtener_cobro(tarifa_base_hora, 4.0)
    print(f"Cobro Fin de Semana (4 hrs): Bs. {cobro_fds:.2f}")
