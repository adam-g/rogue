#	This is some kind of class

# Instantiate the player and put him in the first room
def setup():
	print("First room")


def main():
	game_on = True

	while(game_on):
		print("Hello world")
		game_on = False


current_map = []
player = None
setup(current_map, player)
main(current_map, player)