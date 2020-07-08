from globals import *
from math import sin, cos, radians
class GameObject:

	def __init__(self, x, y, v, dirn):
		self.x = x
		self.y = y
		self.v = v
		self.dirn = 0
		self.w = 20
		self.h = 20
		self.update_vel()

	def draw(self):
		pygame.draw.rect(root, (255, 0, 0), (self.x, self.y, self.w, self.h))

	def move(self):
		self.update_vel()
		self.x += self.vx
		self.y += self.vy

	def update_vel(self):
		self.vx = self.v*cos(radians(self.dirn))
		self.vy = self.v*sin(radians(self.dirn))
