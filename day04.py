# tuple
a = 'harry',  #packing
b = ()  #empty tuple
c = 'harry',  #packing
d = ('harry',)  #packing
e = 'harry','ron'  #packing
f = ('harry','ron')  #packing
g = ('hermione')  #string
print(id(g))  #before +=
g = g + f  #덮어쓰기
print (g,id(g))  #after +=
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(e))
print(type(g))

x, y = f
print(x)  #unpacking
print(y)  #unpacking