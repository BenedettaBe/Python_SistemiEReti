#list comprehensions

#lista con i primi 5 quadrati perfetti
quadrati = [i**2 for i in range(1,6)]# i per i con i nell'intervallo tra 1 e 6(da 1 a 5)
print(quadrati)

#lista con i primi 10 numeri
numeri_interi = [i for i in range(1,11)]
print(numeri_interi)

#lista con le parole che iniziano con c
stringhe = ["computer", "cellulare", "laptop"]
stringhe_c = [parola for parola in stringhe if parola[0]=="c"]
print(stringhe_c)

#lista con 10 voti casuali
import random
voti = [random.randint(2,10) for _ in range(10)]
print(voti)
voti_insuff = [voto for voto in voti if voto<6]
print(voti_insuff)