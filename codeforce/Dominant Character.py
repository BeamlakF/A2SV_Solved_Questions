t = int(input())

for _ in range(t):
    n = int(input())
    s = input()

    # I have to do it for length 2, 3, 4, 7

    if "aa" in s:
        print(2)
        continue
    elif "aba" in s or "aca" in s:
        print(3)
        continue
    elif "acba" in s or "abac" in s or "acab" in s or "abca" in s:
        print(4)
        continue
    elif "abbaca" in s or "accaba" in s:
        print(6)
        continue
    elif  "abbacca" in s or "accabba" in s:
        print (7)
        continue
    else:
        print(-1)
        continue