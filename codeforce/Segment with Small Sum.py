n, s = map(int, input().split())
arr = list(map(int, input().split()))

left = 0
win_sum = 0
max_len = 0

for right in range(n):
    win_sum += arr[right]
    
    while win_sum > s:
        win_sum -= arr[left]
        left += 1
    
    max_len = max(max_len, right - left + 1)

print(max_len)