"""
Utilizza le list comprehension per creare una funzione che rimuova tutte le vocali presenti in una stringa.
"""

def print_list(lista):
    print("La lista e': ", end="")
    for elemento in lista:
        print(elemento, end=" ") #con end=" "non va a capo dopo ogni elemento, ma mette uno spazio e continua sulla stessa riga
    print("\n")

def main():
    stringa = "supercalifragilistichespiralitoso"
    vocali="aeiouAEIOU"

    string_no_vocali=[k for k in stringa if(k not in vocali)]
    print("".join(string_no_vocali))
    
if __name__=="__main__": 
    main()