class KwikEMart:
    def __init__(self) -> None:
        self._pasillos = {
            'Bebidas': [],
            'Snacks': [],
            'Conveniencia': []
            }

    def add_producto(self, pasillo: str, producto: ProductoKwikE):
        if pasillo in self._pasillos.keys():
            self._pasillos[pasillo].append(producto)

    def remove_producto(self, pasillo: str, id_producto: int):
        if pasillo in self._pasillos.keys():
            for i, p in enumerate(self._pasillos[pasillo]):
                if p._id_producto == id_producto:
                    self._pasillos[pasillo].pop(i)
                    break

    def expiracion(self):
        expirados = []
        for pasillo, productos in self._pasillos.items():
            for i, p in enumerate(productos):
                dias = date.today() - p._fecha_vencimiento
                if dias.days > 1:
                    pass
                else:
                    productos.pop(i)
                    expirados.append(p)
        
        print("Productos expirados:")
        [print(p) for p in expirados]