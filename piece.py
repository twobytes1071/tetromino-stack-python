import random
import copy
import math

# represents a single game piece as a square bitmap
class Piece:

	# a list of all valid piece configurations, not accounting for rotational symmetry
	valid_piece_configurations = (
		[
			[False, False, False, False],
			[False, False, False, False],
			[True, True, True, True],
			[False, False, False, False]
		],
		[
			[True, True],
			[True, True]
		],
		[
			[False, True, False],
			[True, True, True],
			[False, False, False]
		],
		[
			[False, False, False],
			[False, True, True],
			[True, True, False]
		],
		[
			[False, False, False],
			[True, True, False],
			[False, True, True]
		],
		[
			[False, False, False],
			[False, False, True],
			[True, True, True]
		],
		[
			[False, False, False],
			[True, False, False],
			[True, True, True]
		]
	)

	def __init__(self):
		# a bitmap representing the shape of the piece
		self.configuration = []

		# the i-position of the piece on the board
		self.i_position = 0

		# the j-position of the piece on the board
		self.j_position = 0
	
	# randomizes the configuration and rotation of the piece and places it in the top-middle of the board
	def new_piece_setup(self, board_length_j):
		self.configuration = copy.deepcopy(Piece.valid_piece_configurations[random.randint(0, len(Piece.valid_piece_configurations) - 1)])
		for _ in range(random.randint(0, 3)):
			self.rotate_clockwise()
		self.i_position = 0
		self.j_position = math.floor(board_length_j / 2) - math.ceil(len(self.configuration) / 2)

	# moves the piece left
	def move_left(self):
		self.j_position -= 1
	
	# moves the piece right
	def move_right(self):
		self.j_position += 1

	# moves the piece down
	def move_down(self):
		self.i_position += 1

	# rotates the piece clockwise
	def rotate_clockwise(self):
		previous_configuration = copy.deepcopy(self.configuration)
		for i in range(len(self.configuration)):
			for j in range(len(self.configuration[i])):
				self.configuration[j][len(self.configuration) - 1 - i] = previous_configuration[i][j]

	# rotates the piece counterclockwise
	def rotate_counterclockwise(self):
		previous_configuration = copy.deepcopy(self.configuration)
		for i in range(len(self.configuration)):
			for j in range(len(self.configuration[i])):
				self.configuration[len(self.configuration) - 1 - j][i] = previous_configuration[i][j]

	# returns true if the piece in its current location does not overlap any fallen pieces on the board
	def valid_position(self, board):
		for i in range(len(self.configuration)):
			for j in range(len(self.configuration[i])):
				if self.configuration[i][j] == True:
					if self.i_position + i < 0 or self.i_position + i >= len(board):
						return False
					if self.j_position + j < 0 or self.j_position + j >= len(board[self.i_position + i]):
						return False
					if board[self.i_position + i][self.j_position + j] == True:
						return False
		return True
	
	# places the piece on the board as a fallen piece
	def imprint(self, board):
		updated_board = copy.deepcopy(board)
		for i in range(len(self.configuration)):
			for j in range(len(self.configuration[i])):
				if self.configuration[i][j] == True:
					updated_board[self.i_position + i][self.j_position + j] = True
		return updated_board
