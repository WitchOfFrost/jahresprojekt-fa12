import algo.sharedVariables as sharedVariables
from math import inf
from spiele.playGrid import *
import copy


# This function is the implementation of Minimax with Alpha-Beta Pruning.
# If heuristic variable is set to "HISTORY", it will perform move ordering using History Heuristics.
# Otherwise, it will not perform move ordering.
def alpha_beta(grid:grid, depth, alpha, beta, max_player):
    
    sharedVariables.NODE_COUNTER += 1

    # Check if at depth 0 or if current state is game over.
    if depth == 0 or grid.getWinner() != -1:
        #return current game status
        if max_player:
            return grid.evaluateBoard(1) #match ist durch
        else:
            return grid.evaluateBoard(0)

    # Get possible moves.
    moves:array
    if max_player:
        moves = grid.getAllMoves(1)
    else:
        moves = grid.getAllMoves(0)


    # Perform Minimax with Alpha-Beta Pruning.
    if max_player:
        # Initialize variable.
        max_evaluation = -inf

        for child in moves:
            # Increment node counter.
            sharedVariables.NODE_COUNTER += 1

                
            temp = copy.deepcopy(grid)
            if temp._gamemode == gamemode.Tictactoe:
                temp.placeTicTacToePiece(child[0], child[1], 1)
            else:
                temp.moveCellByCoord(child[0], child[1], child[2], child[3])

            # Recursive call.
            evaluation = alpha_beta(temp, depth - 1, alpha, beta, False)
            max_evaluation = max(max_evaluation, evaluation)
            alpha = max(alpha, evaluation)

            # This is the Alpha-Beta cutoff. Increment counter cutoff counter.
            if beta <= alpha:
                sharedVariables.CUTOFF_COUNTER += 1
                break


        # Return the evaluation of the move.
        return max_evaluation
    else:
        # Initialize variable.
        min_evaluation = inf

        for child in moves:
            # Increment node counter.
            sharedVariables.NODE_COUNTER += 1

            
                
            temp = copy.deepcopy(grid)
            if temp._gamemode == gamemode.Tictactoe:
                temp.placeTicTacToePiece(child[0], child[1], 1)
            else:
                temp.moveCellByCoord(child[0], child[1], child[2], child[3])
                
            # Recursive call.
            evaluation = alpha_beta(temp, depth - 1, alpha, beta, True)
            min_evaluation = min(min_evaluation, evaluation)
            beta = min(beta, evaluation)

            # This is the Alpha-Beta cutoff. Increment counter cutoff counter.
            if beta <= alpha:
                sharedVariables.CUTOFF_COUNTER += 1
                break


        # Return the evaluation of the move.
        return min_evaluation
    
# position.get_game_end: Überprüft, ob der Status des Spiels auf "Ende" steht
# position.evaluate_state: Gibt den Endwert des Spiels aus (weiß/schwarz hat mit x Punkten gewonnen)
# position.get_next_moves: ruft die Methode get_next_moves auf, diese generiert ein neues Spielfeld (grid) auf dem der Algorithmus die moves testet
# position.set_evaluation: startet einen neuen Run der Evaluation (tests auf dem test-grid)
# max_evaluation, min_evaluation: ermittelter Wert der Evaluation