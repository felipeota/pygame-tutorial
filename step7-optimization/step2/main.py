import pygame
import time
from falling_object import FallingObject
from character import Character

pygame.init()

# Open pygame window
window_h = 900
window_w = 1200
unit = 2
screen = pygame.display.set_mode((window_w, window_h))

# load some assets
background_image = pygame.image.load("assets/background.jpg").convert()

# the lose_sign is now a Sprite
lose_sign = pygame.sprite.Sprite()
lose_sign.image = pygame.image.load("assets/lose.png").convert_alpha()
lose_sign.rect = lose_sign.image.get_rect()
lose_sign.layer = 0

# start with the background on the screen
screen.blit(background_image, (0, 0))
pygame.display.update()

# the character of the game
character = Character(window_w, window_h, unit)

# Object falling generation interval
object_generation_ticks = 45
last_generation_tick = 0

# Falling objects are now a Group, to get the convenient update method and
# when an object is killed it will be removed automatically
falling_objects = pygame.sprite.Group()

# This group will contain every renderable object.
# we will use it to redraw very little
renderables = pygame.sprite.LayeredUpdates()
renderables.add(character)

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
 
  # limit framerate
  pygame.time.delay(5)
  current_time = time.time()
  if current_time - start_time <= frame_time:
    continue
  start_time = current_time
  
  # Clear the screen before updating anything
  renderables.clear(screen, background_image)
  
  if not lost_game:
    
    # If enough time passed generate a new object
    if last_generation_tick == 0:
      last_generation_tick = object_generation_ticks
      new_object = FallingObject(window_w, window_h, unit)
      falling_objects.add(new_object)
      renderables.add(new_object)
    else:
      last_generation_tick -= 1

    # update objects
    falling_objects.update()
    character.update()

    # Remove objects that "died"
    for object in falling_objects.sprites():
      if object.died():
        object.kill()
    
    # check collisions
    for object in falling_objects.sprites():
      if character.collides_with(object):
        lost_game = True
        renderables.add(lose_sign)
        break
  
  # Draw after updating everything
  dirty = renderables.draw(screen)
  
  pygame.display.update(dirty)
  
pygame.quit()
