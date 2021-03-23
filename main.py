# By Pytel
"""
Hra 2048.
Ovladani je pomoci WASD.
"""
import Game
import Player

DEBUG = False

def yesNo (string):
	YES = ["Yes","yes","Y","y"]
	if string in YES:
		return True
	return false

size = 4
game = Game.Game(size)
game.NewGame()
game.ImportScore()
#game.PrintGame()

game.Logo()

player = Player.Player()

while True != False:
	game.ResetGame()
	
	while not game.End():
		game.SpawnNext()
		game.Print()
		move = player.Move()
		if DEBUG:
			print(" Move: %s\r" % move)		# , end=""
		game.Execute(move)
		game.Evaluate()
	
	print(" ---Game end ---")
	print(" Game score:", game.getScore())		# game score
	
	# Skore
	# Ulozit skore?
	print("What save score?: ", end =" ")
	if yesNo(input()):
		# jak se jmenujes?
		print("What is your name?: ", end =" ")
		name = input()
		game.SaveScore(name)
	
	# vytiskne tabulku skore
	game.PrintScore()
	
	# Konec hry
	print("Press q to exit. ", end =" ")
	answer = input()
	if answer == "q":
		game.ExportScore()
		break


"""
Predelat na zadavani po jednotlivych znacich.
END
"""
