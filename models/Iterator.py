class Iterator:
    def __init__(self, dado):
        self.dado = dado
        self.index = 0

    def __next__(self):
        if self.index >= len(self.dado):
            raise StopIteration
        obj = self.dado[self.index]
        self.index += 1
        return obj

    def __iter__(self):
        return self
    