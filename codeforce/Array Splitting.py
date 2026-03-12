n, k = map(int, input().split())
arr = list(map(int, input().split()))

space = []
for i in range(1, n):
    space.append(arr[i] - arr[i-1])

space.sort(reverse=True)
cost = arr[-1] - arr[0]

for i in range(k-1):
    cost -= space[i]


print(cost)