#dati 4 valori stampare il valore e il tipo delle variabili

def main():
    int = 1
    char = "ciao"
    float = 3.14
    bool = True

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


#variabili = [1,"c", 3.14, True]
 #   for elemento in variabili:
  #      tipo = type(elemento)
   #     print(f"{elemento} : {tipo}")