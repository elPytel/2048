# By Pytel
"""
Funkce hrace pro hru 2048.
"""

MOVE = ["w","a","s","d"]
DEBUG = False

class Player:
	
	#def __init__ (self):
	
	def Move (self):
		while True != False:
			key = input()
			if DEBUG:
				print(key)
			if key in MOVE:
				if DEBUG:
					print("You presed: ", key)
				return key

"""
END
"""