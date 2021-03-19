# By Pytel
"""
Funkce hrace pro hru 2048.
"""
import Input

MOVE = ["w","a","s","d"]
DEBUG = True

class Player:
	
	def __init__ (self):
		self.sc = Input._Getch()
	
	def Move (self):
		while True != False:
			key = self.sc.impl()
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