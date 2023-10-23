"""
Utilizza le list comprehension per scrivere un programma che crei una lista con tutte le potenze di due minori o uguali a un
valore inserito dall'utente. Stampa la lista.
"""

def main():
    numero = int(input("Inserisci un numero: "))
    esponente=int(math.log2(numero))
    potenze = [2**i for i in range(0, esponente +1)]
    print(potenze)

if __name__=="__main__": 
    import math
    main()