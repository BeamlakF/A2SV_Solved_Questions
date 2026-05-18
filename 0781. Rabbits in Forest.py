import math

def numRabbits(self, answers):
        count = {}
        for a in answers:
            count[a] = count.get(a, 0) + 1
        
        total = 0
        for x, freq in count.items():
            group_size = x + 1
            groups = math.ceil(freq / group_size)
            total += groups * group_size
        
        return total