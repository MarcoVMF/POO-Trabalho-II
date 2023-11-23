class Contexto:
    def __init__(self, estrategia):
        self._estrategia = estrategia

    def executar(self, lista):
        return self._estrategia.ordenar(lista)