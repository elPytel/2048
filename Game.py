# By Pytel
"""
Funkce pro hru 2048.
"""
import Score
import random

MOVE = ["w","a","s","d"]
DEBUG = True

class Game:
	
	def __init__ (self, size):
		self.size = size
		self.board = []
		self.score = 0
		self.max_score = 0
		self.end = False
		
		self.logo = "logo.txt"
		self.file_score = ".score.txt"
		self.scoreBoard = None
		
	def ImportScore (self):
		scb = Score.ScoreBoard()
		scb.Import(self.file_score)
		self.scoreBoard = scb
		
	def ExportScore (self):
		self.scoreBoard.Export(self.file_score)
		
	def SaveScore (self, name):
		self.scoreBoard.add(self.size, name, self.score)
		
	def GenerateBoard (self):
		board = []
		for y in range(self.size):
			row = []
			for x in range(self.size):
				col = 0
				row.append(col)
			board.append(row)
		return board
		
	def ResetBoard (self):
		for y in range(self.size):
			for x in range(self.size):
				self.board[y][x] = 0
		"""
		for row in self.board:
			for col in row:
				col = 0
		"""
	
	def ResetGame (self):
		self.ResetBoard()
		self.score = 0
		self.end = False
		if DEBUG:
			print("Reset was performed")
		
	def NewGame (self):
		self.board = self.GenerateBoard()
		self.score = 0
		
	def Evaluate (self):
		free = []
		for y in range(self.size):
			for x in range(self.size):
				if self.board[y][x] == 0:
					free.append([y,x])
		if len(free) < 1:
			self.end = True
			self.score = self.Score()
		
	# Vygeneruje nove hodnoty
	"""
	Vytvoři seznam volnych pozic.
	Jednu z nich nahodne vybere a nahraje na ni "2"
	"""		
	def SpawnNext (self):
		free = []
		for y in range(self.size):
			for x in range(self.size):
				if self.board[y][x] == 0:
					free.append([y,x])
		#print(free)
		if len(free) > 0:
			number = random.choice([2, 4])
			coord = random.choice(free)
			self.board[coord[0]][coord[1]] = number
		else:
			self.end = True
			
	def getCol (self, index):
		col = []
		for row in self.board:
			col.append(row[index])
		return col
		
	def setCol (self, index, col):
		for i in range(self.size):
			self.board[i][index] = col[i]
		
	def getRow (self, index):
		return self.board[index]
		
	def setRow (self, index, row):
		self.board[index] = row
		
	# provede tah na jednom radku
	"""
	Kolabs je smerem v pravo, =>
	"""
	def ExecuteLine (self, line):
		# odstrani mezery
		for i in range(line.count(0)):
			line.remove(0)
		
		# spoji stejna cisla
		i = len(line)-1
		while i > 0:
			if DEBUG and 0:
				print("l[i]:", line[i], "	l[i-1]:", line[i-1])
			if line[i] == line[i-1]:
				line[i-1] = line[i-1]+line.pop(i)
				i = i -2
			else:
				i = i -1
		#print(line)
		
		# nastavi spravnou delku
		while len(line) != self.size:
			line.insert(0, 0)
			
		return line
			
	def Execute (self, move):
		board = self.board
		if move == "w":
			for i in range(self.size):
				line = self.getCol(i)
				line.reverse()
				if DEBUG and 0:
					print("Next line:")
					print(line)
				line = self.ExecuteLine(line)
				line.reverse()
				self.setCol(i, line)
		elif move == "s":
			for i in range(self.size):
				line = self.getCol(i)
				line = self.ExecuteLine(line)
				self.setCol(i, line)
		elif move == "a":
			for i in range(self.size):
				line = self.getRow(i)
				line.reverse()
				line = self.ExecuteLine(line)
				line.reverse()
				self.setRow(i, line)
		elif move == "d":
			for i in range(self.size):
				line = self.getRow(i)
				line = self.ExecuteLine(line)
				self.setRow(i, line)
		elif move == "q":
			self.end = True;
			self.score = self.Score()
		else:
			print("ERROR: invalid move!")
			
	def End (self):
		return self.end
		
	def Score (self):
		score = 0
		for row in self.board:
			for col in row:
				score += col;
		return score
		
	def getScore (self):
		return self.score
	
	def Logo (self):
		file = open(self.logo, 'r',  encoding='utf-8')
		
		print()
		for line in file.readlines():
			print(line, end =" ")
		print()
		file.close()
			
	def Print (self):
		print(" --- Game board ---")
		for row in self.board:
			print(row)
			
	def PrintScore (self):
		self.scoreBoard.Print(10)
		
	def PrintGame (self):
		print(" --- Game ---")
		print(" Size:	", self.size)
		print(" Score:	", self.score)
		print(" Max score:", self.max_score)
		print(" Board:")
		print(self.board)

"""
END
"""