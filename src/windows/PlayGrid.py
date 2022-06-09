from enum import Enum
import math

class gamemode(Enum):
    Dame = 0
    Bauernschach = 1
    Tictactoe = 2
    
class grid:
    #    ------>
    #    width (x)
    # |h [0,0] [0,1] [0,2]
    # |e [1,0] [1,1] [1,2]
    # |i [2,0] [2,1] [2,2]
    # |g etc.
    # |h
    # |t
    # V(y)
    _grid: list = []
    _height = -1
    _width = -1
    _gamemode: gamemode

    def __init__(self, height, width, game: gamemode):
        self._height = height
        self._width = width
        self._gamemode = game
        self.initGrid()
        
    def initGrid(self):
        length = self._height * self._width
        if self._gamemode == gamemode.Dame:
            index = 0
            placePiece = False
            for i in range(self._width):
                coord = self.getCoordByIndex(index)
                if placePiece:
                    self._grid.append(playPieceDame(coord[0], coord[1], 0))
                else:
                    self._grid.append(playPiece(coord[0], coord[1]))
                placePiece = not placePiece
                index += 1
            placePiece = True
            for i in range(self._width):
                coord = self.getCoordByIndex(index)
                if placePiece:
                    self._grid.append(playPieceDame(coord[0], coord[1], 0))
                else:
                    self._grid.append(playPiece(coord[0], coord[1]))
                placePiece = not placePiece
                index += 1
            for i in range(self._width*(self._height-4)):
                coord = self.getCoordByIndex(index)
                self._grid.append(playPiece(coord[0], coord[1]))
                index += 1
            placePiece = False
            for i in range(self._width):
                coord = self.getCoordByIndex(index)
                if placePiece:
                    self._grid.append(playPieceDame(coord[0], coord[1], 1))
                else:
                    self._grid.append(playPiece(coord[0], coord[1]))
                placePiece = not placePiece
                index += 1
            placePiece = True
            for i in range(self._width):
                coord = self.getCoordByIndex(index)
                if placePiece:
                    self._grid.append(playPieceDame(coord[0], coord[1], 1))
                else:
                    self._grid.append(playPiece(coord[0], coord[1]))
                placePiece = not placePiece
                index += 1
                
        elif self._gamemode == gamemode.Bauernschach:
            index = 0
            for i in range(self._width):
                coord = self.getCoordByIndex(index)
                self._grid.append(playPieceBauernschach(coord[0], coord[1], 0))
                index += 1
            for i in range(self._width*(self._height-2)):
                coord = self.getCoordByIndex(index)
                self._grid.append(playPiece(coord[0], coord[1]))
                index += 1
            for i in range(self._width):
                coord = self.getCoordByIndex(index)
                self._grid.append(playPieceBauernschach(coord[0], coord[1], 1))
                index += 1
                
        elif self._gamemode == gamemode.Tictactoe:
            for i in range(length):
                coord = self.getCoordByIndex(index)
                self._grid.append(playPiece(coord[0], coord[1]))
        
    def getGrid(self):
        return self._grid

    def setGrid(self, grid):
        self._grid = grid
        
    def getCoordByIndex(self, index):
        return [index%self._width,math.floor(index / self._width)]

    def getCellByCoord(self, xpos, ypos):
        if not self.coordInsideGrid(xpos, ypos):
            return -1
        return self._grid[xpos + ypos * self._width]
    
    def getCellByIndex(self, index):
        if index > 0 and index < len(self._grid):
            return self._grid[index]
        return -1
    
    def getGridAsString(self):
        str = ""
        index = 0
        for i in self._grid:
            if isinstance(i, playPiece):
                if i.getColor() == 0:
                    str += "P1, "
                elif i.getColor() == 1:
                    str += "P2, "
                else:
                    str += "None, "
                index += 1
                if not (index < self._width):
                    print(str)
                    str = ""
                    index = 0
                 
    def coordInsideGrid(self, xpos, ypos):
        if xpos > 0 and xpos < self._width and ypos > 0 and ypos < self._height:
            return True
        return False
    
    def getMovesOfPiece(self, xpos, ypos):
        temp = self.getCellByCoord(xpos, ypos)
        if self._gamemode == gamemode.Dame:
            if isinstance(temp, playPieceDame):
                possibleCaptures: bool = False
                for i in self._grid:
                    if isinstance(i, playPieceDame):
                        if i.canCapturePiece(self):
                            possibleCaptures = True
                return temp.moves(self, possibleCaptures)
            else:
                return []
        elif self._gamemode == gamemode.Bauernschach:
            if isinstance(temp, playPieceBauernschach):
                return temp.moves(self)
            else:
                return []
            
                
                
    
class playPiece:
    _color = -1 # -1 sind unbelegte Felder
    _xpos = -1
    _ypos = -1
    
    def __init__(self, xpos, ypos, color = -1):
        self._xpos = xpos
        self._ypos = ypos
        self._color = color
        
    def moves(self, grid: grid):
        movelist = []
        return movelist
    
    def getColor(self):
        return self._color
    
    def getCoord(self):
        return [self._xpos, self._ypos]
    
class playPieceDame(playPiece):
    def _init_(self, xpos, ypos, color = -1):
        super().__init__(self, xpos, ypos, color)
        
    def moves(self, grid: grid, possibleCaptures: bool): # überschreibt die vererbte moves-Funktion
        movelist = []
        offset = [[-1,-1],[-1,1],[1,-1],[1,1]]
        for i in offset:
            xposoffset = self._xpos + i[0]
            yposoffset = self._ypos + i[1]
            temp = grid.getCellByCoord(xposoffset, yposoffset)
            if isinstance(temp, playPiece):
                if temp.getColor() != self.getColor():
                    xposoffset += i[0]
                    yposoffset += i[1]
                    temp = grid.getCellByCoord(xposoffset, yposoffset)
                    if isinstance(temp, playPiece):
                        if temp.getColor() == -1:
                            movelist.append([xposoffset,yposoffset])
                elif temp.getColor() == -1 and not possibleCaptures:
                    movelist.append([xposoffset,yposoffset])
        return movelist
    
    def canCapturePiece(self, grid: grid):
        offset = [[-1,-1],[-1,1],[1,-1],[1,1]]
        for i in offset:
            xposoffset = self._xpos + i[0]
            yposoffset = self._ypos + i[1]
            temp = grid.getCellByCoord(xposoffset, yposoffset)
            if isinstance(temp, playPiece):
                if temp.getColor() != self.getColor():
                    xposoffset += i[0]
                    yposoffset += i[1]
                    temp = grid.getCellByCoord(xposoffset, yposoffset)
                    if isinstance(temp, playPiece):
                        if temp.getColor() == -1:
                            return True
        return False
    
class playPieceBauernschach(playPiece):
    def _init_(self, xpos, ypos, color = -1):
        super().__init__(self, xpos, ypos, color)
        
    def moves(self, grid: grid): # überschreibt die vererbte moves-Funktion
        movelist = []
        xposoffset = self._xpos
        yposoffset = self._ypos
        if self._color == 0:
            yposoffset += 1
        else:
            yposoffset -= 1
        temp = grid.getCellByCoord(xposoffset, yposoffset)
        if isinstance(temp, playPiece):
            if temp.getColor() == -1:
                movelist.append([xposoffset, yposoffset])
        
        temp = grid.getCellByCoord(xposoffset - 1, yposoffset)
        if isinstance(temp, playPiece):
            if temp.getColor() != -1 and temp.getColor() != self._color:
                movelist.append([xposoffset - 1, yposoffset])
                
        temp = grid.getCellByCoord(xposoffset + 1, yposoffset)
        if isinstance(temp, playPiece):
            if temp.getColor() != -1 and temp.getColor() != self._color:
                movelist.append([xposoffset + 1, yposoffset])
        return movelist
    
class playPieceTictactoe(playPiece):
    def _init_(self, xpos, ypos, color = -1):
        super().__init__(self, xpos, ypos, color)
        
    def moves(self, grid: grid): # überschreibt die vererbte moves-Funktion
        movelist = []
        return movelist