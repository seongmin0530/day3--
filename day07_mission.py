# 10. 8
class Element:
    def __init__(self, name, symbol, number):
        self.hidden_name = name
        self.hidden_symbol = symbol
        self.hidden_number = number

    def get_value(self):
        return self.hidden_name, self.hidden_symbol, self.hidden_number

    def set_value(self, input_name, input_symbol, input_number):
        self.hidden_name = input_name
        self.hidden_symbol = input_symbol
        self.hidden_number = input_number

    def __str__(self):
        return f'Name: {self.name}\tSymbol: {self.symbol},\tNumber: {self.number}'


el_dict = {'name': 'hydrogen', 'symbol': 'H', 'number': 1}
Hydrogen = Element(**el_dict)
print(Hydrogen.get_value())