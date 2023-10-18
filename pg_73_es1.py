def main():
    num = int(input("Inserisci numero: "))
    div = 3
    if num % div == 0:
        print(f"il numero {num} è divisibile per {div}")
    else:
        print(f"il numero {num} non è divisibile per {div}")


if __name__ == "__main__":
    main()