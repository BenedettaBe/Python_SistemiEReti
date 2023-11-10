def main(): 
    rubrica = {}
    file = open("rubrica.txt", "r")
    righe = file.readlines()
    file.close
    print(righe)

    for riga in righe:
        campi = riga.split(", ")
        #rubrica[nome[0]] = nome[1]
        rubrica[int(campi[1].replace("\n", ""))] = campi[0]  #.replace sostituisce \n con un carattere vuoto

    print(rubrica)
    

if __name__ == "__main__":
    main()