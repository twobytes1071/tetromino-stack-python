import copy
import piece

# represents the playing board as a bitmap of fallen pieces + an actively falling piece
class Board:

    # a list of all valid movement inputs
    valid_user_inputs = ("a", "d", "s", "q", "e", " ", "")

    def __init__(self):
        # the height of the board
        self.length_i = 16

        # the i-position of the maximum height of the stack before ending the game
        self.max_fill_line = 3

        # the width of the board
        self.length_j = 10

        # a bitmap representing the locations of previously-fallen pieces
        self.board = [[False for _ in range(self.length_j)] for _ in range(self.length_i)]

        # the piece being actively moved by the player
        self.active_piece = None

    # prints the entire game screen to the console
    def display(self, score, high_score):
        display_board = copy.deepcopy(self.board)
        if self.has_active_piece():
            display_board = self.active_piece.imprint(display_board)
        for i in range(len(display_board)):
            if i == self.max_fill_line:
                print("--", end="")
            else:
                print(" |", end="")
            for square in display_board[i]:
                if square == True:
                    print("##", end="")
                else:
                    print("  ", end="")
            if i == self.max_fill_line:
                print("-- Score:       " + str(score))
            elif i == self.max_fill_line + 1:
                print("|  High Score:  " + str(high_score))
            else:
                print("| ")
        for _ in range(self.length_j + 2):
            print("--", end="")
        print()

    # creates a new active piece at the top of the board
    def summon_new_piece(self):
        self.active_piece = piece.Piece()
        self.active_piece.new_piece_setup(self.length_j)

    # applies the user's input to move the active piece
    def move_piece(self, user_input):
        move_projection_piece = copy.deepcopy(self.active_piece)
        match user_input:
            case "a":
                move_projection_piece.move_left()
                if move_projection_piece.valid_position(self.board):
                    self.active_piece.move_left()
            case "d":
                move_projection_piece.move_right()
                if move_projection_piece.valid_position(self.board):
                    self.active_piece.move_right()
            case "s":
                move_projection_piece.move_down()
                while move_projection_piece.valid_position(self.board):
                    self.active_piece.move_down()
                    move_projection_piece.move_down()
            case "q":
                move_projection_piece.rotate_counterclockwise()
                if move_projection_piece.valid_position(self.board):
                    self.active_piece.rotate_counterclockwise()
            case "e":
                move_projection_piece.rotate_clockwise()
                if move_projection_piece.valid_position(self.board):
                    self.active_piece.rotate_clockwise()
        move_projection_piece = copy.deepcopy(self.active_piece)
        move_projection_piece.move_down()
        if move_projection_piece.valid_position(self.board):
            self.active_piece.move_down()
        else:
            self.board = self.active_piece.imprint(self.board)
            self.active_piece = None

    # clears all complete rows from the board, shifting higher rows downward
    # returns the score corresponding to the amount of rows cleared
    def clear_full_rows(self):
        rows_cleared = 0
        for i in range(self.max_fill_line + 1, len(self.board)):
            full_row = True
            for j in range(len(self.board[i])):
                if self.board[i][j] == False:
                    full_row = False
                    break
            if full_row:
                for i2 in range(i, 0, -1):
                    for j2 in range(len(self.board[i])):
                        self.board[i2][j2] = self.board[i2 - 1][j2]
                rows_cleared += 1
        return rows_cleared ** 2 * 10

    # returns true if an active piece is in play
    def has_active_piece(self):
        return self.active_piece != None

    # returns true when a fallen piece has reached the max fill line
    def game_over(self):
        for square in self.board[self.max_fill_line]:
            if square == True:
                return True
        return False
