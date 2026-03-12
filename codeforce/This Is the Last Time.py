t = int(input())

for _ in range(t):
    n, k = map(int, input().split())

    casinos = []
    for _ in range(n):
        l, r, real = map(int, input().split())
        casinos.append((l, r, real))

    casinos.sort(key=lambda x: x[0])

    sign = True
    while sign:
        sign = False
        for l, r, real in casinos:
            if l <= k and k <= r and k < real:
                k = real
                sign = True
                
    print(k)