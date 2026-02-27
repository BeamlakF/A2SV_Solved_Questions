n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

left = 0      # pointer for a
right = 0     # pointer for b
ans = 0

while left < n and right < m:
    if a[left] < b[right]:
        left += 1
    elif a[left] > b[right]:
        right += 1
    else:
        value = a[left]
        countA = 0
        countB = 0
        
        while left < n and a[left] == value:
            countA += 1
            left += 1
        
        while right < m and b[right] == value:
            countB += 1
            right += 1
        
        ans += countA * countB

print(ans)