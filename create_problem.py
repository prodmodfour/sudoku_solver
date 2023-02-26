from random import randint
from board import Board

def create_random_sudoku_problem():
	# Create a 9x9 2d list filled with 0s as a starting point.
	sudoku_problem = [[0 for row in range(9)] for column in range(9)]

	board = Board(sudoku_problem)


	return sudoku_problem

if __name__ == "__main__":
	sudoku_problem = create_random_sudoku_problem()

	print(sudoku_problem)