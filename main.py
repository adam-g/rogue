#This is some kind of class
import rogue_utility
import player


# Instantiate the player and put him in the first room
def setup(current_map, player):
	print("First room")


def main(current_map, player):
	game_on = True
	comm = rogue_utility.command_class(player)

	while(comm.game_running):
		print("Hello world")
		comm.get_command()


current_map = []
player = player.player(strength=1337, attacks=2, health=1000)
setup(current_map, player)
main(current_map, player)
