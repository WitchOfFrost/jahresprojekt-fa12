from projectConfig import *

from classes.gameTile import gameTile

class gameGrid():
    def __init__(self, mode):
        self.totalTiles = projectConfig["gridSize"] * projectConfig["gridSize"]
        self.grid = {}
        self.mode = mode
        i = 0
        
        while(i != self.totalTiles):
            i += 1
            self.grid[i] = gameTile(i, self.totalTiles, projectConfig["gridSize"])
            print(self.grid[i].__dict__)

        # # Bauernschach
        # if(mode == "BS"):
        #     print("Not implemented.")
        #     # TODO: Add Logic to generate Bauernschach Players and Start the game Instance
        # # Dame
        # elif(mode == "DM"):
        #     print("Not implemented.")
        #     # TODO: Add Logic to generate Dame Players and Start the game Instance
        # # Tic-Tac-Toe
        # elif(mode == "TTT"):
        #     print("Not implemented.")
        #     # TODO: Add Logic to generate Tic-Tac-Toe Players and Start the game Instance
        # else:
        #     # FIXME: Will Crash without mode, pass any mode to avoid
        #     raise InvalidModeType("Mode type " + mode + " is not a valid game mode!")