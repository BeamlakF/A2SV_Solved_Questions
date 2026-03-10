from typing import List

def setZeroes(self, matrix: List[List[int]]) -> None:
        row = set()
        col = set()
#The two sets will remember which rows and columns should be zeroed.Using set() allows O(1) lookup

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]==0:
                    row.add(i)
                    col.add(j)
#Add i to row makes the entire i-th row to be zeroed out, and Adding  j to col - the entire j-th column  
             
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i in row or j in col:
                    matrix[i][j]=0