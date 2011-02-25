import pygame
import time
from falling_object import FallingObject
from character import Character

pygame.init()

# Open pygame window
window_h = 450
window_w = 600
unit = 1.0
screen = pygame.display.set_mode((window_w, window_h))

# load some assets
background_image = pygame.image.load("assets/background.jpg")

# the character of the game
character = Character(window_w, window_h, unit)

fps = 30
frame_time = 1.0/fps
start_time = time.time()

fallers = []
creation_tick_interval = 45
creation_tick_count = 0

# Main loop
exit = False
while not exit:
  # Process pygame events
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      exit = True
      break
    # Handle character input
    character.input(event)
  if exit:
    break
 
  current_time = time.time()
  if current_time - start_time <= frame_time:
    continue
  start_time = current_time
 
  if creation_tick_count == 0:
    creation_tick_count = creation_tick_interval
    fallers.append(FallingObject(window_w, window_h, unit))
  else:
    creation_tick_count -= 1

  for faller in fallers:
    faller.update()
  character.update()
  
  for faller in fallers:
    if faller.died():
      fallers.remove(faller)

  # draw the background first, because it will cover all the screen 
  screen.blit(background_image, (0,0))
  
  for faller in fallers:
    faller.draw(screen)
  character.draw(screen)
  
  pygame.display.update()

pygame.quit()
