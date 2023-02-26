from board import Board

def validate(sudoku_problem):
	"""
	Checks whether or not a given sudoku problem is valid in accordance with
	sudoku rules.
	"""

	board = Board(sudoku_problem)

	while board.current_square_in_bounds() is True:
		board.current_square = board.state[board.row_num][board.column_num]

		# 0 values are skipped as they are filler values (essentially None).
		# They don't count as being a part of the problem.
		if board.current_square == 0:
			board.progress_to_next_square()
			continue
		elif board.validate_current_square() is False:
			return False
		else:
			board.progress_to_next_square()

	return True

if __name__ == "__main__":
	sudoku_problem = [
		[8, 0, 2, 1, 7, 0, 0, 0, 6],
		[0, 9, 0, 0, 0, 8, 0, 5, 3],
		[0, 4, 0, 3, 0, 0, 0, 1, 8],
		[0, 0, 0, 8, 0, 0, 6, 4, 0],
		[9, 8, 0, 0, 2, 7, 0, 0, 1],
		[0, 0, 3, 0, 9, 0, 0, 2, 7],
		[5, 0, 1, 9, 0, 0, 0, 7, 0],
		[0, 7, 0, 4, 5, 1, 9, 6, 0],
		[4, 2, 9, 0, 3, 0, 0, 0, 0],
	]

	print(validate(sudoku_problem))