
import pygame
from checkers.constants import WIDTH, HEIGHT, Border, RED, WHITE
from checkers.game import Game
from Algo.agent import minimax

import random

FPS = 60


WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Game(checkers)')

def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // Border
    col = x // Border
    return row, col
def make_red_move(game):
    # Get all valid moves for the red player
    red_moves = game.board.get_valid_moves(game.selected)
    if len(red_moves)>0:
        # Select a random move
        move = random.choice(list(red_moves.keys()))
        # Perform the selected move
        game._move(move[0], move[1])
        return True
    else:
        return False
#the main 
def main():
    run = True
    clock = pygame.time.Clock()
    game = Game(WIN)

    while run:
        clock.tick(FPS)
        
        if game.turn == WHITE:
            value, new_board = minimax(game.get_board(), 3, WHITE, game)
            game.move_agent(new_board)
        
            

        

        if game.winner() != None:
            print(game.winner())
            run = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)
                game.select(row, col)
                make_red_move(game)


        game.update()
    
    pygame.quit()

main()