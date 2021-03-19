# By Pytel
"""
Funkce hrace pro hru 2048.
"""
import Input

MOVE = ["w","a","s","d"]
DEBUG = True

class Player:
	
	#def __init__ (self):
	
	def Move (self):
		while True != False:
			key = Input._Getch()
			#key = input()
			if DEBUG:
				print(key)
			if key in MOVE:
				return key
			elif key == 'q':
				return key

"""
END
"""