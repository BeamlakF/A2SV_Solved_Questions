n, m = map(int, input().split())

moves = 0

if m % n != 0:
    print(-1)
else:
    q = m // n

    while q % 2 == 0:
        moves += 1
        q //= 2

    while q % 3 == 0:
        moves += 1
        q //= 3

    if q != 1:
        print(-1)
    else:
        print(moves)
