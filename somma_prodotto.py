def somma(a,b):
    return a+b

def prodotto(a, b):
    return a*b

def divisione(a, b):
    return a/b

def sottrazione(a, b):
    return a-b

def main():
    dizionario = {"+":somma, "*":prodotto, ":":divisione, "-":sottrazione}
    operazione = input("scrivi + per somma, * per prodotto, - per sottrazione, : per divisone  : ")
    if operazione in dizionario:
        a = float(input("Scrivi il primo numero: "))
        b = float(input("Scrivi il secondo numero: "))
        print(dizionario[operazione](a, b)) 
    else:
        print("Errore")

if __name__ == "__main__":
    main()