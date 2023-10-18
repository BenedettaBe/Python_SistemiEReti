#date due variabili "prima" e "seconda" con numeri interi diversi
#stampare a video i valori, scambiare i valori e visualizzarli a video

def main():
    prima = 1
    seconda = 2
    print(f"1: {prima}     2:{seconda}")
    prima, seconda = seconda, prima
    print(f"1: {prima}     2:{seconda}")

if __name__ == "__main__":
    main()