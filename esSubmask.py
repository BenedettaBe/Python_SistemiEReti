#chiedo un numero n compreso tra 1 e 31 che rappresenta una subnetmasck 
#scritta in cdr e deve scriverlo in notazione decimale puntata

def main():
    n = (int)(input("inserisci un numero da 1 a 31: "))
    lista = ("1"*n) + ("0" * (32 - n))
    gruppo1 = lista[0:8]
    gruppo2 = lista[9:16]
    gruppo3 = lista[17:24]
    gruppo4 = lista[25:32]
    numeroBin = [gruppo1,gruppo2,gruppo3,gruppo4]
    print(".".join(numeroBin))
    numeroDec =f"{int(gruppo1, 2)}.{int(gruppo2, 2)}.{int(gruppo3, 2)}.{int(gruppo4, 2)}"
    print(numeroBin)


if __name__ == "__main__":
    main()