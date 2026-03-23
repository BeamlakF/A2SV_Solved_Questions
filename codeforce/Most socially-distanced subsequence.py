t = int(input())

for _ in range(t):
    n = int(input())
    p = list(map(int, input().split()))
    
    res = [p[0]]  
    
    for i in range(1, n - 1):
        prev = p[i - 1]
        curr = p[i]
        next = p[i + 1]
        
        
        if (curr > prev and curr > next) or (curr < prev and curr < next):
            res.append(curr)
    
    res.append(p[-1])  
    
    print(len(res))
    print(*res)