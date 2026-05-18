from typing import List

def flipAndInvertImage(self, mat: List[List[int]]) -> List[List[int]]:
        
        for row in mat:
            row.reverse()
            
            for i in range(len(row)):
                row[i] = 1 - row[i]

        return mat