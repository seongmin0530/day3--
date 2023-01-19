# global variable

g = 'global variable'

def change_print_global():
    g = 'local variable'
    return g

def print_global():
    global g
    g = 'global variable in function'
    return g


change_print_global()
print_global()
print(g)
print(globals())
print(__name__)