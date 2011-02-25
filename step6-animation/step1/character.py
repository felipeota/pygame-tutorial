import pygame
from animation import Animation, Frame
from time import time

class Character:

  def __init__(self, screen_w, screen_h, unit):
    self.unit = unit
    self.create_animations()
    image_rect = self.animation.get_current_frame().image.get_rect()
    self.center = image_rect.width/2
    self.position = [(screen_w - image_rect.width)/2, screen_h - image_rect.height]
    size_reduction = 10*unit
    self.collision_rect = pygame.Rect(image_rect.left + size_reduction, 
      image_rect.top + size_reduction,
      image_rect.width - 2*size_reduction, 
      image_rect.height - 4*size_reduction)
    self.screen_w = screen_w
    self.direction = [0, 0]
    
  def create_animations(self):
    image = pygame.image.load("assets/character.png")
    
    # create the frames for the "walking left" animation
    frames = [
      Frame(image = image, position = [0, 4*self.unit], duration = 4),
      Frame(image = image, position = [0, 0],           duration = 4),
    ]

    # and with that create the "walking left" animation
    self.animation = Animation(frames)
    
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
    if self.direction[0] != 0:
      self.animation.update()
    self.position[0] = (self.position[0] + self.direction[0]*8*self.unit + self.center)\
      %self.screen_w - self.center
  
  def draw(self, on_surface):
    self.animation.draw(on_surface, self.position)
   
  def collides_with(self, other):
    return self.get_absolute_rect().colliderect(other.get_absolute_rect())
  
  def get_absolute_rect(self):
    return self.collision_rect.move(self.position)
