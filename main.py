import pygame
pygame.init()


WIDTH = 500
HEIGHT = 500
CEN_X = WIDTH//2
CEN_Y = HEIGHT//2
FPS = 60
missiles = []


root = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()


if __name__ == "__main__":
	from screen import start_screen, game_screen
	game_screen()