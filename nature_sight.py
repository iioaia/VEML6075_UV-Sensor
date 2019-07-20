import unicornhathd
import colorsys
import time
import random
from random import randint
from time import sleep




# UnicornHat HD  Settings

unicornhathd.brightness(0.05)


# Simulating UV readings in Int

def var():
	global x, y
	x = random.randint(0, 15)
	y = random.randint(0, 15)


# Setting the pixel from the UV reading. 

def uvsensor(x, y):
	uvar = x
	uvbr = y
	unicornhathd.set_pixel(x, y, 0, 50, 244)
	print "Initial Reading X" ,uvar
	print "Initial Reading Y" ,uvbr
	
	# print "X and Y from the randomint!"
	






# Main 

running = True    # Easier to understand for newcomers
try:
	while running:
			var()
			uvsensor(x, y)
			unicornhathd.show()
			sleep(3)
			unicornhathd.off()

            
			
except KeyboardInterrupt:
	unicornhathd.off()









