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

	# Missile(50, 20, 3, 0)

	# from main import createPlayer
	# createPlayer()
	# from main import Player

	Player = Plane(250, 250, 2, 0)

	ground = pygame.image.load('assets/ground_tile.png')
	global gr
	gr = ground.get_rect()

	# print(gr.w)


	@Screen
	def move_handler():

		# bg = pygame.image.load('assets/sky.jpg')
		# root.blit(bg, (0, 0))

		root.fill((255, 255, 255))
		
		ga = Player.sa%91
		ga = round(ga)
		ga = ga-91

		for i in range(6):
			root.blit(ground, (ga+(i*gr.w), 500-gr.h))

		keys = pygame.key.get_pressed()
		if keys[pygame.K_LEFT]:
			Player.dirn -= 2
		elif keys[pygame.K_RIGHT]:
			Player.dirn += 2

		Player.update_cart_vel()
		Player.move()
		Player.draw()
 
		for missile in missiles:
			missile.update_vel(Player)
			missile.move()
			missile.draw()

	move_handler()

