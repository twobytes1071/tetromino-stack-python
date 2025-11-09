import game_board

def main():
	welcome()
	high_score = 0
	continue_playing = True
	while continue_playing:
		board = game_board.Board()
		score = 0
		while not board.game_over():
			if not board.has_active_piece():
				board.summon_new_piece()
			clear_screen()
			board.display(score, high_score)
			user_move = game_input("Make your move: ", game_board.Board.valid_user_inputs)
			board.move_piece(user_move)
			if not board.has_active_piece():
				score += board.clear_full_rows()
				if score > high_score:
					high_score = score
		clear_screen()
		board.display(score, high_score)
		print("Game over! Score: " + str(score))
		user_choice = user_input("Press [ENTER] to play again. Type 'quit' to exit. ", ("", "quit"))
		if user_choice == "quit":
			continue_playing = False
		
def welcome():
    input("Welcome to Tetronimo Stack!\n\nBlocky pieces will fall from the top, and the goal is to stack them as neatly as possible. Every complete row will disappear to make room for more blocks. \
The game ends when the blocks stack too high; keep them below the line!\n\n\
Scoring:\nSingle row clear:     10 points\nDouble row clear:     40 points\nTriple row clear:     90 points\nQuadruple row clear:  160 points\n\n\
Controls:\n[A]:      Move left\n[D]:      Move right\n[Q]:      Rotate counterclockwise\n[E]:      Rotate clockwise\n[S]:      Drop to bottom\n[ENTER]:  Drop one space\n\n\
Press [ENTER] to start. ")

def clear_screen():
	for _ in range(30):
		print()

def user_input(message, valid_user_inputs):
	user_input = input(message)
	while user_input not in valid_user_inputs:
		user_input = input(message)
	return user_input

def game_input(message, valid_user_inputs):
	user_input = input(message)
	if len(user_input) >= 1:
		user_input = user_input[-1]
	while user_input not in valid_user_inputs:
		user_input = input(message)
		if len(user_input) >= 1:
			user_input = user_input[-1]
	return user_input

if __name__ == "__main__":
    main()
