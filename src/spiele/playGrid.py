from array import array
from enum import Enum
import math
import pygame

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
    _grid: list
    _height = -1
    _width = -1
    _gamemode: gamemode

    def __init__(self, height, width, game: gamemode):
        self._height = height
        self._width = width
        self._gamemode = game
        self._grid = []
        self.initGrid()
        
    def initGrid(self):
        length = self._height * self._width
        if self._gamemode == gamemode.Dame:
            index = 0
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
            for i in range(self._width*(self._height-4)):
                coord = self.getCoordByIndex(index)
                self._grid.append(playPiece(coord[0], coord[1]))
                index += 1
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
                
                
        elif self._gamemode == gamemode.Bauernschach:
            index = 0
            for i in range(self._width):
                coord = self.getCoordByIndex(index)
                self._grid.append(playPieceBauernschach(coord[0], coord[1], 1))
                index += 1
            for i in range(self._width*(self._height-2)):
                coord = self.getCoordByIndex(index)
                self._grid.append(playPiece(coord[0], coord[1]))
                index += 1
            for i in range(self._width):
                coord = self.getCoordByIndex(index)
                self._grid.append(playPieceBauernschach(coord[0], coord[1], 0))
                index += 1
                
                
        elif self._gamemode == gamemode.Tictactoe:
            index = 0
            for i in range(length):
                coord = self.getCoordByIndex(index)
                self._grid.append(playPiece(coord[0], coord[1]))
                index += 1
        
    def setAllRect(self, border, top_border, grid_size):
        for i in self._grid:
            if isinstance(i, playPiece):
                i.setRect(border, top_border, grid_size)
        
    def getGrid(self):
        return self._grid

    def setGrid(self, grid):
        self._grid = grid
        
    def getCoordByIndex(self, index):
        return [index%self._width,math.floor(index / self._width)]
    
    def getIndexByCoord(self, xpos, ypos) -> int:
        return xpos + ypos * self._width

    def getCellByCoord(self, xpos, ypos):
        if not self.coordInsideGrid(xpos, ypos):
            return -1
        return self._grid[self.getIndexByCoord(xpos, ypos)]
    
    def getCellByIndex(self, index):
        if index > 0 and index < len(self._grid):
            return self._grid[index]
        return -1
    
    def setCellByCoord(self, xpos, ypos, cell):
        if self.coordInsideGrid(xpos, ypos) and isinstance(cell, playPiece):
            self._grid[self.getIndexByCoord(xpos, ypos)] = cell
            cell.setCoord(xpos, ypos)
            
    def moveCellByCoord(self, xpos, ypos, xendpos, yendpos) -> int:
        if self.coordInsideGrid(xpos, ypos) and self.coordInsideGrid(xendpos, yendpos):
            temp = self._grid[self.getIndexByCoord(xpos, ypos)]
            if isinstance(temp, playPiece):
                self.setCellByCoord(xendpos, yendpos, temp)
                temp.setCoord(xendpos, yendpos)
                self.setCellByCoord(xpos, ypos, playPiece(xpos, ypos))
                # self.printGridAsString()
                return self.isGameWon()
        return -1
    
    def printGridAsString(self):
        str = ""
        index = 0
        for i in self._grid:
            if isinstance(i, playPiece):
                if i.getColor() == 0:
                    str += "P1, "
                elif i.getColor() == 1:
                    str += "P2, "
                else:
                    str += "No, "
                index += 1
                if not (index < self._width):
                    print(str)
                    str = ""
                    index = 0
                 
    def coordInsideGrid(self, xpos, ypos) -> bool:
        if 0 <= xpos < self._width and 0 <= ypos < self._height:
            return True
        return False
    
    def getMovesOfPiece(self, xpos, ypos) -> array:
        temp = self.getCellByCoord(xpos, ypos)
        if self._gamemode == gamemode.Dame:
            if isinstance(temp, playPieceDame):
                color = temp.getColor()
                possibleCaptures: bool = False
                for i in self._grid:
                    if isinstance(i, playPieceDame):
                        if i.getColor() == color:
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
            
    def isGameWon(self) -> int:
        if self._gamemode == gamemode.Bauernschach or self._gamemode == gamemode.Dame:
            for i in range(self._width):
                temp = self._grid[i]
                if isinstance(temp, playPiece):
                    if temp.getColor() == 0:
                        return 0
            
            length = len(self._grid) - 1
            for i in range(length-self._width,length):
                temp = self._grid[i]
                if isinstance(temp, playPiece):
                    if temp.getColor() == 1:
                        return 1
            
            allMoves = self.getAllMoves(0) + self.getAllMoves(1)
            print(allMoves)
            if len(allMoves) == 0:
                return 2
                    
        return -1
    
    def resetGrid(self):
        self._grid = []
        self.initGrid()
        
    def placeTicTacToePiece(self, xpos, ypos, color):
        self.setCellByCoord(xpos,ypos,playPieceTictactoe(xpos, ypos, color))
        return self.isTicTacToeGameWon()
        
    def isTicTacToeGameWon(self) -> int:
        for i in self._grid:
            if isinstance(i,playPiece):
                coord = i.getCoord()
                color = i.getColor()
                if color != -1:
                    for off in [[1,0],[0,1],[1,1],[-1,1]]:
                        # print(str(off[0]) + ", " + str(off[1]))
                        xpos = coord[0] + off[0]
                        ypos = coord[1] + off[1]
                        if self.coordInsideGrid(xpos, ypos):
                            temp = self._grid[self.getIndexByCoord(xpos, ypos)]
                            if isinstance(temp,playPiece):
                                if(color == temp.getColor()):
                                    xpos = xpos + off[0]
                                    ypos = ypos + off[1]
                                    if self.coordInsideGrid(xpos, ypos):
                                        temp = self._grid[self.getIndexByCoord(xpos, ypos)]
                                        if isinstance(temp,playPiece):
                                            if(color == temp.getColor()):
                                                xpos = xpos + off[0]
                                                ypos = ypos + off[1]
                                                if self.coordInsideGrid(xpos, ypos):
                                                    temp = self._grid[self.getIndexByCoord(xpos, ypos)]
                                                    if isinstance(temp,playPiece):
                                                        if(color == temp.getColor()):
                                                            return i.getColor()
                                                    
        return -1
    
    def getWinner(self): # Gibt den aktuellen Gewinner wieder (0 -> Spieler1, 1 -> Spieler 2, -1 -> Kein Gewinner)
        if self._gamemode == gamemode.Tictactoe:
            return self.isTicTacToeGameWon()
        else:
            return self.isGameWon()
        
    def getAllMoves(self, playerColor) -> array:
        moveList = []
        if self._gamemode == gamemode.Tictactoe:
            for i in self._grid:
                if isinstance(i, playPiece):
                    coord = i.getCoord()
                    if i.getColor() == -1:
                        moveList.append([coord[0], coord[1]])
        elif self._gamemode == gamemode.Bauernschach:
            for i in self._grid:
                if isinstance(i, playPiece):
                    if i.getColor() == playerColor:
                        coord = i.getCoord()
                        movesOfPiece = self.getMovesOfPiece(coord[0], coord[1])
                        for j in movesOfPiece:
                            moveList.append([coord[0], coord[1], j[0], j[1]])
        elif self._gamemode == gamemode.Dame:
            for i in self._grid:
                if isinstance(i, playPiece):
                    if i.getColor() == playerColor:
                        coord = i.getCoord()
                        movesOfPiece = self.getMovesOfPiece(coord[0], coord[1])
                        for j in movesOfPiece:
                            moveList.append([coord[0], coord[1], j[0], j[1]])
        return moveList
    
    def evaluateBoard(self, color): # Spieler 1 auf 0 Spieler 0 auf 5
        currScore = 0
        currWinner = self.getWinner()
        pointsForPlayerPiece = 1
        pointsForEnemyPiece = 1
        if currWinner == color:
            return math.inf
        elif currWinner != -1 and currWinner != 2:
            return -(math.inf)
        else:
            for i in self._grid:
                if isinstance(i,playPiece):
                    iColor = i.getColor()
                    dist = 0
                    if iColor == 1:
                        dist = i.getCoord()[1]
                    elif iColor == 0:
                        dist = 5 - i.getCoord()[0]
                    if iColor == color:
                        currScore += pointsForPlayerPiece * dist
                    elif iColor != -1:
                        currScore -= pointsForEnemyPiece * dist
                        
        return currScore
                
                
class playPiece:
    _color = -1 # -1 sind unbelegte Felder
    _xpos = -1
    _ypos = -1
    rect = -1
    
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
    
    def setCoord(self, xpos, ypos):
        self._xpos = xpos
        self._ypos = ypos
    
    def setRect(self, border, top_border, grid_size):
        self.rect = pygame.Rect(border + self._xpos * grid_size, top_border + self._ypos * grid_size, grid_size, grid_size)
        
    def getRect(self) -> pygame.rect:
        return self.rect
    
class playPieceDame(playPiece):
    def _init_(self, xpos, ypos, color = -1):
        super().__init__(self, xpos, ypos, color)
        
    def moves(self, grid: grid, possibleCaptures: bool): # überschreibt die vererbte moves-Funktion
        print(possibleCaptures)
        movelist = []
        offset = [[-1,-1],[-1,1],[1,-1],[1,1]]
        for i in offset:
            xposoffset = self._xpos + i[0]
            yposoffset = self._ypos + i[1]
            temp = grid.getCellByCoord(xposoffset, yposoffset)
            if isinstance(temp, playPiece):
                if temp.getColor() != self.getColor() and temp.getColor() != -1:
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
                if temp.getColor() != self.getColor() and temp.getColor() != -1:
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
        if self._color == 1:
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

