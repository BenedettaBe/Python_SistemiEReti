#lamba function: utile per definire funzioni brevi

def somma(a, b):
    return a+b

print(somma(3,4))


#nome funzione= lambda  parametri della funzioni semparati da virgole : cosa ritorna la funzione
somma = lambda x,y: x+y


lista = [10, 4]
print(somma(*lista))#(*lista) spacchettare la lista sui paramentri