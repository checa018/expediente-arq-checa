class EncomiendaBase:
    def obtener_descripcion(self):
        return "Encomienda Estándar"

    def calcular_costo(self):
        return 20.0


class DecoradorEncomienda:
    def __init__(self, encomienda):
        self.encomienda = encomienda

    def obtener_descripcion(self):
        return self.encomienda.obtener_descripcion()

    def calcular_costo(self):
        return self.encomienda.calcular_costo()


class ConSeguro(DecoradorEncomienda):
    def obtener_descripcion(self):
        return self.encomienda.obtener_descripcion() + " + Seguro de Envío"

    def calcular_costo(self):
        return self.encomienda.calcular_costo() + 15.0


class ConManejoFragil(DecoradorEncomienda):
    def obtener_descripcion(self):
        return self.encomienda.obtener_descripcion() + " + Manejo Frágil"

    def calcular_costo(self):
        return self.encomienda.calcular_costo() + 10.0


# Ejemplo de uso
if __name__ == "__main__":
    mi_encomienda = EncomiendaBase()
    mi_encomienda = ConSeguro(mi_encomienda)
    mi_encomienda = ConManejoFragil(mi_encomienda)

    print(f"Detalle: {mi_encomienda.obtener_descripcion()}")
    print(f"Costo total: ${mi_encomienda.calcular_costo()}")
