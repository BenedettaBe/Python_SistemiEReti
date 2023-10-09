def main():
   # num1 = float(input("Inserisci primo numero: "))
   # num2 = float(input("Inserisci secondo numero: "))
    num1, num2 = 5, 7 #assegnamento multiplo
    if num1 < num2:
        num1, num2 = num2, num1 #scambio di variabili

    print(f"{num1} {num2}")


if __name__ == "__main__":
    main()