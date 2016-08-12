"""
 Pygame base template for opening a window

 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/

 Explanation video: http://youtu.be/vRB_983kUMc
"""

import pygame
from pygame import *
import random

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


pygame.init()

# Set the width and height of the screen [width, height]
size = [400, 400]
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Snow")


speed=1

snow_list = []

	

for i in range(50):
	x = random.randrange(0, 400)
	y = random.randrange(0, 400)
	snow_list.append([x, y])
 
clock = pygame.time.Clock()

done = False



	#def __init__(self, size, position, wind=False):
		
		#def fall(self, speed):
		
			
	
        #Uses pygame and the global screen variable to draw the snowflake on the screen
        
        



# Used to manage how fast the screen updates




# Speed


#INITIALIZE YOUR SNOWFLAKE HERE! 

# Snow List


# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # --- Game logic should go here
	
    # --- Screen-clearing code goes here

    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.

    screen.fill(BLACK)  

    # --- Drawing code should go here
    # Begin Snow
 
    for i in range(len(snow_list)):
       
	    pygame.draw.circle(screen, WHITE, snow_list[i], 2)
        
	    snow_list[i][1] += 1
		
		
    if snow_list[i][1] > 400:
		
            
            y = random.randrange(-50, -10)
            snow_list[i][1] = y
		
            x = random.randrange(0, 400)
            snow_list[i][0] = x



    


    # End Snow
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(20)

# Close the window and quit.
pygame.quit()
exit() # Needed when using IDLE
