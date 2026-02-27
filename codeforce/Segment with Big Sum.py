n, s = map(int, input().split())
arr = list(map(int, input().split()))

left = 0
win_sum = 0
min_len = float('inf')

for right in range(n):
    win_sum += arr[right]
    
    while win_sum >= s:
        min_len = min(min_len, right - left + 1)
        win_sum -= arr[left]
        left += 1

if min_len == float('inf'):
    print(-1)
else:
    print(min_len)