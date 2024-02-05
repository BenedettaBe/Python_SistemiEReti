import random
import pygame
from pygame.locals import *

#classe per il bird
class Bird(pygame.sprite.Sprite):
        def __init__(self, x,y):
           pygame.sprite.Sprite.__init__(self) 
           self.images = []
           self.index = 0
           self.counter = 0 #variabile per controllare la velocità per il cambio di immagine
           self.vel = 0 #variabile per controllare il volo del bird contando anche la gravita


            #aggiungo tutte le immagini relative al bird in una lista di immagini
           self.images.append(pygame.image.load('birdVolo.png'))
           self.images.append(pygame.image.load('birdSu.png'))
           self.images.append(pygame.image.load('birdGiu.png'))
           
           self.image = self.images[self.index]#prima immagine
        #creo rettangolo per il bird e lo disegno nelle cordinate passate alla funzione
           self.rect = self.image.get_rect()
           self.rect.center = [x, y]

        #aggiorno l'immagine 
        def update(self, input):
            #simulo il volo
            self.counter += 1
            if self.counter > 7: 
                self.counter = 0
                if self.index < 2:
                    self.index += 1
                else:
                    self.index =0
            self.image = self.images[self.index]

            #il birbd vola in alto se premo il pulsante altrimenti la forza di gravità lo fa scendere
            self.vel += 0.5
            if self.vel > 5:
              self.vel = 5
            if self.rect.y < 425:
               self.rect.y += int(self.vel)
            
            if input[pygame.K_SPACE] and self.rect.y > 0:
                self.vel = -7
        
        def draw(self, screen):
            screen.blit(self.image, (self.rect.x, self.rect.y))
            
class Nemico(pygame.sprite.Sprite):
    def __init__(self, x, y,):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('missile.png')
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]

    def update(self):
        #missile che si muove
        self.rect.x -= 1
        if self.rect.x <= 1:
            self.kill()

def main(): 
    clock = pygame.time.Clock() 
    fps = 50
    p = 0

    WIDTH = 500 #larghezza schermo
    HEIGHT = 500 #altezza schermo
    x_pavimento = 0 #utilizzo una variabile per poter simulare lo scorrimento del pavimento
    cont = 130 #contatore per distanziare i missili
    collision = False
            
    #carico lo sfondo
    sfondo = pygame.image.load('giorno.png')
    pavimento = pygame.image.load('pavimento.png')

    #creo schermo
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Flappy Bird')           

    #creo il bird
    bird = Bird(100, int(HEIGHT /2))

    #creo gruppo missili
    missili_group = pygame.sprite.Group()
    m1 = Nemico(400, 80)
    missili_group.add(m1)

    run = True
    while run:
        clock.tick(fps)

        if collision == False:
        #disegno sfondo
            screen.blit(sfondo, (0,0)) 

            #disegno pavimento che si muove
            screen.blit(pavimento, (x_pavimento,425))
            x_pavimento -= 1
            if abs(x_pavimento) > 60:
                x_pavimento = 0
            
            #memorizza il tasto premuto
            input = pygame.key.get_pressed() 
            #disegno il bird
            bird.draw(screen)
            bird.update(input)

            #se il bird tocca per terra il giocatore perde
            if bird.rect.bottom > 425:
                collision = True

            #disegno i missili
            for missile in missili_group:
                if cont == 0:
                    y = random.randint(20, 400)
                    m1 = Nemico(499, y)
                    missili_group.add(m1)
                    cont = 130
                cont -= 1
                missili_group.draw(screen)
                missili_group.update()
                if bird.rect.colliderect(missile.rect): #controllo collisioni
                    collision = True
                else: 
                    p +=1
            
        else:
            screen.blit(pygame.image.load('gameOver.png'), (0,0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        pygame.display.update() #aggiorna lo schermo
    
if __name__ == "__main__" : 
    main()