def verifica(num):
    l = str(num).split()
    l2 = []
    for el in l:
        l2.append(int(el)**3)
    if sum(l2) == num:
        return True
    return False

def main():
    print("Numeri narcisisti: ")
    for i in range(1,1000):
        if(verifica(i) == True):
            print(f"{i} \n")

if __name__ == "__main__":
    main()