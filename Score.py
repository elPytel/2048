# By Pytel

import os

DEBUG = True

class Score:
	
	def __init__ (self, size, name, score):
		self.size = size
		self.name = name
		self.score = score
		
	def Print (self):
		print("Size:", self.size, "\tName:", self.name, "\tscore:", self.score)

class ScoreBoard:
		
	def __init__ (self):
		self.data = []
		
	def add (self, size, name, score):
		score = Score(size, name, score)
		self.data.append(score)
		# tohle je sice pomaly, ale co se da delat
		"""ut.sort(key=lambda x: x.count, reverse=True)"""
		self.data.sort(key=lambda x: x.score)
		
	def parse (self, string):
		array = string.split()
		if DEBUG:
			print("Parsed:", array)
		size = int(array[1])
		name = array[3]
		score = int(array[5])
		return [size, name, score]
		
	def Import (self, file):
		# existuje?
		file_exists = os.path.isfile(file)
		if file_exists:		# vytvori pokud neexistuje
			file = open(file, 'r', encoding='utf-8')
			for line in file.readlines():
				array = self.parse(line)
				score = Score(array[0], array[1], array[2])
				self.data.append(score)
			file.close()
		
	def Export (self, file):
		file = open(file, 'w', encoding='utf-8')
		# TODO tohle je osklivy
		for score in self.data:
			file.write("Size: " + str(score.size) + " Name: " + str(score.name) + " Score: " + str(score.score) + " \n")
		
		file.close()
	
	def Print (self, number):
		if number > len(self.data):
			number = len(self.data)
			
		for i in range(number):
			score = self.data[i]
			score.Print()
		
	
"""
END
"""
