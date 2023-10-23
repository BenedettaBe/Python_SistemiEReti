""" - creare una lista_voti con i tuoi voti all'interno
    - stampare la lista senza il primo e ultimo voto
    - sostituire il quarto voto con un 10
    - stampare i primi 3 voti
"""

def print_list(l):
    for elemento in l:
        print(elemento, end=" ")
    print()

def main():
    #vogliamo permettere all'utente di caricare una lista
    lista_voti = []
    num = 1
    nVoti= 0
    while True:
        num = int(input("inserire voto(-1 per uscire): "))
        if(num <0 and nVoti >= 6):
            break
        elif num>0:
            lista_voti.append(num)
            nVoti = nVoti + 1
    
    #stampare la lista senza il primo e ultimo voto
    print(lista_voti[1:-1])
    
    #sostituire il quarto voto con un 10
    lista_voti[4]=10

    #stampare la lista senza il primo e ultimo voto
    print(lista_voti[:3])

if __name__ == "__main__":
    main()