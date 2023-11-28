import random

def main():
    s= 0
    lista = [random.choice([-1,1]) for _ in range(1, 60 * 60 * 24 * 5)]
    for i in lista:
        s += i
    print(s)

if __name__ == "__main__":
    main()