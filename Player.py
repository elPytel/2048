import curses
# By Pytel and Guly
"""
Funkce hrace pro hru 2048.
"""

#from curses import has_key
#curses.BUTTON1_PRESSED
#instance of int

MOVE = ['w', 's', 'a', 'd']
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

import curses
stdscr = curses.initscr()
try:
	stdscr.scrollok(True)
	curses.noecho()
	curses.cbreak()

	stdscr.addstr('Stiskni q pro konec\n')
	ch = stdscr.getch()
	while ch != ord('q'):
		stdscr.addstr('To nebylo ono\n')
		ch = stdscr.getch()
	
finally:
	curses.nocbreak()
	curses.echo()
	curses.endwin()
"""