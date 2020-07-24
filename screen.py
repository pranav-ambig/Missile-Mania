from glob_var import *
from classes import GameObject, Plane, Missile

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

	Missile(20, 250, 3, 0)

	@Screen
	def move_handler():
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

