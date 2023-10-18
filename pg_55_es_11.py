""" - creare una lista x
    - copiare in una nuova lista una metà, e in un'altra nuova lista l'altra metà
    - aggiungere il valore 5 alla lista della prima metà
"""

def main():
    x = [0,1,2,3,5,6,7,8]
    l1=[]
    l2 = []

    for k in x [0:4] :
        l1.append(k)
    l1.append(5)

    for k in x [4:8] :
        l2.append(k) 
    
    print("prima metà")
    for k in l1:
        print(k, end="\t")
    print()

    print("seconda metà")
    for k in l2:
        print(k, end="\t")

if __name__ == "__main__":
    main()