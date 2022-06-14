from array import array
import algo.ki as ki
from spiele.playGrid import grid, gamemode, playPiece
from enum import Enum
# from algo import ki

import copy
import math
import pygame
pygame.init()

class gamestate(Enum):
    Player1Turn = 0
    Player2Turn = 1
    Exit = 2
    Player1Win = 3
    Player2Win = 4
    
grid_size = 100
spr_emptyGrid = pygame.transform.scale(pygame.image.load("src/assets/sprites/empty.png"), (grid_size, grid_size))
spr_emptyMove = pygame.transform.scale(pygame.image.load("src/assets/sprites/emptyMove.png"), (grid_size, grid_size))
spr_grid1 = pygame.transform.scale(pygame.image.load("src/assets/sprites/grid1.png"), (grid_size, grid_size))
spr_grid1Capture = pygame.transform.scale(pygame.image.load("src/assets/sprites/grid1Capture.png"), (grid_size, grid_size))
spr_grid1Selected = pygame.transform.scale(pygame.image.load("src/assets/sprites/grid1Selected.png"), (grid_size, grid_size))
spr_grid2 = pygame.transform.scale(pygame.image.load("src/assets/sprites/grid2.png"), (grid_size, grid_size))
spr_grid2Capture = pygame.transform.scale(pygame.image.load("src/assets/sprites/grid2Capture.png"), (grid_size, grid_size))
spr_grid2Selected = pygame.transform.scale(pygame.image.load("src/assets/sprites/grid2Selected.png"), (grid_size, grid_size))
    
class Spielesammlung:
    
    gm: gamemode
    difficulty:int
    wins = 0
    bg_color = (192, 192, 192)
    grid_color = (128, 128, 128)
    game_width = 6
    game_height = 6
    buttonList = []
    border = 16
    top_border = 100
    display_width = grid_size * game_width + border * 2
    display_height = grid_size * game_height + border + top_border
    gameDisplay = pygame.display.set_mode((display_width, display_height))
    timer = pygame.time.Clock()
    pygame.display.set_caption("Bauernschach")
    
    currentSelectedCell = [-1,-1]
    allMovesOfPiece = []
    
    
    def __init__(self, mode, difficulty):
        self.difficulty = difficulty
        if mode == "Bauernschach":
            self.gm = gamemode.Bauernschach
        elif mode == "Dame":
            self.gm = gamemode.Dame
        elif mode == "TicTacToe":
            self.gm = gamemode.Tictactoe
        self.gameGrid = grid(self.game_height, self.game_width, self.gm)
        
    def drawText(self,txt, s, yOff=0):
        screen_text = pygame.font.SysFont("Calibri", s, True).render(txt, True, (0, 0, 0))
        rect = screen_text.get_rect()
        rect.center = (self.game_width * grid_size / 2 + self.border, self.game_height * grid_size / 2 + self.top_border + yOff)
        self.gameDisplay.blit(screen_text, rect)
        
    def drawGrid(self):
        for i in range(self.game_height):
            for j in range(self.game_width):
                currCell = self.gameGrid.getCellByCoord(i,j)
                if isinstance(currCell, playPiece):
                    color = currCell.getColor()
                    if color == 0:
                        canBeCaptured = False
                        for x in self.allMovesOfPiece:
                            if x == [i,j]:
                                canBeCaptured = True
                                self.gameDisplay.blit(spr_grid1Capture, currCell.getRect())
                        if not canBeCaptured:
                            if [i,j] == self.currentSelectedCell:
                                self.gameDisplay.blit(spr_grid1Selected, currCell.getRect())
                            else:
                                self.gameDisplay.blit(spr_grid1, currCell.getRect())
                    elif color == 1:
                        canBeCaptured = False
                        for x in self.allMovesOfPiece:
                            if x == [i,j]:
                                canBeCaptured = True
                                self.gameDisplay.blit(spr_grid2Capture, currCell.getRect())
                        if not canBeCaptured:
                            if [i,j] == self.currentSelectedCell:
                                self.gameDisplay.blit(spr_grid2Selected, currCell.getRect())
                            else:
                                self.gameDisplay.blit(spr_grid2, currCell.getRect())
                    else:
                        canBeMovedTo = False
                        for x in self.allMovesOfPiece:
                            if x == [i,j]:
                                canBeMovedTo = True
                                self.gameDisplay.blit(spr_emptyMove, currCell.getRect())
                        if not canBeMovedTo:        
                            self.gameDisplay.blit(spr_emptyGrid, currCell.getRect())
                else:
                    print("Fehler: Zugriff außerhalb des Grids")
                        
    def getClickedPlayPiece(self, event:pygame.event) -> playPiece | None:
        for i in range(self.game_height):
            for j in range(self.game_width):
                currCell = self.gameGrid.getCellByCoord(i,j)
                if isinstance(currCell, playPiece):
                    if currCell.getRect().collidepoint(event.pos):
                        return currCell
        return None
    
    def clickedPieceinMoveArray(self, coord: array) -> bool:
        for i in self.allMovesOfPiece:
            if i == coord:
                return True
        return False
        
    def mainLoopBauernschach(self):
        currentGamestate = gamestate.Player1Turn
        t = 0
        self.gameGrid.setAllRect(self.border, self.top_border, grid_size)
        while currentGamestate != gamestate.Exit:
            self.gameDisplay.fill(self.bg_color)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT: # falls das Fenster geschlossen wird
                    currentGamestate = gamestate.Exit
                else:
                    if currentGamestate == gamestate.Player1Turn and event.type == pygame.MOUSEBUTTONUP and event.button == 1:# Linksklick
                        currCell = self.getClickedPlayPiece(event)
                        currCellCoord = currCell.getCoord()
                        if isinstance(currCell,playPiece):
                            if self.currentSelectedCell == [-1,-1]:
                                    print(currCell.getColor())
                                    if currCell.getColor() == 0:
                                        self.currentSelectedCell = currCellCoord
                                        self.allMovesOfPiece = self.gameGrid.getMovesOfPiece(self.currentSelectedCell[0], self.currentSelectedCell[1])
                                    print(self.currentSelectedCell)
                            elif self.clickedPieceinMoveArray(currCellCoord):
                                temp = self.currentSelectedCell
                                self.currentSelectedCell = [-1, -1]
                                self.allMovesOfPiece = []
                                gameWon = self.gameGrid.moveCellByCoord(temp[0], temp[1], currCellCoord[0], currCellCoord[1])
                                self.gameGrid.setAllRect(self.border, self.top_border, grid_size)
                                if gameWon == 0 or gameWon == 2:
                                    currentGamestate = gamestate.Player1Win
                                    self.wins += 1
                                elif gameWon == 1:
                                    currentGamestate = gamestate.Player2Win
                                else:
                                    gameWon = self.performKIMove()
                                    if gameWon == 0:
                                        currentGamestate = gamestate.Player1Win
                                        self.wins += 1
                                    elif gameWon == 1 or gameWon == 2:
                                        currentGamestate = gamestate.Player2Win
                                    self.gameGrid.setAllRect(self.border, self.top_border, grid_size)
                                
                            elif currCell.getColor() == 0:
                                self.currentSelectedCell = currCellCoord
                                self.allMovesOfPiece = self.gameGrid.getMovesOfPiece(self.currentSelectedCell[0], self.currentSelectedCell[1])
                            else:
                                self.currentSelectedCell = [-1, -1]
                                self.allMovesOfPiece = []
                    elif currentGamestate == gamestate.Player1Win or currentGamestate == gamestate.Player2Win:
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_r:
                                currentGamestate = gamestate.Exit
                                self.gameGrid.resetGrid()
                                self.mainLoopBauernschach()
                            elif event.key == pygame.K_x:
                                currentGamestate = gamestate.Exit
                                
                                            

            self.drawGrid()
            if currentGamestate == gamestate.Player1Turn or currentGamestate == gamestate.Player2Turn:
                t += 1
            elif currentGamestate == gamestate.Player1Win:
                self.drawText("Player 1 WON!", 50)
                self.drawText("R to Restart or x to Exit", 35, 50)
            elif currentGamestate == gamestate.Player2Win:
                self.drawText("Player 2 WON!", 50)
                self.drawText("R to Restart or x to Exit", 35, 50)
            s = str(t // 15)
            screen_text = pygame.font.SysFont("Calibri", 50).render(s, True, (0, 0, 0))# Timer anzeigen/updaten
            self.gameDisplay.blit(screen_text, (self.border, self.border))
            screen_text = ""

            pygame.display.update()  # Das Fenster aktualisieren

            self.timer.tick(15)  # fps
            
    def mainLoopDame(self):
        currentGamestate = gamestate.Player1Turn
        t = 0
        self.gameGrid.setAllRect(self.border, self.top_border, grid_size)
        while currentGamestate != gamestate.Exit:
            self.gameDisplay.fill(self.bg_color)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT: # falls das Fenster geschlossen wird
                    currentGamestate = gamestate.Exit

                else:
                    if currentGamestate == gamestate.Player1Turn and event.type == pygame.MOUSEBUTTONUP and event.button == 1:# Linksklick
                        currCell = self.getClickedPlayPiece(event)
                        currCellCoord = currCell.getCoord()
                        if isinstance(currCell,playPiece):
                            if self.currentSelectedCell == [-1,-1]:
                                    print(currCell.getColor())
                                    if currCell.getColor() != -1:
                                        self.currentSelectedCell = currCellCoord
                                        self.allMovesOfPiece = self.gameGrid.getMovesOfPiece(self.currentSelectedCell[0], self.currentSelectedCell[1])
                                    print(self.currentSelectedCell)
                            elif self.clickedPieceinMoveArray(currCellCoord):
                                temp = self.currentSelectedCell
                                self.currentSelectedCell = [-1, -1]
                                self.allMovesOfPiece = []
                                gameWon = self.gameGrid.moveCellByCoord(temp[0], temp[1], currCellCoord[0], currCellCoord[1])
                                if gameWon == 0:
                                    currentGamestate = gamestate.Player1Win
                                    self.wins += 1
                                elif gameWon == 1:
                                    currentGamestate = gamestate.Player2Win
                                else:
                                    self.gameGrid.setAllRect(self.border, self.top_border, grid_size)
                                    gameWon = self.performKIMove()
                                    if gameWon == 0:
                                        currentGamestate = gamestate.Player1Win
                                        self.wins += 1
                                    elif gameWon == 1:
                                        currentGamestate = gamestate.Player2Win
                                    self.gameGrid.setAllRect(self.border, self.top_border, grid_size)
                            elif currCell.getColor()  != -1:
                                self.currentSelectedCell = currCellCoord
                                self.allMovesOfPiece = self.gameGrid.getMovesOfPiece(self.currentSelectedCell[0], self.currentSelectedCell[1])
                            else:
                                self.currentSelectedCell = [-1, -1]
                                self.allMovesOfPiece = []
                    elif currentGamestate == gamestate.Player1Win or currentGamestate == gamestate.Player2Win:
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_r:
                                currentGamestate = gamestate.Exit
                                self.gameGrid.resetGrid()
                                self.mainLoopDame()
                            elif event.key == pygame.K_x:
                                currentGamestate = gamestate.Exit
                                
                                            

            self.drawGrid()
            if currentGamestate == gamestate.Player1Turn or currentGamestate == gamestate.Player2Turn:
                t += 1
            elif currentGamestate == gamestate.Player1Win:
                self.drawText("Player 1 WON!", 50)
                self.drawText("R to Restart or x to Exit", 35, 50)
            elif currentGamestate == gamestate.Player2Win:
                self.drawText("Player 2 WON!", 50)
                self.drawText("R to Restart or x to Exit", 35, 50)
            s = str(t // 15)
            screen_text = pygame.font.SysFont("Calibri", 50).render(s, True, (0, 0, 0))# Timer anzeigen/updaten
            self.gameDisplay.blit(screen_text, (self.border, self.border))
            screen_text = ""

            pygame.display.update()  # Das Fenster aktualisieren

            self.timer.tick(15)  # fps
            
    def mainLoopTicTacToe(self):
        currentGamestate = gamestate.Player1Turn
        t = 0
        self.gameGrid.setAllRect(self.border, self.top_border, grid_size)
        while currentGamestate != gamestate.Exit:
            self.gameDisplay.fill(self.bg_color)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT: # falls das Fenster geschlossen wird
                    currentGamestate = gamestate.Exit
                else:
                    if currentGamestate == gamestate.Player1Turn and event.type == pygame.MOUSEBUTTONUP and event.button == 1:# Linksklick
                        currCell = self.getClickedPlayPiece(event)
                        currCellCoord = currCell.getCoord()
                        if isinstance(currCell,playPiece):
                            if currCell.getColor() == -1:
                                gameWon = self.gameGrid.placeTicTacToePiece(currCellCoord[0], currCellCoord[1], 0)
                                self.gameGrid.setAllRect(self.border, self.top_border, grid_size)
                                if gameWon == 0:
                                    currentGamestate = gamestate.Player1Win
                                    self.wins += 1
                                elif gameWon == 1:
                                    currentGamestate = gamestate.Player2Win
                                else:
                                    gameWon = self.performKIMove()
                                    if gameWon == 0:
                                        currentGamestate = gamestate.Player1Win
                                        self.wins += 1
                                    elif gameWon == 1:
                                        currentGamestate = gamestate.Player2Win
                                    self.gameGrid.setAllRect(self.border, self.top_border, grid_size)
                    elif currentGamestate == gamestate.Player1Win or currentGamestate == gamestate.Player2Win:
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_r:
                                currentGamestate = gamestate.Exit
                                self.gameGrid.resetGrid()
                                self.mainLoopTicTacToe()
                            elif event.key == pygame.K_x:
                                currentGamestate = gamestate.Exit

            self.drawGrid()
            if currentGamestate == gamestate.Player1Turn or currentGamestate == gamestate.Player2Turn:
                t += 1
            elif currentGamestate == gamestate.Player1Win:
                self.drawText("Player 1 WON!", 50)
                self.drawText("R to Restart or x to Exit", 35, 50)
            elif currentGamestate == gamestate.Player2Win:
                self.drawText("Player 2 WON!", 50)
                self.drawText("R to Restart or x to Exit", 35, 50)
            s = str(t // 15)
            screen_text = pygame.font.SysFont("Calibri", 50).render(s, True, (0, 0, 0))# Timer anzeigen/updaten
            self.gameDisplay.blit(screen_text, (self.border, self.border))
            screen_text = ""

            pygame.display.update()  # Das Fenster aktualisieren

            self.timer.tick(15)  # fps
            
    def useAlgo(self) -> array: # Rückgabewert muss ein Array mit dieser Form sein: [startx, starty, endx, endy] und für TicTacToe: [xplazieren, yplazieren]
        moves = self.gameGrid.getAllMoves(1)
        maxEval = -math.inf
        bestMove = []
        for child in moves:
            temp = copy.deepcopy(self.gameGrid)
            if self.gm == gamemode.Tictactoe:
                temp.placeTicTacToePiece(child[0], child[1], 1)
            else:
                temp.moveCellByCoord(child[0], child[1], child[2], child[3])
            currEval = ki.alpha_beta(temp, 4, -(math.inf), math.inf, False)
            if currEval > maxEval:
                maxEval = currEval
                bestMove = child
        if bestMove == []:
            bestMove = moves[0]
        return bestMove
    
    def performKIMove(self) -> int:
        kIMove = self.useAlgo()
        if self.gm == gamemode.Tictactoe:
            return self.gameGrid.placeTicTacToePiece(kIMove[0], kIMove[1], 1)
        else:
            return self.gameGrid.moveCellByCoord(kIMove[0], kIMove[1], kIMove[2], kIMove[3])
    
    def gameloop(self) -> int:
        
        if self.gm == gamemode.Bauernschach:
            self.mainLoopBauernschach()
        elif self.gm == gamemode.Dame:
            self.mainLoopDame()
        elif self.gm == gamemode.Tictactoe:
            self.mainLoopTicTacToe()
            
        pygame.quit()
        return self.wins #test
