import pygame

pygame.init()

# Open pygame window
window_h = 450
window_w = 600
screen = pygame.display.set_mode((window_w, window_h))

# Main loop
exit = False
while not exit:
  # Process pygame events
  for event in pygame.event.get():
    if event.type == pygame.QUIT or \
      (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
      exit = True
      break
  if exit:
    break

pygame.quit()

