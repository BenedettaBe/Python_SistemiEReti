#dati 4 valori stampare il valore e il tipo delle variabili 
#(utilizzare l'assegnazione multipla)

def main():
    int, char, float, bool = 1, "ciao", 3.14, True

    tipo = type(int)
    print(f"{int} : {tipo}")
    tipo = type(char)
    print(f"{char} : {tipo}")
    tipo = type(float)
    print(f"{float} : {tipo}")
    tipo = type(bool)
    print(f"{bool} : {tipo}")

if __name__ == "__main__":
    main()