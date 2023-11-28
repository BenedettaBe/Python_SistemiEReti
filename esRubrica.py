def main(): 
    rubrica = {}
    file = open("rubrica.txt", "r")
    righe = file.readlines()
    file.close
    print(righe)

    for riga in righe:
        campi = riga.split(", ")
        rubrica[int(campi[1].replace("\n", ""))] = campi[0]  #.replace sostituisce \n con un carattere vuoto

    print(rubrica)
    
    tro = -1
    dato=input("inserisci dato: ")
    for num in rubrica:
        if dato == str(num):
            print(f"numero: {num}  nome:{rubrica[num]}")
            tro = 1
        elif rubrica[num] == dato:
            print(f"nome:{rubrica[num]}  numero: {num}")
            tro = 1

    if(tro == -1):
        print("non è stato trovato!!!")
        

if __name__ == "__main__":
    main()