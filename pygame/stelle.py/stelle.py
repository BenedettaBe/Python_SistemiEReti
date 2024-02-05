import random
import math
import pygame
import sys
 
WIN_SIZE     = [800, 600]
STARS_CENTER = [400, 300]
NUM_STARS    = 150
 
def init_star():
    vel_MIN = 1.0
    vel_MAX = 5.0
    
    direzione = random.uniform(0, 2*math.pi)
    velocità  = random.uniform(vel_MIN, vel_MAX)
    
    vel_X = math.sin(direzione)*velocità
    vel_Y = math.cos(direzione)*velocità
    
    return [vel_X, vel_Y], STARS_CENTER[:]
 
def initialize_stars():
    stars = []
    for x in range(NUM_STARS):
        star = init_star()
        stars.append(star)
    return stars
 
def draw_stars(surface, stars, color):
    for vel, pos in stars:
        pos = (int(pos[0]), int(pos[1]))
        surface.set_at(pos, color)
 
def move_stars(stars):
    for vel, pos in stars:
        pos[0]=pos[0]+vel[0]
        pos[1]=pos[1]+vel[1]
        if not (0 <= pos[0] <= WIN_SIZE[0]) or not (0 <= pos[1] <= WIN_SIZE[1]):
            vel[:], pos[:] = init_star()
        else:
            vel[0]=vel[0]*1.05
            vel[1]=vel[1]*1.05
 
def main():  
    pygame.init()
    SCREEN=pygame.display.set_mode(WIN_SIZE)
    pygame.display.set_caption("pygame: Stars Example")
    clock=pygame.time.Clock()

    WHITE=(255, 240, 200)
    BLACK=(20, 20, 40)

    STARS=initialize_stars()
    while True:
        for e in pygame.event.get():
            if(e.type == pygame.QUIT) or (e.type == pygame.KEYUP and e.key == pygame.K_ESCAPE):
                pygame.quit()
                sys.exit()
            elif(e.type == pygame.MOUSEBUTTONDOWN) and (e.button == 1):
                STARS_CENTER[:]=list(e.pos)

        SCREEN.fill(BLACK)
        move_stars(STARS)
        draw_stars(SCREEN, STARS, WHITE)
        pygame.display.update() 
        clock.tick(30)

if(__name__ == "__main__"):
    main()