matrix = [list(map(int, input().split())) for _ in range(5)]

for i in range(5):
    for j in range(5):
        if matrix[i][j] == 1:
            row_1, col_1 = i, j
            break

moves = abs(row_1 - 2) + abs(col_1 - 2)
print(moves)

    