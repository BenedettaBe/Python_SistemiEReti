#dato un numero dispari(fare controllo) scelto da terminare stampare un rombo con n asterischi
#es: n = 5
 #         *
 #        ***
 #       *****
 #        ***
 #         *

def main():
    n = int(input("inserisci numero dispari"))

    for i in range(0,n):
        for k in range(1, i):
            print(f"*")

if __name__ == "__main__":
    main()