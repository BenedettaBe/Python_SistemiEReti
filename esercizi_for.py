lista = [4, 100, 5, "ciao", print] #lista

#Ciclo for C-style (DA NON FARE)
for i in range(0,len(lista)): #len(lista) dice la dimensione
        print(f"l'elemento {i}esimo della lista è {lista[i]}")


#Ciclo for Python-style
for elemento in lista:  #per ogni elemento in lista, stampa elemento(la variabile"elemento" può avere un altro nome)
    print(f"Elemento: {elemento}")

