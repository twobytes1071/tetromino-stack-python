import random
import copy
import math

# represents a single game piece as a square bitmap

class Piece:
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
		self.configuration = []
		self.i_position = 0
		self.j_position = 0
	
	def new_piece_setup(self, board_length_j):
		self.configuration = copy.deepcopy(Piece.valid_piece_configurations[random.randint(0, len(Piece.valid_piece_configurations) - 1)])
		for _ in range(random.randint(0, 3)):
			self.rotate_clockwise()
		self.i_position = 0
		self.j_position = math.floor(board_length_j / 2) - math.ceil(self.size() / 2)

	def size(self):
		return len(self.configuration) - 1

	def move_left(self):
		self.j_position -= 1
	
	def move_right(self):
		self.j_position += 1

	def move_down(self):
		self.i_position += 1

	def rotate_clockwise(self):
		previous_configuration = copy.deepcopy(self.configuration)
		for i in range(len(self.configuration)):
			for j in range(len(self.configuration[i])):
				self.configuration[j][self.size() - i] = previous_configuration[i][j]

	def rotate_counterclockwise(self):
		previous_configuration = copy.deepcopy(self.configuration)
		for i in range(len(self.configuration)):
			for j in range(len(self.configuration[i])):
				self.configuration[self.size() - j][i] = previous_configuration[i][j]

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
	
	def imprint(self, board):
		updated_board = copy.deepcopy(board)
		for i in range(len(self.configuration)):
			for j in range(len(self.configuration[i])):
				if self.configuration[i][j] == True:
					updated_board[self.i_position + i][self.j_position + j] = True
		return updated_board