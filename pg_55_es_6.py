#data una parola stampare tutte le lettere con indice dispari


def main():
    parola = "ciao"
    print(parola[1::2])

def mainFor():
    parola = "ciao"
    for k in range(0,len(parola)):
        if(k % 2 != 0):
            print(f"{parola[k]}", end="")

if __name__ == "__main__":
    main()