"""
appicare l'operatore di concatenazione delle stringhe sulle lista "a" e "b"
stampa la lista finale
"""

def print_list(l):
    print("La lista è: ", end=" ")
    for elemento in l:
        #print(elemento, end="\n") == print(elemento)
        print(elemento, end=" ")
    print()

def main():
    a = [0,1,2,3]
    b = [4,5,6,7]
    print_list(a+b)
    
if __name__ == "__main__":
    main()