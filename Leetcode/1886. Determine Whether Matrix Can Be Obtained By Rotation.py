from typing import List

def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        n = len(mat)

        for _ in range(4): # to check 90, 270, 180 and 0
            if mat == target:
                return True
            for i in range(n):
                for j in range(i, n):
                    mat[i][j], mat[j][i] = mat[j][i], mat[i][j]

            for row in mat:
                row.reverse()

        return False