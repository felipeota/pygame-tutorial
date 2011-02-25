import pygame
import time

pygame.init()

# Open pygame window
window_h = 450
window_w = 600
screen = pygame.display.set_mode((window_w, window_h))
screen.fill((0,0,255))

# load some assets
background_image = pygame.image.load("assets/background.jpg")
object_image = pygame.image.load("assets/faller_003.png")

object_position = [0,0]

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
  if exit:
    break
 
  current_time = time.time()
  if current_time - start_time <= frame_time:
    continue
  start_time = current_time

  # draw the background first, to erase everything that was behind 
  screen.blit(background_image, (0,0))
  # draw everything else over the background
  screen.blit(object_image, object_position)
  
  # Move the object around the screen
  object_position[0] = (object_position[0] + 3)%window_w
  object_position[1] = (object_position[1] + 5)%window_h
  
  pygame.display.update()
pygame.quit()