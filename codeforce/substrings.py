# s = input().strip()
# n = len(s)

# answer = 0

# for L in range(n - 1, 0, -1):   # substring length
#     seen = set()
#     found = False
    
#     for i in range(n - L + 1):
#         sub = s[i:i+L]
#         if sub in seen:
#             answer = L
#             found = True
#             break
#         seen.add(sub)
    
#     if found:
#         break

# print(answer)

