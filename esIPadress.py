def completaBin(strbin):
    b = strbin[2:]
    l = len(b)
    return "0"*(8-l)+b

def main():
    address = "10.172.24.20"
    groups = address.split(".")#divide address in una lista di stringhe
    groups = [int(group) for group in groups]#converte la lista in una lista di interi
    groupsBin = [bin(group) for group in groups]#converte la lista in una lista di interi

    print(groups)
    print(groupsBin)

    print(completaBin(groupsBin[2]))
    groupsStrbin=[completaBin(bin) for bin in groupsBin]
    print(groupsBin)
    print(".".join(groupsStrbin))

if __name__ == "__main__":
    main()