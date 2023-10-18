""" - creare una lista_voti con i tuoi voti all'interno
    - stampare la lista senza il primo e ultimo voto
    - sostituire il quarto voto con un 10
    - stampare i primi 3 voti
"""

def main():
    #vogliamo permettere all'utente di caricare una lista
    lista_voti = []
    num = 1
    nVoti= 0
    while (num > 0 or len(lista_voti)<6):
        num = int(input("inserire voto(-1 per uscire): "))
        if num>-1:
            lista_voti.append(num)
            nVoti = nVoti +1
    
    #stampare la lista senza il primo e ultimo voto
    for k in lista_voti [1:-1]:
        print(k, end="\n")
    
    #sostituire il quarto voto con un 10
    lista_voti[4]=10

    #stampare la lista senza il primo e ultimo voto
    print("primi 3 voti: ")
    for k in range (0,3):
        print(lista_voti[k], end="\t")

if __name__ == "__main__":
    main()