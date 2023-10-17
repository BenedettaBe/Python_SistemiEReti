#le liste
def print_list(l):
    print("La lista è: ", end=" ")
    for elemento in l:
        #print(elemento, end="\n") == print(elemento)
        print(elemento, end=" ")
    print()

def main():
    l = [1,2,3,"c", 3.14, "python"]
    r = [5, 6, "j"]
    #print(l)
    #print(l[-1])
    #print_lista(l+r)#concatena le due liste

    #vogliamo permettere all'utente di caricare una lista
    lista = []
    num = 1
    while num > 0:
        num = int(input("scrivere numero: "))
        if num>0:
            lista.append(num)
    print_list(lista)


if __name__ == "__main__":
    main()