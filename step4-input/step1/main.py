import pygame
import time

pygame.init()

# Open pygame window
window_h = 450
window_w = 600
screen = pygame.display.set_mode((window_w, window_h))

# load some assets
background_image = pygame.image.load("assets/background.jpg")
character_image = pygame.image.load("assets/character.png")

# character data
character_position = [0, window_h - character_image.get_height()]
direction = 0

start_time = time.time()
fps = 30
frame_time = 1.0/fps

# Main loop
exit = False
while not exit:
  # Process pygame events
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      exit = True
      break
    # Handle movement for the character
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_LEFT:
        direction = -1
      elif event.key == pygame.K_RIGHT:
        direction = 1
    if event.type == pygame.KEYUP:
      if (event.key == pygame.K_LEFT and direction == -1) or\
        (event.key == pygame.K_RIGHT and direction == 1):
        direction = 0
  if exit:
    break
  
  current_time = time.time()
  if current_time - start_time <= frame_time:
    continue
  start_time = current_time
  
  # draw the background first, because it will cover all the screen 
  screen.blit(background_image, (0,0))
  # draw everything else over the background
  screen.blit(character_image, character_position)
  
  # Move the character around the screen
  character_position[0] = (character_position[0] + direction*8)%window_w
  
  pygame.display.update()

pygame.quit()
