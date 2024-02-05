import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

def prettyPrint(matrice, separatore = " "):
    for riga in matrice:
        rigaStr=[str(x) for x in riga]
        print(separatore.join(rigaStr))

def diz_inverso(matrice):
    d = {i: [] for i in range(len(matrice))}
    k=0
    for riga in matrice:
        for num in riga:
            d[k].append(num)
        k+=1

    print(d)

def disegnaGrafo(matrice_adiacenza):
    # Crea un grafo non diretto
    G = nx.Graph()

    # Aggiungi nodi al grafo
    num_nodi = len(matrice_adiacenza)
    G.add_nodes_from(range(num_nodi))

    # Aggiungi archi al grafo in base alla matrice di adiacenza
    for i in range(num_nodi):
        for j in range(num_nodi):
            if matrice_adiacenza[i][j] == 1:
                G.add_edge(i, j)

    # Disegna il grafo
    pos = nx.spring_layout(G)  # Layout per il disegno del grafo
    nx.draw(G, pos, with_labels=True, font_weight='bold', node_size=700, node_color='skyblue', font_color='black', font_size=8, edge_color='gray', linewidths=1)

    # Mostra il grafo
    plt.show()

def main():
    dizR = {0:[2,3], 1:[2,4], 2:[0,1,3], 3:[0,2,4], 4:[1,3]}
    n  = len(dizR)
    mat= [[0]*n for _ in range (n)]
    l2 = []
    for k, v in dizR.items():
        for  h in v:
            mat[k][h] = 1      
    prettyPrint(mat,)
    diz_inverso(mat)

    disegnaGrafo(mat)

if __name__ == '__main__':
    main()