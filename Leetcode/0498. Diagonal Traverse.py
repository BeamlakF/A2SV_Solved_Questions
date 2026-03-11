from typing import List


def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:

        total_rows = len(matrix)
        total_cols = len(matrix[0])
        result = []

        for diagonal in range(total_rows + total_cols - 1):

            current_diagonal = []

            for row in range(total_rows):
                column = diagonal - row

                if 0 <= column < total_cols:
                    current_diagonal.append(matrix[row][column])

            if diagonal % 2 == 0:
                current_diagonal.reverse()

            result.extend(current_diagonal)

        return result