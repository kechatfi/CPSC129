# life_gui_0.py
#
# Graphical user interface for Conway's Game of Life.
import pygame
import sys
import time
import random

# Colour definitions.
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
TEAL = (0, 128, 128)
YELLOW = (255, 255, 0)
GREY = (128,128,128)
SILVER = (192, 192, 192)

pygame.init()

U_ROWS = 25 # rows in the Life universe.
U_COLS = 40 # cols in the Life universe.

live_cell = pygame.image.load("Aqua-Ball-icon.png")
cell_size = 16
grid_size = cell_size + 1 # + 1 allows for 1 pixel border on LHS of cell.

SCREEN_BORDER = 10
SCREEN_HEIGHT = U_ROWS*grid_size + 1 + 2*SCREEN_BORDER # + 1 allows for 1 pixel border on RHS of screen.
SCREEN_WIDTH = U_COLS*grid_size + 1 + 2*SCREEN_BORDER 
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
screen.fill(BLACK)
pygame.display.flip()


# Draw horizontal lines.
for y in range(0, U_ROWS+1):
    pygame.draw.line(screen, GREY, (SCREEN_BORDER, SCREEN_BORDER + y*grid_size),
                     (SCREEN_WIDTH - SCREEN_BORDER - 1, SCREEN_BORDER + y*grid_size))

# Draw vertical lines.
for x in range(0, U_COLS+1):
    pygame.draw.line(screen, GREY, (SCREEN_BORDER + x*grid_size, SCREEN_BORDER),
                     (SCREEN_BORDER + x*grid_size, SCREEN_HEIGHT - SCREEN_BORDER - 1))
pygame.display.flip()

for i in range(1,100):
    # + 1s below move past LH borderline, below upper borderline.
    screen.blit(live_cell, (SCREEN_BORDER + random.randint(0, U_COLS-1)*grid_size+1,
                            SCREEN_BORDER + random.randint(0, U_ROWS-1)*grid_size+1))
pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
