from random import randint
from board import Board

def create_random_sudoku_problem():
	"""
	Creates a randomised sudoku problems by filling a 9x9 2d list with random
	integers between 1-9. Then iterates across the 2d list and sets any values
	that are not a part of a valid problem to 0. This leaves us with a valid
	sudoku problem in a format suitable for our other functions. 
	"""
	
	# Create a 9x9 2d list filled with 0s as a starting point.
	sudoku_problem = [[0 for row in range(9)] for column in range(9)]

	board = Board(sudoku_problem)

	while board.current_square_in_bounds() is True:
		board.state[board.row_num][board.column_num] = randint(1, 9)
		board.progress_to_next_square()

	# Reset for the next while loop.
	board.row_num, board.column_num = 0, 0

	# Removes invalid values and leaves a valid sudoku_problem. 
	while board.current_square_in_bounds() is True:
		board.current_square = board.state[board.row_num][board.column_num]

		if board.validate_current_square() is False:
			board.state[board.row_num][board.column_num] = 0
		
		board.progress_to_next_square()

	sudoku_problem = board.state
	return sudoku_problem

if __name__ == "__main__":
	sudoku_problem = create_random_sudoku_problem()

	print(sudoku_problem)