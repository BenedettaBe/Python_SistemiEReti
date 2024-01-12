import random
class Nemico():
    def __init__(self, pos_x, pos_y, nVite):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.nVite = nVite 
    def stampa(self):
        print(f"Nemico in posizione {self.pos_x}, {self.pos_y} con {self.nVite} vite")

class Personaggio():
    def __init__(self):
        pass

def main():
    N_NEMICI = 5
    WIDTH = 800
    HEIGHT = 400
    lista_nemici = []
    random.seed(1234)
    for _ in range(N_NEMICI):
        pos_x = random.randint(0, WIDTH-1)
        pos_y = random.randint(0, HEIGHT-1)
        nemico = Nemico(pos_x, pos_y, 5)
        lista_nemici.append(nemico)
    
    personaggio = {"posizione_x" : 100, "posizione_y" : 200}
    for nemico in lista_nemici:
        nemico.stampa()
        if nemico.pos_x == personaggio["posizione_x"] and nemico.pos_y == personaggio["posizione_y"]:
            print("COLLISIONE")


if __name__ == "__main__":
    main()