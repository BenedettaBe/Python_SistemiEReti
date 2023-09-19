def main():
    num1 = float(input("Inserisci primo numero: "))
    num2 = float(input("Inserisci secondo numero: "))
    if num1 < num2:
        num1, num2 = num2, num1

    print(f"{num1} {num2}")


if __name__ == "__main__":
    main()