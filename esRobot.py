import pygame

class Grafo():
    def draw_map(self, screen, mappa, robot, lato_quad, pavimento, muro, font):
        k = 0
        for y, row in enumerate(mappa):
            for x, cell in enumerate(row):
                if cell == 1:
                    screen.blit(muro, (x * lato_quad, y * lato_quad))
                elif cell == 3:
                    pass
                    #screen.blit(robot, (x * lato_quad, y * lato_quad))
                else:
                    screen.blit(pavimento, (x * lato_quad, y * lato_quad))
                    testo = font.render(f"{k}", True, (0, 0, 0))
                    text_rect = testo.get_rect(center=(x * lato_quad + lato_quad - 15, y * lato_quad + 15))
                    screen.blit(testo, text_rect)
                    k += 1


    def findFreeCell(self):
        self.matriceNumerata = self.mat
        for i, riga in enumerate(self.mat):
            for j, cella in enumerate(riga):
                if cella[][] > -1:
                    self.matriceNumerata[i][j] = 1
                else:
                    self.matriceNumerata[i][j] = cont
                    
                    
def main():
    pygame.init()
    lato_quad = 100
    mappa = []
    diz = []

    pavimento = pygame.image.load("pavimento.jpg")
    pavimento = pygame.transform.scale(pavimento, (lato_quad, lato_quad))
    muro = pygame.image.load("muro.jpg")
    muro = pygame.transform.scale(muro, (lato_quad, lato_quad))
    robot = pygame.image.load("omino.png")
    muro = pygame.transform.scale(robot, (lato_quad, lato_quad))
    
    with open("pavimento.csv", "r") as f:
        for riga in f.readlines():
            riga = riga.split(',')  
            riga_int = [int(c) for c in riga]
            mappa.append(riga_int)
    
    num_colonne = len(mappa[0])
    num_righe = len(mappa)
    screen_width = num_colonne * lato_quad
    screen_height = num_righe * lato_quad
    
    matrice = [[-1 for _ in range(num_righe)] for _ in range(num_colonne)]


    screen = pygame.display.set_mode((screen_width, screen_height))
    font = pygame.font.SysFont("Verdana", 30)
    
    pygame.display.set_caption('Mappa')
    running = True
    while running:
        k = 0
        for y, row in enumerate(mappa):
            for x, cell in enumerate(row):
                if cell == 1:
                    screen.blit(muro, (x * lato_quad, y * lato_quad))
                else:
                    screen.blit(pavimento, (x * lato_quad, y * lato_quad))
                    testo = font.render(f"{k}", True, (0, 0, 0))
                    text_rect = testo.get_rect(center=(x * lato_quad + lato_quad - 15, y * lato_quad + 15))
                    screen.blit(testo, text_rect)
                    k += 1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        pygame.display.flip()

        #carico la matrice
        for indice_riga, riga in enumerate(mappa):
            for indice_colonna, casella in enumerate(riga):
                if matrice[indice_riga][indice_colonna] > -1:
                    matrice[indice_riga][indice_colonna] = k
                    
                    


    pygame.quit()


if __name__ == '__main__':
    main()