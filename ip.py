#dato da input un indirizzo di rete e la subnet mask verificare:
#se privato o loopback
#se l'indirizzo è valido stampa tutti gli ip utilizzabili

import ipaddress

def main():
    ip = input("inserisci ip: ")
    sb = input("inserisci subnet mask: ")
    IP = ipaddress.IPv4Address(ip)
    ipPieno = str(ip+sb)
    if(IP.is_private):
        print("è privato")
    if(IP.is_loopback):
        print("è loopback")
    ipRete = ipaddress.IPv4Network(ipPieno, strict=False)
    if (ipPieno) == str(ipRete):
        print(f"è di rete perchè l'indirizzo {ip} coincide con l'indirizzo {ipRete}")
    else:
        print(f"non è di rete perchè l'indirizzo {ip} coincide con l'indirizzo {ipRete}")
    hosts = list(ipRete.hosts())
    print(hosts)
    print(f"il primo host utilizzabile é: {hosts[0]}")
    print(f"l'ultimo host utilizzabile é: {hosts[-1]}")

if __name__ == "__main__":
    main()