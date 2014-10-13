import unittest
from matrix_bombing import bomb, matrix_bombing_plan


class TestMatrixBombing(unittest.TestCase):
    def testBombAt00(self):
        m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        result = [[1, 1, 3], [3, 4, 6], [7, 8, 9]]

        self.assertEqual(result, bomb(m, (0, 0)))

    def testBombZeroes(self):
        m = [[0, 0, 0], [0, 100, 0], [0, 0, 0]]
        result = [[0, 0, 0], [0, 100, 0], [0, 0, 0]]

        self.assertEqual(result, bomb(m, (1, 1)))

    def testMatrixBombingPlanExample(self):
        m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        result = {
            (0, 0): 42, (0, 1): 36, (0, 2): 37,
            (1, 0): 30, (1, 1): 15, (1, 2): 23,
            (2, 0): 29, (2, 1): 15, (2, 2): 26
        }

        self.assertEqual(result, matrix_bombing_plan(m))

if __name__ == '__main__':
    unittest.main()
