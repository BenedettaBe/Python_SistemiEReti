class Quad:
    def __init__(self, lato):
        self.lato = lato

    def calcolaArea(self):
        return self.lato*self.lato

    def calcolaPerimetro(self):
        return self.lato * 4
    
    def descrizione(self):
        return f"Nome: {self.lato}, area: {self.calcolaArea}, perimetro: {self.calcolaPerimetro}"
    
    def puntoInterno(self, x, y):
        return (x > 0 and x < self.lato and y > 0 and y < self.lato)
    
def main():
    quadrato = Quad(3)
    print(quadrato.descrizione)
    print(quadrato.puntoInterno(4,5))

    quadrato2 = Quad(3)
    print(quadrato.descrizione)
    print(quadrato.puntoInterno(3,2))

if __name__ == "__main__":
    main()