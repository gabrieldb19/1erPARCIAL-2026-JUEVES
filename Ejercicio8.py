class Nodo:
    def __init__(self, dato, sig=None):
        self._elem = dato
        self._nxt = sig

class IteradorLista:
    def __init__(self, cabeza):
        self.actual = cabeza

    def __iter__(self):
        return self

    def __next__(self):
        if self.actual is None:
            raise StopIteration
        elemento = self.actual._elem
        self.actual = self.actual._nxt
        return elemento

class ListaEnlazada:
    def __init__(self, header: Nodo = None):
        self.header: Nodo = header

    def __str__(self):
            return str(list(self))

    def __iter__(self):
        return IteradorLista(self.header)

    def append(self, elem: Nodo):
        if not self.header:
            self.header = elem
            return
        
        n = self.header
        while n._nxt:
            n = n._nxt
        n._nxt = elem

    def remove(self, elemento):
        anterior = None
        actual = self.header

        while actual:
            if actual._elem == elemento:
                if anterior is None:
                    self.header = actual._nxt
                else:
                    anterior._nxt = actual._nxt
                return True
            anterior = actual
            actual = actual._nxt

        return False

class KwikEMart:
    def __init__(self) -> None:
        self._pasillos = {
            'Bebidas': ListaEnlazada(),
            'Snacks': ListaEnlazada(),
            'Conveniencia': ListaEnlazada()
            }

    def add_producto(self, pasillo: str, producto: ProductoKwikE):
        if pasillo in self._pasillos.keys():
            self._pasillos[pasillo].append(Nodo(producto))

    def remove_producto(self, pasillo: str, id_producto: int):
        if pasillo in self._pasillos.keys():
            for p in self._pasillos[pasillo]:
                if p._id_producto == id_producto:
                    self._pasillos[pasillo].remove(p)
                    break

    def expiracion(self):
        expirados = []
        for pasillo, productos in self._pasillos.items():
            for p in productos:
                dias = date.today() - p._fecha_vencimiento
                if dias.days > 1:
                    pass
                else:
                    productos.remove(p)
                    expirados.append(p)
        
        print("Productos expirados:")
        [print(p) for p in expirados]