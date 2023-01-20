# 10.5
class Element:
    def __init__(self, name, symbol, number):
        self.name = name
        self.symbol = symbol
        self.number = number


el_dict = {'name': 'Hydrogen', 'symbol': 'H', 'number': 1}
Hydrogen = Element(**el_dict)
print(Hydrogen.name, Hydrogen.symbol, Hydrogen.number)