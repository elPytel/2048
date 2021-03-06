# By Pytel
"""
Hra 2048.
Ovladani je pomoci WASD.
"""
import Game
import Player

DEBUG = False

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
	print("What is your name?: ", end =" ")
	name = input()
	game.SaveScore(name)
	
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
