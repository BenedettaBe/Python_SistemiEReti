import sys

sys.maxsize

def sceltaNodo(nonVisitati, label):
    minLab = sys.maxsize
    minNodo = None
    for nodo in nonVisitati:
        labelNodo = label[nodo]
        if labelNodo < minLab:
            minLab = labelNodo
            minNodo = nodo
    return minNodo

def daNodoaNodo(nodo_sorgente, nodo_destinatario, dizPred):
    lista = []
    lista.append(dizPred[nodo_destinatario])
    while nodo_destinatario != nodo_sorgente:
        nodo_destinatario = dizPred[nodo_destinatario]
        lista.append(dizPred[nodo_destinatario])
        print(nodo_destinatario)
    lista = lista[::-1]
    print(lista)


def djastra(nodo_sorgente, matrice):
    n_nodi = len(matrice)
    nonVisitati = set([i for i in range (0, n_nodi)])
    label = {i:sys.maxsize for i in range (0,n_nodi)}
    label[nodo_sorgente] = 0
    dizPred = {i:None for i in range (0,n_nodi)}
    
    while len(nonVisitati) != 0:
        nodoCorrente = sceltaNodo(nonVisitati, label)
        nonVisitati.remove(nodoCorrente)
        for nodoVicino, peso in enumerate(matrice[nodoCorrente]):
            if peso>0:
                nuovaLabel = label[nodoCorrente] + peso
                if nuovaLabel < label[nodoVicino]:
                    label[nodoVicino] = nuovaLabel
                    dizPred[nodoVicino] = nodoCorrente
        
    return label, dizPred
                

def main():
    mat1=[[0,4,0],
         [4,0,3],
         [0,3,0]]
    
    nodo_sorgente=0
    nodo_destinatario=2
    label, dizPred= djastra(nodo_sorgente, mat1)
    print(label)
    print(dizPred)
    daNodoaNodo(nodo_sorgente, nodo_destinatario, dizPred)


if __name__ == "__main__":
    main()