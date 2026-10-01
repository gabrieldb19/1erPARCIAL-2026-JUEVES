def __str__(self) -> str:
    return f'Producto: {self.descripcion}|ID: {self._id_producto}|Precio: ${self.precio}|Stock: {self.stock}'
    
def __eq__(self, value: object) -> bool:
    if type(value) != ProductoKwikE:
        return False
    
    return self._id_producto == value._id_producto and self.descripcion == value.descripcion