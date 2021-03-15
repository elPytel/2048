# By Pytel
"""
Funkce pro hru 2048.
"""
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
		for row in self.board:
			for col in row:
				col = 0
	
	def ResetGame (self):
		self.ResetBoard()
		self.score = 0
		self.end = False
		
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
		
	# Vygeneruje nove hodnoty
	# Vytvoři seznam volnych pozic.
	# Jednu z nich nahodne vybere a nahraje na ni "2"		
	def SpawnNext (self):
		free = []
		for y in range(self.size):
			for x in range(self.size):
				if self.board[y][x] == 0:
					free.append([y,x])
		#print(free)
		if len(free) > 0:
			coord = random.choice(free)
			self.board[coord[0]][coord[1]] = 2
		else:
			self.end = True
			
	def getCol (self, index):
		col = []
		for row in self.board:
			col.append(row(index))
		return col
		
	def setCol (self, index, col):
		for i in range(self.size):
			self.board[i][index] = col[i]
		
	def getRow (self, index):
		return self.board[index]
		
	def setRow (self, index, row):
		self.board[index] = row
			
	def Execute (self, move):
		board = self.board
		if move == "w":
			for x in range(self.size):
				for y in range(self.size-1):
					if board[y+1][x] == 0:
						continue
					if board[y][x] == 0:
						board[y][x] = board[y+1][x]
						board[y+1][x] = 0
					if board[y][x] == board[y+1][x]:
						board[y][x] = board[y][x]*2
						board[y+1][x] = 0
		
		elif move == "s":
			for x in range(self.size):
				for y in range(self.size-1, 0, -1):
					#print("y:", y,"x:",x)
					if board[y-1][x] == 0:
						continue
					if board[y][x] == 0:
						board[y][x] = board[y-1][x]
						board[y-1][x] = 0
					if board[y][x] == board[y-1][x]:
						board[y][x] *= 2
						board[y-1][x] = 0
		
		# TODO
		elif move == "a":
			for y in range(self.size):
				for x in range(self.size-1):
					if board[y][x+1] == 0:
						continue
					if board[y][x] == 0:
						board[y][x] = board[y][x+1]
						board[y][x+1] = 0
					if board[y][x] == board[y][x+1]:
						board[y][x] *= 2
						board[y][x+1] = 0
		
		elif move == "d":
			for y in range(self.size):
				for x in range(self.size-1, 0, -1):
					if board[y][x-1] == 0:
						continue
					if board[y][x] == 0:
						board[y][x] = board[y][x-1]
						board[y][x-1] = 0
					if board[y][x] == board[y][x-1]:
						board[y][x] *= 2
						board[y][x-1] = 0
		
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
		
	def Print (self):
		print(" --- Game board ---")
		for row in self.board:
			print(row)
		
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