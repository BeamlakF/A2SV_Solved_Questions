from collections import Counter

t = int(input())

for _ in range(t):
  s = input()
  t = input()

  count_s = Counter(s)
  count_t = Counter(t)

  if not(count_s <= count_t):
    print("Impossible")
    continue

  left = count_t - count_s
  
  start = []

  for e in left:
    while left[e] > 0:
      start.append(e)
      left[e] -= 1

  start.sort()

  res = []

  i = 0
  for e in s:
    while i < len(start) and start[i] < e:
      res.append(start[i])
      i += 1


    res.append(e)

  res.extend(start[i:])
  print(''.join(res))

    
