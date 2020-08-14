import pygame
pygame.init()


# from glob_var import *

WIDTH = 500
HEIGHT = 500
CEN_X = WIDTH//2
CEN_Y = HEIGHT//2
FPS = 60
missiles = []


root = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

def createPlayer():
	from classes import Plane
	global Player
	Player = Plane(250, 250, 2, 0)

if __name__ == "__main__":
	from screen import start_screen, game_screen
	game_screen()