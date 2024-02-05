import pygame

# inizializza pygame: chiamare sempre per prima
pygame.init()

# finestra principale (prende come parametro una tupla con le dimensioni)
screen = pygame.display.set_mode((800, 600))

pygame.draw.circle(screen, "red", (200, 200), 120)

# aggiorna lo schermo dopo che abbiamo disegnato su screen
pygame.display.flip()

#termina correttamente il programma
input("Premi INVIO per terminare il programma")
pygame.quit()