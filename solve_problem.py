from board import Board

def solve(sudoku_problem):
	"""Solves the sudoku problem by using the backtracking algorithm."""
	
	board = Board(sudoku_problem)
	iteration = 0

	while board.current_square_in_bounds() is True:
		print(f"Iteration: {iteration}")
		print(f"Current iteration: {board.state}")

		iteration += 1
		problem_square = sudoku_problem[board.row_num][board.column_num]

		# Without this bit of code, the program will infinitely loop between
		# backtracking from an incorrect square to skipping a square that was
		# included in the sudoku problem.
		if board.last_move == 'backtrack' and problem_square != 0:
			board.backtrack_to_previous_square()
			continue

		# None zero values given in the sudoku problem are automatically correct
		# and should not be altered
		if problem_square != 0:
			board.progress_to_next_square()
			continue

		board.state[board.row_num][board.column_num] += 1
		board.current_square = board.state[board.row_num][board.column_num]
		
		if board.current_square > 9:
			board.backtrack_to_previous_square()
			continue
		elif board.validate_current_square() is True:
			board.progress_to_next_square()
			continue

	print(f"Iterations required to solve: {iteration}")
	print(f"Solution: {board.state}")

	return board.state

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

	solve(sudoku_problem)
