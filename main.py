# By Pytel
"""
Hra 2048.
Ovladani je pomoci WASD.
"""
import Game
import Player

size = 4
game = Game.Game(size)
game.NewGame()
game.ResetGame()
#game.PrintGame()

game.Logo()

player = Player.Player()

while not game.End():
	game.SpawnNext()
	game.Print()
	move = player.Move()
	print("Move:", move)
	game.Execute(move)
	game.Evaluate()

print(" ---Game end ---")
print(" Game score:", game.Score())		# game score



"""
Predelat na zadavani po jednotlivych znacich.
END
"""
