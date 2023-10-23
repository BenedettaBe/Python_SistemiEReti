"""
Utilizza le list comprehension per scrivere un programma che crei una lista con tutti i quadrati perfetti minori di 200 che siano
dispari. Stampa la lista.
"""

def main():
    #quadrati = [i**2 for i in range (0, int(math.sqrt(200)) + 1) if i**2 % 2 != 0]
    quadrati = [i**2 for i in range (0, 1000) if (i**2 % 2 != 0) and (i**2 < 200)]
    print(quadrati)
    
if __name__=="__main__": 
    import math
    main()