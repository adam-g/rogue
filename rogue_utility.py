# Class to get commands and do them
import player


class command_class:
    player = player.player(0, 0, 0)
    game_running = False
    commands = {}

    def __init__(self, player):
        self.game_running = True
        self.player = player
        self.commands = {
            'help': self.help,
            'quit': self.quit,
            'status': self.status,
            'suicide': self.suicide,
            }

    def help(self):
        print("Available commands:")
        for c in self.commands.keys():
            print(c)

    def quit(self):
        print("Exiting game...\n")
        self.game_running = False

    def suicide(self):
        print("Our hero reached for the knife and slit his own throat. WHY??")
        self.player.health = 0

    def status(self):
        print("Strength: ", self.player.strength)
        print("Attacks: ", self.player.attacks)
        print("Health: ", self.player.health)

    def get_command(self):
        while(self.game_running):
            line = input("Enter command> ")
            args = line.split()
            if len(args) > 0:
                commandFound = False
                for c in self.commands.keys():
                    if args[0] == c[:len(args[0])]:
                        self.commands[c]()
                        commandFound = True
                        break
                if not commandFound:
                    print("Invalid command, try again.\n")
            if(self.player.health < 1):
                print("Sadly our hero has died, try again")
                self.game_running = False
