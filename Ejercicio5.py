from datetime import date

class ProductoKwikE:
    def __init__(self, id_producto: int, descripcion: str, fecha_vencimiento: date, precio: float, stock: int) -> None:
        self._id_producto = id_producto
        self._descripcion = descripcion
        self._fecha_vencimiento = fecha_vencimiento
        self._precio = precio
        self._stock = stock

    # ############################################# #
    # Metodos __str__, __eq__ para el ejercicio 6
    def __str__(self) -> str:
        return f'Producto: {self.descripcion}|ID: {self._id_producto}|Precio: ${self.precio}|Stock: {self.stock}'
    
    def __eq__(self, value: object) -> bool:
        if type(value) != ProductoKwikE:
            return False
    
        return self._id_producto == value._id_producto and self.descripcion == value.descripcion
    # ############################################# #

    def expiracion(self):
        if date.today() > self._fecha_vencimiento:
            print(f'Producto vencido. Cambiado stock a 0.')
            self.stock = 0
        else:
            print('Producto aun sin expirar.')

    @property
    def descripcion(self):
        return self._descripcion
    @descripcion.setter
    def descripcion(self, nuevo: str):
        self._descripcion = nuevo

    @property
    def precio(self):
        return self._precio
    @precio.setter
    def precio(self, nuevo):
        self._precio = nuevo
    
    @property
    def stock(self):
        return self._stock
    @stock.setter
    def stock(self, nuevo):
        self._stock = nuevo