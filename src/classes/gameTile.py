from projectConfig import *

class gameTile():
    def __init__(self, id, total, size):
        self.state = 0  # 0 = Empty, 1 = Player, 2 = AI
        self.id = id  # ID of the Tile, starting in the upper left corner going to the bottom right
        self.row = int((total - id) / size ) + 1 # Row Position, Top row is labeled as the highest number
        self.size = projectConfig["tileSize"]