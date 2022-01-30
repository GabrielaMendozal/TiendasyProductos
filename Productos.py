class Producto:
    def __init__(self, name,precio,categoria):
        self.name = name
        self.precio = precio
        self.categoria = categoria

        def actualizar_precio(self, cambio_porcentaje, está_elevado):
            if está_elevado = True 
                self.precio += cambio_porcentaje
            else:
                self.precio -= cambio_porcentaje
            return self

        def Print_info(self):
            print(f'Nombre del producto: {self.name}, categoria: {self.categoria}, precio: {self.precio}')