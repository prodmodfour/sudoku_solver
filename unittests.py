import unittest
from board import Board
from solve_problem import solve
from validate_problem import validate
from create_problem import create_random_sudoku_problem

class TestSolver(unittest.TestCase):

	def test_validate(self):
		"""
		Tests whether the validate method can correctly return Tre in the event 
		that it is given a valid sudoku problem.
		"""
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

		self.assertTrue(validate(sudoku_problem))

	def test_solve(self):
		"""
		Tests whether the solve method can get the correct solution to a given
		sudoku problem.
		"""
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

		true_solution = [
			[8, 3, 2, 1, 7, 5, 4, 9, 6],
			[1, 9, 6, 2, 4, 8, 7, 5, 3],
			[7, 4, 5, 3, 6, 9, 2, 1, 8],
			[2, 5, 7, 8, 1, 3, 6, 4, 9],
			[9, 8, 4, 6, 2, 7, 5, 3, 1],
			[6, 1, 3, 5, 9, 4, 8, 2, 7],
			[5, 6, 1, 9, 8, 2, 3, 7, 4],
			[3, 7, 8, 4, 5, 1, 9, 6, 2],
			[4, 2, 9, 7, 3, 6, 1, 8, 5],
		]

		program_solution = solve(sudoku_problem)

		self.assertEqual(program_solution, true_solution)

	def test_create(self):
		"""
		Tests whether the create_random_sudoku_problem method can create a valid 
		sudoku problem in the correct format for our other functions. This test 
		is only valid if the validate function is working correctly. This is 
		unavoidable as create_random_sudoku_problem() returns a random value
		that cannot easily be tested, to my knowledge at this time.
		"""

		sudoku_problem = create_random_sudoku_problem()

		self.assertTrue(validate(sudoku_problem))


if __name__ == "__main__":
	unittest.main()

