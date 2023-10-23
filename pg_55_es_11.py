""" - creare una lista x
    - copiare in una nuova lista una metà, e in un'altra nuova lista l'altra metà
    - aggiungere il valore 5 alla lista della prima metà
"""

def print_list(l):
    for elemento in l:
        print(elemento, end=" ")
    print()

def main():
    x = [0,1,2,3,5,6,7,8]
    l1=[]
    l2 = []

    mezzo = len(x)//2 #// divisione intera

    l1 = x[:mezzo]
    l2 = x[mezzo:]
    
    l1.append(l2[0])

    print("prima metà")
    print_list(l1)

    print("seconda metà")
    print_list(l2)

if __name__ == "__main__":
    main()