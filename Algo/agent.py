from copy import deepcopy
import pygame

RED_player= (255,0,0)
WHITE_player = (255, 255, 255)

def minimax(state, depth, maxi, game):
    #check if there is no end for the game 
    if depth == 0 or state.winner() != None:
        return state.evaluate(), state
    #evaluate the depth for the algorithm 
    if maxi:
        #put the max with postive infinity 
        maxScore = float('-inf')
        moveB = None
        #go recursively 
        for m in get_all_moves(state, WHITE_player, game):
            val= minimax(m, depth-1, False, game)[0]
            maxScore = max(maxScore,val)
            if maxScore == val:
                moveB = m
        
        return maxScore, moveB
    else:
        #put minmum with negative infinty 
        minScore = float('inf')

        moveB = None
        for m in get_all_moves(state, RED_player, game):
            val= minimax(m, depth-1, True, game)[0]
            #select the minmum between the two 
            minScore = min(minScore, val)
            if minScore == val:
                moveB = m
        
        return minScore, moveB

def alpha_beta(state, depth, alpha, beta, maxi, game):
    if depth == 0 or state.winner() is not None:
        return state.evaluate(), state

    if maxi:
        maxScore = float('-inf')
        moveB = None
        for m in get_all_moves(state, WHITE_player, game):
            val = minimax(m, depth - 1, alpha, beta, False, game)[0]
            maxScore = max(maxScore, val)
            # here we did the same thing but we modify the code 
            if maxScore == val:
                moveB = m
            #if the alpha is greater than beta we break means that we are out from the recursive function 
            alpha = max(alpha, maxScore)
            if alpha >= beta:
                break

        return maxScore, moveB
    else:
        minScore = float('inf')
        moveB = None
        for m in get_all_moves(state, RED_player, game):
            val = minimax(m, depth - 1, alpha, beta, True, game)[0]
            minScore = min(minScore, val)
            if minScore == val:
                moveB = m
            # we do it with beta this time 
            beta = min(beta, minScore)
            if alpha >= beta:
                break

        return minScore, moveB


def get_all_moves(board, color, game):
    moves = []

    for piece in board.AlLpieces(color):
        #we get the all moves to choise between them 
        valid_moves = board.get_valid_moves(piece)
        for move, skip in valid_moves.items():
            #get a copy from the current board 
            boardCoppy = deepcopy(board)
            # copy from a piece to virtualy choice a move 
            cpy_piece = boardCoppy.get_piece(piece.row, piece.col)
            new_ = choice(cpy_piece, move, boardCoppy, game, skip)
            moves.append(new_)
    
    return moves
def choice(piece, move, board, game, skip):
    board.move(piece, move[0], move[1])
    # If we can skip a piece we remove it from the board 
    if skip:
        board.remove(skip)

    return board



