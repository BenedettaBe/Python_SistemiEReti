#SLICING di stringhe
s = "ciao"
#s[0] [1] [2] [3]
#s[-4][-3][-2][-1]
#   c   i   a   o
print(f"il primo carattere è {s[0]}")
#print(s[0])
print(f"l'ultimo carattere è {s[-1]}")
print(f"il penultimo carattere è {s[-2]}")

#C style - DA NON USARE 
print(f"l'ultimo carattere è {s[len(s)-1]}")

s = "ciao come stai"
print(f"dal carattere 3 al carattere 7 escluso {s[3:7]}") #dal carattere 3 al carattere 7 escluso
print(f"Tutta la stringa esclusi il 1° e l'ultimo carattere {s[1:-1]}") #Tutta la stringa esclusi il 1°(s[0]) e l'ultimo carattere
print(f"Tutta la stringa escluso il 1° carattere {s[1:]}") #stampa tutto tranne il 1° carattere
print(f"Tutta la stringa escluso l'ultimo carattere {s[:-1]}") #stampa tutto tranne l'ultimo carattere
print(s[::-1])#stampa la stringa al contrario