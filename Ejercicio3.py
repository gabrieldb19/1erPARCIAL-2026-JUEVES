def cantidad_recursiva(a: int, b: int):
    def contar(index):
        if index == b:
            return 0
        return a + contar(index + 1)

    return contar(0)