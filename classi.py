#classi
#in py è tutto pubblico = no set/get

#definizione classe (nome con iniziale maiuscola)
class Quadrato():
    def __init__(self, lato):#definizione del costruttore def __init__(self):   le cose tra parentesi sono parametri
         self.lato = lato

    def calcolaArea(self):#metodo
         return self.lato**2
    
    def stampaLato(self):
         print(f"Il lato è {self.lato}")
    
def main():
        q = Quadrato(4)
        print(f"l'area del quadrato è {q.calcolaArea()}")
        print(q.lato)
        q.lato = 5
        print(f"l'area del quadrato è {q.calcolaArea()}")

if __name__ == "__main__":
     main()