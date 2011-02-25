import pygame

class Character:
  def __init__(self, screen_w, screen_h, unit):
    self.unit = unit
    self.image = pygame.image.load("assets/character.png")
    image_rect = self.image.get_rect()
    self.position = [(screen_w - image_rect.width)/2, screen_h - image_rect.height]
    self.screen_w = screen_w
    self.direction = [0, 0]
    
  def input(self, event):
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_LEFT:
        self.direction[0] = -1
      elif event.key == pygame.K_RIGHT:
        self.direction[0] = 1
    if event.type == pygame.KEYUP:
      if (event.key == pygame.K_LEFT and self.direction[0] == -1) or\
        (event.key == pygame.K_RIGHT and self.direction[0] == 1):
        self.direction[0] = 0
  
  def update(self):
    image_center = self.image.get_width()/2
    self.position[0] = (self.position[0] + self.direction[0]*8*self.unit + image_center)\
      %self.screen_w - image_center
  
  def draw(self, on_surface):
    on_surface.blit(self.image, self.position)