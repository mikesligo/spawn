import pygame,sys
from pygame.locals import *

pygame.init()

def aspectratio(val):
    return val * 16 / 9

side = 640
size = width, height = aspectratio(side), (side)
screen = pygame.display.set_mode(size)
background = (27,27,40)
gridcolour = (0x42,0xFF,0x49)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    screen.fill(background)
    grid = pygame.draw.rect(screen, gridcolour,(aspectratio(20),20,aspectratio(600),600))
    mainborder = pygame.draw.rect(screen, background,(aspectratio(21),21,aspectratio(598),598))

    leftgrid = pygame.draw.rect(screen, gridcolour,(aspectratio(21),21,aspectratio(159),599))
    leftborder = pygame.draw.rect(screen, background,(aspectratio(21),21,aspectratio(158),598))

    rightgrid = pygame.draw.rect(screen, gridcolour,(aspectratio(440),21,aspectratio(159),599))
    rightborder = pygame.draw.rect(screen, background,(aspectratio(441),21,aspectratio(158),598))
    pygame.display.flip()
