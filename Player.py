# By Pytel and Guly
"""
Funkce hrace pro hru 2048.
"""
import curses
#from curses import has_key
#curses.BUTTON1_PRESSED
#instance of int

MOVE = ['w', 's', 'a', 'd']
DEBUG = False

class Player:
	
	def __init__ (self):
		self.stdscr = curses.initscr()
	
	def Move (self):
		curses.noecho()
		curses.cbreak()
		while True != False:
			key = chr(self.stdscr.getch())
			
			if DEBUG:
				print(key)
			if key in MOVE:
				curses.nocbreak()
				curses.echo()
				return key
			elif key == 'q':
				curses.nocbreak()
				curses.echo()
				return key

if __name__ == '__main__':
	import curses
	stdscr = curses.initscr()
	try:
		stdscr.scrollok(True)
		curses.noecho()
		curses.cbreak()

		stdscr.addstr('Stiskni q pro konec\n')
		ch = stdscr.getch()
		while ch != ord('q'):
			stdscr.addstr('To nebylo ono \n')
			ch = stdscr.getch()
	
	finally:
		curses.nocbreak()
		curses.echo()
		curses.endwin()

"""
END
"""