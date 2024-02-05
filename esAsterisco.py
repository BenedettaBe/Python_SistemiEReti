#dato un numero dispari(fare controllo) scelto da terminare stampare un rombo con n asterischi
#es: n = 5
 #         *
 #        ***
 #       *****
 #        ***
 #         *

def main():
    n = 0
    nAst = 1

    while n % 2 == 0:
        n = int(input("inserisci numero dispari"))

    for i in range(0, n//2+1):
        print(" " * ((n - i)//2) + "*" * nAst)
        nAst += 2

    for i in range(n//2, 0):
        spazio = int(n - i) * " "
        nAst -= 2
        print(spazio + "*" * nAst)

    for i in range(n//2, 0):
        print(" " * ((n - i)//2) + "*" * nAst)
        nAst -= 2  

if __name__ == "__main__":
    main()