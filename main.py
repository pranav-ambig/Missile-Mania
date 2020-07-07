import pygame

pygame.init()

WIDTH = 500
HEIGHT = 500

root = pygame.display.set_mode((WIDTH, HEIGHT))

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			quit()

	root.fill((255, 255, 255))
	pygame.display.update()

