#data una parola di almeno 8 carattere, stampare tua la parola con "?" al posto del terzo carattere
def main():
    parola = "Benedetta"
    if(len(parola) < 8):
        print("parola non valida")
    else:
        for k in range(0,len(parola)):
            if(k == 3):
                print(f"?", end="")
            else:
                print(f"{parola[k]}", end="")

if __name__ == "__main__":
    main()