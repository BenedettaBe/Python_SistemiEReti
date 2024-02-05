import pygame

pygame.init()

SCREEN_WIDTH = 800 #larghezza schermo
SCREEN_HEIGHT = 600 #altezza schermo

#creo lo schermo
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Prova rettangolo')

player = pygame.Rect((300, 250, 50, 50)) #rettangolo

run = True #variabile per il ciclo while
while run:
    screen.fill((0,0,0))

    pygame.draw.rect(screen, (255, 0 ,0), player) #disegna rettangolo(dove, colore, quale)

    key = pygame.key.get_pressed() #memorizza il tasto premuto
    if key[pygame.K_a]: #sinistra
        player.move_ip(-1, 0)
    elif key[pygame.K_d]: #destra
        player.move_ip(1, 0)
    elif key[pygame.K_w]: #su
        player.move_ip(0, -1)
    elif key[pygame.K_s]: #giù
        player.move_ip(0, 1)

    for event in pygame.event.get(): #cerco degli eventi all'interno del gioco
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()#aggiorna lo schermo

pygame.quit()