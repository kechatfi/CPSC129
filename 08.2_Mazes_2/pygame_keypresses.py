# http://gpwiki.org/index.php/Python:Pygame_keyboard_input

import pygame
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption('Pygame Caption')
pygame.mouse.set_visible(0)


done = False
while not done:
   for event in pygame.event.get():
      if event.type == pygame.QUIT:
         done = True
      elif (event.type == KEYUP) or (event.type == KEYDOWN):
         print(event)
         if (event.key == K_ESCAPE):
            done = True
pygame.quit()
