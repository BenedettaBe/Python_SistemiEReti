import random
import csv

def genera_labirinto(righe, colonne):
    labirinto = [[0 for _ in range(colonne)] for _ in range(righe)]

    # Genera corridoi casuali
    for i in range(1, righe, 2):
        for j in range(1, colonne, 2):
            labirinto[i][j] = 1

    # Aggiungi corridoi orizzontali casuali
    for i in range(1, righe, 2):
        for j in range(0, colonne, 2):
            if random.random() < 0.5:
                labirinto[i][j] = 1

    # Aggiungi corridoi verticali casuali
    for i in range(0, righe, 2):
        for j in range(1, colonne, 2):
            if random.random() < 0.5:
                labirinto[i][j] = 1

    # Assicurati che ci sia un percorso continuo da un punto di partenza a un punto di arrivo
    labirinto[0][random.randint(0, colonne - 1)] = 1
    labirinto[righe - 1][random.randint(0, colonne - 1)] = 1

    return labirinto

def salva_labirinto_csv(labirinto, nome_file):
    with open(nome_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(labirinto)

# Esempio di utilizzo
righe = 10
colonne = 10
labirinto = genera_labirinto(righe, colonne)
salva_labirinto_csv(labirinto, 'labirinto.csv')
