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

# Objects falling generation interval
object_generation_ticks = 45
last_generation_tick = 0

falling_objects = []

fps = 30
frame_time = 1.0/fps
start_time = time.time()

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

  # If enough time passed generate a new object
  if last_generation_tick == 0:
    last_generation_tick = object_generation_ticks
    falling_objects.append(FallingObject(window_w, window_h, unit))
  else:
    last_generation_tick -= 1

  # update objects
  for object in falling_objects:
    object.update()
  character.update()

  # Remove objects that "died"
  for object in falling_objects:
    if object.died():
      falling_objects.remove(object)
    
  # draw the background first, because it will cover all the screen 
  screen.blit(background_image, (0,0))
  
  # draw everything else over the background
  for object in falling_objects:
    object.draw(screen)
  character.draw(screen)
  
  pygame.display.update()

pygame.quit()
