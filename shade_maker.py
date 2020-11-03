# Create bubbles by moving the mouse.
# Rotating colors with each new Mouse (x, y) position.
# Moving the mouse in the window creates 'art'.



# MODULES / FILES
import pygame
import random



# INITIALIZE
pygame.init()
WIN_X, WIN_Y = 400, 400
window = pygame.display.set_mode((WIN_X, WIN_Y))
pygame.display.set_caption("Shade Snake")




# MAIN LOOP
run = True
while run:

	# SET MOUSE (X, Y)
	MOUSE_X, MOUSE_Y = pygame.mouse.get_pos()

	# FOR EACH EVENT...
	for event in pygame.event.get():

		# IF WINDOW CLOSES.
		if event.type == pygame.QUIT:
			run = False

		# BLACK/WHITE ONLY
		random_color = random.randint(0, 255)
		pygame.draw.circle(window, (random_color, random_color, random_color), (MOUSE_X, MOUSE_Y), 25)

	# UPDATE WINDOW
	pygame.display.update()

# if run == False, end pygame.
pygame.quit()
