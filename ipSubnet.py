#fare un programma che chieda all'utente un indirizzo IP e 
#una subnet mask in notazione CIDR: calcolare IP di rete e IP di broadcast

def convertiDecimale(ip_binario):
    gruppoDecimale = []
    for i in range (0,32, 8):
        ottetto = ip_binario[i:i+8]
        gruppoDecimale.append(str(int(ottetto,2)))#riempe la lista con i gruppi binari
    return ".".join(gruppoDecimale)

def main():
    address = input("Inserisci indirizzo IP: ")
    n = int(input("Inserisci una subnet mask in notazione CIDR: "))
    
    numBin=[format(int()), '00b']
    subnet = (("1" * n) + "0" * (32 - n))
    wildcard = (("0" * n) + "1" * (32 - n))
    groups = address.split(".")
    rete =["0" if(k<n) else ("0") for k in range(32)]
    broadcast =[groups[k] if (k < n or groups[k] == 1) else ("0") for k in range(32)]


    print(f"Indirizzo rete: {convertiDecimale(rete)}")
    print(f"Indirizzo broadcast: {convertiDecimale(broadcast)}")

if __name__ == '__main__':
    main()