def main():
    nome = input ("Come ti chiami? ")
    anni = int(input("Quanti anni hai? "))#input è una stringa quindi devo fare il casting con int
    anno_corrente = int(input("In quale anno siamo? "))
    print(f"Il tuo nome è {nome} e hai {anni} anni")#con f se devo utilizzare delle variabili atrimenti senza f
    print(f"Sei nato nel {anno_corrente - anni}")

#print(type(anni))#stampa il tipo di variabile

if __name__ == "__main__":
    main()