class Testo():
    def __init__(self, text):
         self.text = text

    def nCar(self):
        return len(self.text)
    
    def listaParole(self):
        return self.text.split(" ")
    
    def lungPar(self):
        lista = self.listaParole()
        lung = []
        for el in lista:
            lung.append(len(el))
        return lung
    
    def cercaPar(self, par):
        ret = False
        if(par in self.text):
            ret = True
        return ret
    
    def salvaSuFile(self, file):
        file = open(file, "w")
        file.write(self.text)
        file.close()

    def freqPar(self):
        diz = {}
        for el in self.listaParole:
            diz[el] = 0
        for par in self.listaParole:
            diz[par] = diz[par] + 1

        print(diz)

         
def main():
    frase = Testo("ciao come stai?")
    num = frase.nCar()
    parole = frase.listaParole()
    lungPar = frase.lungPar()
    presente= frase.cercaPar('come')
    frase.salvaSuFile('v.txt')
    frase.freqPar()
    print(f"{num} {parole} {lungPar} {presente}")


if __name__ == "__main__":
    main()