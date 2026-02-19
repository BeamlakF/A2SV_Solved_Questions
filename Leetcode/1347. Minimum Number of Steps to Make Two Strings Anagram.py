from collections import Counter

def minSteps(self, s: str, t: str) -> int:
        count_s = Counter(s)
        count_t = Counter(t)
        output = 0
        
        for char in count_s:
            if count_s[char] > count_t.get(char, 0):
                output += count_s[char] - count_t.get(char, 0)
        
        return output
