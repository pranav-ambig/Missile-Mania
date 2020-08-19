# from glob_var import *
from main import WIDTH, HEIGHT, CEN_X, CEN_Y, FPS, missiles, root, clock
from math import sin, cos, radians, degrees, atan
import pygame

class GameObject:

	def __init__(self, x, y, v, dirn):
		self.x = x
		self.y = y
		self.v = v
		self.dirn = dirn
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
		self.sa = 0 #scroll amount
		# self.ga = 0

	def move(self):
		if self.x >= WIDTH-self.w-20 and self.vx >  0:
			self.sa -= self.vx
		elif self.x <= self.w+20 and self.vx < 0:
			self.sa += -self.vx
		else:
			self.x += self.vx
		self.y += self.vy

		
		# self.ga = -x

		# print(self.ga)


class Missile(GameObject):

	def __init__(self, x, y, v, dirn):
		super().__init__(x, y, v, dirn)
		missiles.append(self)
		img = pygame.image.load('assets/missile1.png')
		self.img = img

	def draw(self):
		img = pygame.transform.rotate(self.img, -self.dirn)
		img_r = img.get_rect()
		img_r.center = self.x, self.y
		root.blit(img, (img_r))

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

