"""
Utilizza le list comprehension per creare la tavola pitagorica per i numeri da 1 a 10. 
Stampa la tavola ottenuta e salvala su file.
"""

def print_tavola(tavola):
    for k, tabellina in enumerate(tavola): #enumerate numera le liste e ritorna indice e elemento
        #tabellina è una lista. tavola è una lista di liste
        #k = indice dell'array
        print(f"tabellina del {k+1}: {tabellina}")

def main():
    n = 10
    tavola = [[i * j for j in range(1, n + 1)] for i in range(1, n + 1)]
    print_tavola(tavola)

    file = open("tabelline.txt", "w")
    for tabellina in tavola: 
        file.write(f"{tabellina}\n")
    file.close

if __name__=="__main__": 
    main()