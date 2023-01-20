# 10.4
class Element:
    def __init__(self, name, symbol, number):
        self.name = name
        self.symbol = symbol
        self.number = number


test = Element('Hydrogen', 'H', 1)
print(test.name, test.symbol, test.number)