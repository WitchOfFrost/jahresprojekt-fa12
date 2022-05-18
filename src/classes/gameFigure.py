import exceptions.InvalidPlayerType as InvalidPlayerType

# TODO: Add Logic for players, bind to player movements

class gameFigure():
    def __init__(self, type, position):
        self.type = type # Figure type, yellow = AI (Player 2), red = Player
        if(self.type == "red"):
            self.position = position
        elif(self.type == "yellow"):
            self.position = position
        else:
            raise InvalidPlayerType("Player type " + type + " is not a valid type!")