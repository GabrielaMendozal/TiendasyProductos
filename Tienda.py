from Productos import Productos

class Tienda:
    def __init__(self,name,lista_de_productos):
        self.name =name
        self.lista_de_productos = []

    def agregar_producto(self, nuevo_producto):
        self.lista_de_productos.append

    def vender_producto(self, id):
        self.lista_de_productos.pop(id)
        print (f'{self.name}, {self.precio},{self.categoria}')

    def inflación(self, porcentaje_aumento)
        self.precio += porcentaje_aumento
        actualizar_precio ()

    def hacer_liquidación(self, category, porcentaje_descuento)
        actualizar_precio()