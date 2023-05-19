import pygame
from checkers.constants import WIDTH, HEIGHT, Border, RED, WHITE
from checkers.game import Game
from Algo.agent import minimax
from Algo.agent import alpha_beta


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
def level_menu():
    # Create a Pygame font object
    font = pygame.font.Font(None, 36)

    # Create Pygame text objects for the level options
    easy_text = font.render("1 Easy", True, (255, 255, 255))
    medium_text = font.render("2 Medium", True, (255, 255, 255))
    hard_text = font.render("3 Hard", True, (255, 255, 255))

    # Get the dimensions of the text objects
    easy_width, easy_height = easy_text.get_size()
    medium_width, medium_height = medium_text.get_size()
    hard_width, hard_height = hard_text.get_size()

    # Calculate the position to draw the text objects
    easy_x = (WIDTH - easy_width) // 2
    easy_y = (HEIGHT - easy_height) // 2 - 50
    medium_x = (WIDTH - medium_width) // 2
    medium_y = (HEIGHT - medium_height) // 2
    hard_x = (WIDTH - hard_width) // 2
    hard_y = (HEIGHT - hard_height) // 2 + 50

    # Draw the text objects onto the Pygame window
    WIN.blit(easy_text, (easy_x, easy_y))
    WIN.blit(medium_text, (medium_x, medium_y))
    WIN.blit(hard_text, (hard_x, hard_y))

    # Update the Pygame display
    pygame.display.update()

    # Wait for the user to click on a level option
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if easy_x <= pos[0] <= easy_x + easy_width and easy_y <= pos[1] <= easy_y + easy_height:
                    return 1

                elif medium_x <= pos[0] <= medium_x + medium_width and medium_y <= pos[1] <= medium_y + medium_height:
                    return 2
                elif hard_x <= pos[0] <= hard_x + hard_width and hard_y <= pos[1] <= hard_y + hard_height:
                    return 3
#the main





def algoritm_menu():
    # Create a Pygame font object
    font = pygame.font.Font(None, 36)

    # Create Pygame text objects for the level options
    mini_text = font.render("1- Minimax ", True, (255, 255, 255))
    alpha_text = font.render("2- Alpha bita", True, (255, 255, 255))


    # Get the dimensions of the text objects
    mini_width, mini_height = mini_text.get_size()
    alpha_width, alpha_height = alpha_text.get_size()


    # Calculate the position to draw the text objects
    mini_x = (WIDTH - mini_width) // 4
    mini_y = (HEIGHT - mini_height ) // 4 - 50
    alpha_x = (WIDTH - alpha_width) // 4
    alpha_y = (HEIGHT - alpha_height) // 4


    # Draw the text objects onto the Pygame window
    WIN.blit(mini_text, (mini_x, mini_y))
    WIN.blit(alpha_text, (alpha_x, alpha_y))

    # Update the Pygame display
    pygame.display.update()

    # Wait for the user to click on a level option
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if mini_x <= pos[0] <= mini_x + mini_width and mini_y <= pos[1] <= mini_y + mini_height:
                    return 1

                elif alpha_x <= pos[0] <= alpha_x + alpha_width and alpha_y <= pos[1] <= alpha_y + alpha_height:
                    return 2

def main():
    run = True
    clock = pygame.time.Clock()
    algo = algoritm_menu()
    level = level_menu()
    game = Game(WIN)

    while run:
        clock.tick(FPS)

        if game.turn == WHITE:
            if level == 1 :
                if algo == 1:
                 value, new_board = minimax(game.get_board(), 3, WHITE, game)
                 game.move_agent(new_board)
            elif level==2:
                if algo == 1:
                 value, new_board = minimax(game.get_board(), 3, WHITE, game)
                 game.move_agent(new_board)
            elif level==3:
                if algo == 1:
                 value, new_board = minimax(game.get_board(), 3, WHITE, game)
                 game.move_agent(new_board)
            elif level == 1 :
                if algo == 2:
                 value, new_board = alpha_beta(game.get_board(), 1, WHITE, game)
                 game.move_agent(new_board)
            elif level==2:
                if algo == 2:
                  value, new_board = alpha_beta(game.get_board(), 2, WHITE, game)
                  game.move_agent(new_board)
            elif level==3:
                if algo == 2:
                  value, new_board = alpha_beta(game.get_board(), 3, WHITE, game)
                  game.move_agent(new_board)
        if game.winner() != None:
            draw_winner(game.winner())
            #run = False

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