from typing import List


def rotate(self, matrix: List[List[int]]) -> None:
        for i in range(len(matrix)):
            for j in range(i,len(matrix[0])):
                matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]
                #transposing the matrix first, and then flip it
        for i in matrix:
            i.reverse()