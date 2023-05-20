import pygame
from .constants import BLACK, ROWS, RED, Border, COLS, WHITE
from .piece import Piece


class Board:
    def __init__(self):
        self.board = []
        self.num_red_left = self.num_white_left = 12
        self.num_red_kings = self.num_white_kings = 0
        self.create_board_with_pieces()

    def draw_board_squares(self, window):
        window.fill(BLACK)
        for row in range(ROWS):
            for col in range(row % 2, COLS, 2):
                pygame.draw.rect(window, RED, (row * Border, col * Border, Border, Border))

    def evaluate_game(self):
        return self.num_white_left - self.num_red_left + (self.num_white_kings * 0.5 - self.num_red_kings * 0.5)

    # get all pieces left and update it every time
    def get_all_pieces_left(self, color):
        pieces_left = []
        for row in self.board:
            for piece in row:
                if piece != 0 and piece.color == color:
                    pieces_left.append(piece)
        return pieces_left

    def move(self, piece, row, col):
        self.board[piece.row][piece.col], self.board[row][col] = self.board[row][col], self.board[piece.row][piece.col]
        piece.move(row, col)

        if row == ROWS - 1 or row == 0:
            piece.put_crown_on_board()
            if piece.color == WHITE:
                self.num_white_kings += 1
            else:
                self.num_red_kings += 1

    # hr\er we get the piece
    def get_piece(self, row, col):
        return self.board[row][col]

    def create_board_with_pieces(self):
        for row_board in range(ROWS):
            self.board.append([])
            for col_board in range(COLS):
                if col_board % 2 == ((row_board + 1) % 2):
                    if row_board < 3:
                        self.board[row_board].append(Piece(row_board, col_board, WHITE))
                    elif row_board > 4:
                        self.board[row_board].append(Piece(row_board, col_board, RED))
                    else:
                        self.board[row_board].append(0)
                else:
                    self.board[row_board].append(0)

    def draw_pieces_on_board(self, window):
        self.draw_board_squares(window)
        for r in range(ROWS):
            for c in range(COLS):
                piece_of_board = self.board[r][c]
                if piece_of_board != 0:
                    piece_of_board.draw(window)

    def remove_piece(self, pieces):
        for p in pieces:
            self.board[p.row][p.col] = 0
            if p != 0:
                if p.color == RED:
                    self.num_red_left -= 1
                else:
                    self.num_white_left -= 1

    def get_winner(self):
        if self.num_red_left <= 0:
            return WHITE
        elif self.num_white_left <= 0:
            return RED

        return None

    def get_piece_valid_moves(self, piece):
        valid_moves = {}
        left_place = piece.col - 1
        right_place = piece.col + 1
        piece_row = piece.row

        if piece.color == RED or piece.king:
            valid_moves.update(self._traverse_left(piece_row - 1, max(piece_row - 3, -1), -1, piece.color, left_place))
            valid_moves.update(self._traverse_right(piece_row - 1, max(piece_row - 3, -1), -1, piece.color, right_place))
        if piece.color == WHITE or piece.king:
            valid_moves.update(self._traverse_left(piece_row + 1, min(piece_row + 3, ROWS), 1, piece.color, left_place))
            valid_moves.update(self._traverse_right(piece_row + 1, min(piece_row + 3, ROWS), 1, piece.color, right_place))

        return valid_moves

    def _traverse_left(self, start, stop, step, color, left, skipped=[]):
        moves_valid = {}
        last = []
        for r in range(start, stop, step):
            if left < 0:
                break

            current = self.board[r][left]
            if current == 0:
                if skipped and not last:
                    break
                elif skipped:
                    moves_valid[(r, left)] = last + skipped
                else:
                    moves_valid[(r, left)] = last

                if last:
                    if step == -1:
                        row = max(r - 3, 0)
                    else:
                        row = min(r + 3, ROWS)
                    moves_valid.update(self._traverse_left(r + step, row, step, color, left - 1, skipped=last))
                    moves_valid.update(self._traverse_right(r + step, row, step, color, left + 1, skipped=last))
                break
            elif current.color == color:
                break
            else:
                last = [current]

            left -= 1

        return moves_valid

    def _traverse_right(self, start, stop, step, color, right, skipped=[]):
        moves_valid = {}
        last = []
        for r in range(start, stop, step):
            if right >= COLS:
                break

            current = self.board[r][right]
            if current == 0:
                if skipped and not last:
                    break
                elif skipped:
                    moves_valid[(r, right)] = last + skipped
                else:
                    moves_valid[(r, right)] = last

                if last:
                    if step == -1:
                        row = max(r - 3, 0)
                    else:
                        row = min(r + 3, ROWS)
                    moves_valid.update(self._traverse_left(r + step, row, step, color, right - 1, skipped=last))
                    moves_valid.update(self._traverse_right(r + step, row, step, color, right + 1, skipped=last))
                break
            elif current.color == color:
                break
            else:
                last = [current]

            right += 1

        return moves_valid
