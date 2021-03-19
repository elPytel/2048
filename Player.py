import curses
# By Pytel and Guly
"""
Funkce hrace pro hru 2048.
"""

from curses import has_key
#curses.BUTTON1_PRESSED
#instance of int

MOVE = []
EX = []
MOVE[0] = curses.KEY_UP
MOVE[1] = curses.KEY_DOWN
MOVE[2] = curses.KEY_LEFT
MOVE[3] = curses.KEY_RIGHT
EX[0] = curses.KEY_EXIT


DEBUG = False

class Player:
	
	#def __init__ (self):
	
	def Move (self):
		while True != False:
			key = input()
			if DEBUG:
				print(key)
			if key in MOVE:
				return key
			elif key in EX:
				return key

"""
END
"""