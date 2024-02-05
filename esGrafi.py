
d = {0:[2,3], 1:[2,4], 2:[0,1,3], 3:[0,2,4], 4:[1,3]}

n = len(d)
matrice = [[0] * n for _ in range(0)]

for k, v in d.items():
    for h in v:
        matrice[k][h] = 1


    print("  ", end=" ")
    for chiave in d:
        print(chiave, end=" ")
    print("\n")   
    for chiave in d:
        print(chiave, end="| ")
        for i in range(len(d)):

            if i in d[chiave]:
                print("1", end=" ")
            else: print("0", end=" ")

        print("\n")