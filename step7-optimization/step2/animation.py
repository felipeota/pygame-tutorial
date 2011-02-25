from math import floor

class Animation(): 
    
  def __init__(self, frames, repeat=True):
    self.frames = frames
    self.current_time = 0
    self.current_frame = 0
    total_time = 0
    self.stage = None
    for frame in frames:
      total_time += frame.duration
    self.to = total_time     
    self.repeat = repeat
    self.last_frame_time = 0

  def update(self, interval=1):
    current_time = self.current_time
    current_time += interval
    current_frame = self.current_frame
    last_frame_time = self.last_frame_time
    to = self.to
    if (current_time > to):
      factor = current_time/to
      current_time =  (factor - floor(factor))*to
      current_frame = 0
      last_frame_time = 0
      if not self.repeat:
        self.stop()
        self.reset()
        return
    while self.frames[current_frame].duration + last_frame_time < current_time:
      last_frame_time += self.frames[current_frame].duration
      current_frame += 1
    self.current_frame = current_frame
    self.current_time = current_time
    self.last_frame_time = last_frame_time

  def reset(self):
    self.current_frame = 0
    self.current_time = 0
    self.last_frame_time = 0

  def get_current_frame(self):
    return self.frames[self.current_frame]
    
  def draw(self, on_surface, position):
    self.get_current_frame().draw(on_surface, position)
   
  def update_sprite(self, sprite, position):
    self.get_current_frame().update_sprite(sprite, position)
        
class Frame():

  def __init__(self, image, position, duration):
    self.image = image
    self.position = position
    self.duration = duration
  
  def draw(self, on_surface, position):
    absolute_pos = [position[0] + self.position[0],
                    position[1] + self.position[1]]
    on_surface.blit(self.image, absolute_pos)
  
  def update_sprite(self, sprite, position):
    sprite.image = self.image
    sprite.rect = self.image.get_rect().move(position).move(self.position)
