import pygame

def set(x, y):
    pygame.init()
    screen = pygame.display.set_mode((x, y))
    pygame.display.set_caption("gioco")

def termina():
    input("Premi INVIO per terminare il programma")
    pygame.quit()


def main(): 
    set(800, 600)
    
    termina()

if __name__ == "__main__" : 
    main()