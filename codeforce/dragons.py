mystrength , N = map(int, input().split())
arr = []
for _ in range(N):
  dragon, bonus = map(int, input().split())
  arr.append((dragon, bonus))

arr.sort()
flag = True
for dragon, bonus in arr:
  if dragon < mystrength:
    mystrength += bonus
  else:
    flag = False
    break
if flag: 
  print("YES")
else:
  print("NO")