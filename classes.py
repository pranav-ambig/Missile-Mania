from glob_var import *
from math import sin, cos, radians, degrees, atan

class GameObject:

	def __init__(self, x, y, v, dirn):
		self.x = x
		self.y = y
		self.v = v
		self.dirn = 0
		self.w = 20
		self.h = 20
		self.update_cart_vel()

	def draw(self):
		pygame.draw.rect(root, (255, 0, 0), (self.x, self.y, self.w, self.h))

	def update_cart_vel(self):
		self.vx = self.v*cos(radians(self.dirn))
		self.vy = self.v*sin(radians(self.dirn))

class Plane(GameObject):

	def __init__(self, x, y, v, dirn):
		super().__init__(x, y, v, dirn)

class Missile(GameObject):

	def __init__(self, x, y, v, dirn):
		super().__init__(x, y, v, dirn)
		missiles.append(self)

	def move(self):
		self.x += self.vx
		self.y += self.vy

	def update_dirn(self):
		dx = CEN_X-self.x
		dy = CEN_Y-self.y
		if dx == 0:
			dx = 0.01
		self.dirn = degrees(atan(dy/dx))

		if (self.x or self.y) > CEN_X:
			self.dirn += 180


	def update_vel(self, p: Plane):
		self.update_dirn()
		super().update_cart_vel()
		self.vx -= p.vx
		self.vy -= p.vy

