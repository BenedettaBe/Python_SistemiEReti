import pygame
from pygame.locals import *

#classe per il bird
class Bird(pygame.sprite.Sprite):
        def __init__(self, x,y):
           pygame.sprite.Sprite.__init__(self) 
           self.images = []
           self.index = 0
           self.counter = 0 #variabile per controllare la velocità per il cambio di immagine

            #aggiungo tutte le immagini relative al bird in una lista di immagini
           self.images.append(pygame.image.load('birdVolo.png'))
           self.images.append(pygame.image.load('birdSu.png'))
           self.images.append(pygame.image.load('birdGiu.png'))
           
           self.image = self.images[self.index]#prima immagine
        #creo rettangolo per il bird e lo disegno nelle cordinate passate alla funzione
           self.rect = self.image.get_rect()
           self.rect.center = [x, y]

        #aggiorno l'immagine per simulare il volo
        def update(self, input):
            self.counter += 1
            if self.counter > 7: 
                self.counter = 0
                if self.index < 2:
                    self.index += 1
                else:
                    self.index =0
            self.image = self.images[self.index]
            if input 
            

def main(): 
    clock = pygame.time.Clock() 
    run = True

    WIDTH = 500 #larghezza schermo
    HEIGHT = 500 #altezza schermo
    x_pavimento = 0 #utilizzo una variabile per poter simulare lo scorrimento del pavimento

    #carico lo sfondo
    sfondo = pygame.image.load('giorno.png')
    pavimento = pygame.image.load('pavimento.png')

    #creo schermo
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Flappy Bird')           

    #creo il bird
    bird_group = pygame.sprite.Group()
    flappy = Bird(100, int(HEIGHT /2))
    bird_group.add(flappy)

    #creo missile
    missile = pygame.image.load('missile.png')

    
    while run:
        clock.tick(60)
        
        #disegno sfondo
        screen.blit(sfondo, (0,0)) 

        #disegno pavimento che si muove
        screen.blit(pavimento, (x_pavimento,425))
        x_pavimento -= 2
        if abs(x_pavimento) > 60:
            x_pavimento = 0

        input = pygame.key.get_pressed()#memorizzo il tasto premuto
        #disegno bird
        bird_group.draw(screen)
        bird_group.update(input)


    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        pygame.display.update() #aggiorna lo schermo

if __name__ == "__main__" : 
    main()