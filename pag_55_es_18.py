def quadrato(num):
    return num*num

def main():
    num1 = int(input("inserire un numero: "))
    num2 = int(input("inserire un secondo numero: "))
    lista = [quadrato(num1) + quadrato(num2), quadrato(num1 + num2), quadrato(num1) - quadrato(num2), quadrato(num1 - num2)]
    print(lista)

if __name__ == "__main__":
    main()