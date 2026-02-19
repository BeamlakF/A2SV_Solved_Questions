from collections import Counter

def smallestPalindrome(self, s: str) -> str:
        s = sorted(s)
        count = Counter(s)
        left = []
        middle = ""

        for char in count:
            if count[char] % 2 == 1:
                middle = char
            left.append(char * (count[char] // 2))
        
        left_part = "".join(left)
        return left_part + middle + left_part[::-1]

        