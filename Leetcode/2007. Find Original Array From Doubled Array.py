from collections import Counter

def findOriginalArray(self, changed):
        if len(changed) % 2 != 0:
            return []
        
        changed.sort()
        count = Counter(changed)
        original = []
        
        for x in changed:
            if count[x] == 0:
                continue
            
            if count[2 * x] == 0:
                return []
            
            original.append(x)
            count[x] -= 1
            count[2 * x] -= 1