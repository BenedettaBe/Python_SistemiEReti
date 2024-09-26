#set()crea un insieme, non indicizzabili
a = set([1,2,3])
b = set([5,6])
print(a)
print(b)
print(a|b)
print(a&b)
b.remove(6)
print(b)