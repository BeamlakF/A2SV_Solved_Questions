t = int(input())

for _ in range(t):
    n = int(input())
    s = input()

    if "aa" in s:
        print(2)
    elif "aba" in s or "aca" in s:
        print(3)
    elif "abca" in s:
        print(4)
    else:
        print(-1)