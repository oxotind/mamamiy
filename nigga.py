import pygame
import random

WIDTH = 900
HEIGHT = 700

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Nigga")
clock = pygame.time.Clock()

running = True
while running:
    clock.tick(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            
            screen.fill(white)
            
            pygame.quit()
            