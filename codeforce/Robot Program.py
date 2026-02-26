t = int(input())

for _ in range(t):
    n, x, k = map(int, input().split())
    s = input()

    position = x
    first_find = -1
    # time can never start from -1, so it's just there to mark it...
    # if we use 0...when we add 1 later, it will deonstrate forst_find at time 1 but 
    # we want it to be at time 0

    for i in range(n):
        if s[i] == 'L':
            position -= 1
        else:
            position += 1

        if position == 0:
            first_find = i + 1
            break

    # If never hits zero OR hits after k, meaning never find 0...because we have limited k times
    if first_find == -1 or first_find > k:
        print(0)
        continue

    # if we find the first 0
    remaining_cycle = k - first_find

    # Now find cycle from 0
    position = 0
    cycle = -1

    for i in range(n):
        if s[i] == 'L':
            position -= 1
        else:
            position += 1

        if position == 0:
            cycle = i + 1
            break

    # If no cycle, if it never returns to 0, after he first run
    if cycle == -1:
        print(1)
        continue
    extra_time = remaining_cycle // cycle
    print(1 + extra_time)