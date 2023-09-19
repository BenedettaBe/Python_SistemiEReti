def main():
    a = float(input("Inserisci un numero: "))
    print(f"il tipo di a è {type(a)}")
    if a > 5:
        print(" a è maggiore di 5")
    elif (a<=5) & (a>=0):
        print("a è minore o uguale a 5")
    else:
        print("a è minore o uguale a 5 di 0")

#print(type(anni))#stampa il tipo di variabile

if __name__ == "__main__":
    main()