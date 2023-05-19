import pygame
from checkers.constants import WIDTH, HEIGHT, Border, RED, WHITE
from checkers.game import Game
from Algo.agent import minimax

import random
import sys
FPS = 60

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Game(checkers)')

pygame.font.init() # Initialize the Pygame font module


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
def draw_winner(winner):
    # Create a new Pygame window
    winner_win = pygame.display.set_mode((200, 100))
    pygame.display.set_caption('Winner')

    # Create a Pygame font object
    font = pygame.font.Font(None, 36)

    # Create a Pygame surface to hold the winner message
    if winner == RED:
        text_surface = font.render("Red wins!", True, (255, 0, 0))
    elif winner == WHITE:
        text_surface = font.render("White wins!", True, (255, 255, 255))
    else:
        text_surface = font.render("Tie game!", True, (255, 255, 255))

    # Get the dimensions of the text surface
    text_width, text_height = text_surface.get_size()

    # Calculate the position to draw the text surface
    x = (200 - text_width) // 2
    y = (100 - text_height) // 2

    # Draw the text surface onto the Pygame window
    winner_win.blit(text_surface, (x, y))

    # Update the Pygame display
    pygame.display.update()

    # Wait for a user event to close the window
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

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
            draw_winner(game.winner())
            run = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)
                game.select(row, col)
                if make_red_move(game) == False:
                    draw_winner(game.winner())
                    break
                    #run =False




        game.update()


    pygame.quit()

main()