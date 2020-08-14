# from glob_var import *
from main import WIDTH, HEIGHT, CEN_X, CEN_Y, FPS, missiles, root, clock
from classes import GameObject, Plane, Missile
import pygame

def Screen(func):

	def wrapper(*args, **kwargs):
		while True:
			clock.tick(FPS)
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					quit()

			func(*args, **kwargs)
			pygame.display.update()

	return wrapper

@Screen
def start_screen():
	root.fill((255, 255, 255))

def game_screen():

	Missile(50, 20, 3, 0)

	@Screen
	def move_handler():
		from main import createPlayer
		createPlayer()
		from main import Player
		root.fill((255, 255, 255))
		keys = pygame.key.get_pressed()
		if keys[pygame.K_LEFT]:
			Player.dirn += 2
		elif keys[pygame.K_RIGHT]:
			Player.dirn -= 2

		Player.update_cart_vel()
		Player.draw()

		for missile in missiles:
			missile.update_vel(Player)
			missile.move()
			missile.draw()

	move_handler()

