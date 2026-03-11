from typing import List

 def imageSmoother(self, mat: List[List[int]]) -> List[List[int]]:
        row = len(mat)
        col = len(mat[0])
        res = [[0]*col for _ in range(row)]

        for i in range(row):
            for j in range(col):
                total = 0
                count = 0

                for x in range(i-1, i+2):
# we are checking the surrounding 8 matrice values, so... as range doesn't see the end, I will do i+2, j+2...
                    for y in range(j-1, j+2):
                        if 0 <= x < row and 0 <= y < col: # this check the validity-does the say the i+1 fall out of row when I am checking,
                            total += mat[x][y]
                            count += 1

                res[i][j] = total // count

        return res