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
		"""
		Checks whether the current square is within the 9x9 grid. This function 
		is used to break while loops that iterate across the grid. Once the
		progress_to_next_square() or backtrack_to_previous_square() functions
		cause the the column_num and row num values to be outside of bounds
		(0-8), this function returns False and the various while loops in 
		other functions break.
		"""
		
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
		

if __name__ == "__main__":
	pass