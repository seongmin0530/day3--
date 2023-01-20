# 10. 7
class Element:
    def __init__(self, name, symbol, number):
        self.name = name
        self.symbol = symbol
        self.number = number

    def __str__(self):
        return f'Name: {self.name}\tSymbol: {self.symbol},\tNumber: {self.number}'


el_dict = {'name': 'hydrogen', 'symbol': 'H', 'number': 1}
Hydrogen = Element(**el_dict)
print(Hydrogen)