import numpy as np

def create_board():
	board = np.zeros((6,7))
	return board

def drop_piece():
	pass

def is_valid_location():
	pass

def get_next_open_row():
    pass
    
board = create_board()
game_over = False

while not gave_over:
	# Asks for P1's input
	if turn == 0:
		selection = input("Player 1 your turn (0-6:"))


	# Asks for P2's input
else:
	 selection = int(input("Player 2 your turn (0-6):"))

turn += 1
turn = turn % 2