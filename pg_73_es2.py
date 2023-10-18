#stampa a video se un numero (chiesto all'utente) è divisibile per 2, o per 3, o per 5, o per nessuno di essi
def main():
    num = int(input("Inserisci numero: "))
    div = 3
    if num % 2 == 0:
        print(f"il numero {num} è divisibile per 2")
    elif num % 3 == 0:
         print(f"il numero {num} è divisibile per 3")
    elif num % 5 == 0:
         print(f"il numero {num} è divisibile per 5")
    else:
         print(f"il numero {num} non è divisibile per 2, 3 o 5")


if __name__ == "__main__":
    main()