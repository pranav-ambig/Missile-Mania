from globals import *
from classes import GameObject

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
	x = GameObject(50, 50, 2, 0)

	@Screen
	def move_handler():
		root.fill((255, 255, 255))
		keys = pygame.key.get_pressed()
		if keys[pygame.K_LEFT]:
			x.dirn -= 2
		elif keys[pygame.K_RIGHT]:
			x.dirn += 2 

		x.move()
		x.draw()

	move_handler()

