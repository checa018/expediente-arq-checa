class Cliente:
    def __init__(self, id_cliente, nombre, telefono, direccion):
        self.id_cliente = id_cliente
        self.nombre = nombre
        self.telefono = telefono
        self.direccion = direccion

    def consultar_estado(self, encomienda):
        print(f"Cliente {self.nombre} consulta estado: {encomienda.consultar_estado()}")
