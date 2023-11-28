def numProteine(car, p):
    return len([a for a in p if a == car])
    
def main():
    file = open("covid-19_gen1.txt", "r")
    righe = file.readlines()
    file.close
    proteine = ""
    for riga in righe:
        proteine = proteine + riga[:-1]

    print(proteine)

    print(f"a: {numProteine('A', proteine)}")
    print(f"c: {numProteine('C', proteine)}")
    print(f"g: {numProteine('G', proteine)}")
    print(f"t: {numProteine('T', proteine)}")
    
    spike = "ATGTTTGTTTTT"
    for i in enumerate(proteine [:-12]):
        if(proteine[i: i+len(spike)] == spike):
            return i
        
    return -1

if __name__ == "__main__":
    main()