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
lose_sign = pygame.image.load("assets/lose.png")

# the character of the game
character = Character(window_w, window_h, unit)

# Object falling generation interval
object_generation_ticks = 45
last_generation_tick = 0

falling_objects = []

# framerate limiter
start_time = time.time()
fps = 30
frame_time = 1.0/fps

# Main loop
exit = False
lost_game = False
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
  
  if not lost_game:
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

    # check collisions
    for object in falling_objects:
      if character.collides_with(object):
        lost_game = True
        break
    
  # draw the background first, because it will cover all the screen 
  screen.blit(background_image, (0,0))
  
  # draw everything else over the background
  for object in falling_objects:
    object.draw(screen)
  character.draw(screen)
  
  if lost_game:
    screen.blit(lose_sign, (0, 0))
  
  pygame.display.update()
  
pygame.quit()
