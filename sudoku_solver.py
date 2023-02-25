class Board:
	"""
	A class that represents the sudoku problem as a board. Methods can be used
	to 'progress' or 'backtrack' the current position on the board. There is
	also a method that checks whether or not the current value in the current
	square is valid in accordance with sudoku rules.
	"""

	def __init__(self, sudoku_problem):
		"""
		Copies the sudoku problem onto the board. Initialises variables that are
		used to keep track of where on the board we are currently using as well
		as what our last move was.
		"""

		self.state = []
		self.sudoku_problem = sudoku_problem

		for row in sudoku_problem:
			row = row.copy()
			self.state.append(row)

		self.number_rows, self.number_columns = 9, 9
		self.row_num, self.column_num = 0, 0
		self.current_square = self.state[self.row_num][self.column_num]
		self.last_move = None

	def current_square_in_bounds(self):
		if self.row_num < 0 or self.row_num >= self.number_rows:
			return False
		elif self.column_num < 0 or self.column_num >= self.number_columns:
			return False
		else:
			return True

	def progress_to_next_square(self):
		if self.column_num < 8:
			self.column_num += 1
		elif self.column_num == 8:
			self.row_num += 1
			self.column_num = 0

		self.last_move = 'progress'

	def validate_current_square(self):
		"""
		Checks whether or not the current value in the current square is valid 
		in accordance with sudoku rules.
		"""

		if self._validate_row() is False:
			return False
		elif self._validate_column() is False:
			return False
		elif self._validate_nonet() is False:
			return False
		else:
			return True
	
	def _validate_row(self):
		current_row = self.state[self.row_num].copy()
		current_row.remove(self.current_square)
		
		if self.current_square in current_row:
			return False

	def _validate_column(self):
		current_column = []

		for i in range(9):
			# Skip the current square.
			if i == self.row_num:
				continue

			square = self.state[i][self.column_num]
			current_column.append(square)

		if self.current_square in current_column:
			return False

	def _validate_nonet(self):
		# A nonet is also known as a block.
		current_nonet = self._create_current_nonet()

		if self.current_square in current_nonet:
			return False

	def _create_current_nonet(self):
		current_nonet = []

		# Find the row and column numbers for the first square in the nonet.
		x = int(self.column_num / 3)
		x *= 3
		y = int(self.row_num / 3)
		y *= 3

		# Iterates across the nonet and adds each square to the current nonet
		# list. 
		for i in range(3):
			for j in range(3):
				square = self.state[y][x]
				current_nonet.append(square)

				x += 1

			x -= 3
			y += 1

		current_nonet.remove(self.current_square)
		return current_nonet

	def backtrack_to_previous_square(self):
		# if the correct answer for the current square has no been given by the
		# sudoku problem, sets the current square to 0.
		if self.sudoku_problem[self.row_num][self.column_num] == 0:
			self.state[self.row_num][self.column_num] = 0

		if self.column_num > 0:
			self.column_num -= 1
		elif self.column_num == 0:
			self.row_num -= 1
			self.column_num = 8

		self.last_move = 'backtrack'

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
