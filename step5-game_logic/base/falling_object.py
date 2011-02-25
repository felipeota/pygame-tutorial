import pygame
from random import randint

fallers_size = 6
fallers = ["assets/faller_001.png", 
          "assets/faller_002.png", 
          "assets/faller_003.png", 
          "assets/faller_004.png", 
          "assets/faller_005.png",
          "assets/faller_006.png" ]

class FallingObject:
  def __init__(self, screen_w, screen_h, unit):
    self.unit = unit
    self.image = pygame.image.load(fallers[randint(0, fallers_size - 1)]);
    image_rect = self.image.get_rect()
    # Begin with a random horizontal position at the top
    self.position = [randint(0, screen_w - image_rect.width), -image_rect.height]
    self.screen_h = screen_h
    
  def update(self):
    self.position[1] += 4*self.unit;
  
  def draw(self, on_surface):
    on_surface.blit(self.image, self.position)

  def died(self):
    return self.position[1] > self.screen_h
