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
game.PrintGame()

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
Predelat padani, tak aby se cisla neposouvaly jen o jedno pole, ale aspadli az dolu!
END
"""
