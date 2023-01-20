# 10.3

class Thing3:
    def __init__(self, letter):
        self.letter = letter
        print('Thing3 class object is Created')


test = Thing3('xyz')
print(test.letter)