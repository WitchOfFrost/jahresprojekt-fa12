from projectConfig import *

from classes.gameTile import gameTile

class gameGrid():
    def __init__(self):
        self.totalTiles = projectConfig["gridSize"] * projectConfig["gridSize"]
        self.grid = {}
        i = 0

        while(i != self.totalTiles):
            i += 1
            self.grid[i] = gameTile(i, self.totalTiles, projectConfig["gridSize"])
            print(self.grid[i].__dict__)
