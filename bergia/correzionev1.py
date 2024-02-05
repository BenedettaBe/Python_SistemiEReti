class Testo():
    def __init__(self, text):
         self.text = text

    def nCar(self):
        return len(self.text)
    
    def listaParole(self):
        return self.text.split(" ")
    
    def lungPar(self):
        lista = self.listaParole()
        return [len(parola) for parola in lista]
        
    def cercaPar(self, par):
        return par in self.text
    
    def salvaSuFile(self, file):
        with open(file, "w") as file:
            file.write(self.text)

    def freqPar(self):
        diz = {}
        for el in self.listaParole():
            diz[el] = 0
        for par in self.listaParole():
            diz[par] = diz[par] + 1

        return diz

         
def main():
    frase = Testo("ciao come stai?")
    num = frase.nCar()
    parole = frase.listaParole()
    lungPar = frase.lungPar()
    presente= frase.cercaPar('come')
    frase.salvaSuFile('v.txt')
    f = frase.freqPar()
    print(f"{num} {parole} {lungPar} {presente} {f}")


if __name__ == "__main__":
    main()