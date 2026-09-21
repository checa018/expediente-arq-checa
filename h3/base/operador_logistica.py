class OperadorLogistica:
    def __init__(self, id_operador, nombre):
        self.id_operador = id_operador
        self.nombre = nombre

    def actualizar_estado(self, encomienda, nuevo_estado):
        print(f"Operador {self.nombre} actualiza la encomienda {encomienda.codigo_seguimiento}...")
        encomienda.cambiar_estado(nuevo_estado)
