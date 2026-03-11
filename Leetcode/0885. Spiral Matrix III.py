def spiralMatrixIII(self, rows, cols, rStart, cStart):

        result = []
        result.append([rStart, cStart])
        step_size = 1

        row = rStart
        col = cStart
        while len(result) < rows * cols:
            for _ in range(step_size):
                col += 1
                if 0 <= row < rows and 0 <= col < cols:
                    result.append([row, col])
                    
            for _ in range(step_size):
                row += 1
                if 0 <= row < rows and 0 <= col < cols:
                    result.append([row, col])
            step_size += 1

            for _ in range(step_size):
                col -= 1
                if 0 <= row < rows and 0 <= col < cols:
                    result.append([row, col])

            for _ in range(step_size):
                row -= 1
                if 0 <= row < rows and 0 <= col < cols:
                    result.append([row, col])

            step_size += 1

        return result