# By Pytel and Guly
"""
Funkce hrace pro hru 2048.
"""
import curses
stdscr = curses.initscr()
#from curses import has_key
#curses.BUTTON1_PRESSED
#instance of int

MOVE = [ord('w'), ord('s'), ord('a'), ord('d')]
DEBUG = False

class Player:
	stdscr = curses.initscr()
	#def __init__ (self):
	
	def Move (self):
		while True != False:
			key = stdscr.getch()
			if DEBUG:
				print(key)
			if key in MOVE:
				return key
			elif key == ord('q'):
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
			stdscr.addstr('To nebylo ono\n')
			ch = stdscr.getch()
	
	finally:
		curses.nocbreak()
		curses.echo()
		curses.endwin()

"""
END
"""