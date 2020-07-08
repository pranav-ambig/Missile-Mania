from globals import *

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
