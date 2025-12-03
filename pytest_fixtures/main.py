# def soma(a: int, b: int) -> int:
#     return a + b

class Fruta:
    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        return self.name == other.name
