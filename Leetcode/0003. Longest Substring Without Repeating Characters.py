def lengthOfLongestSubstring(self, s: str) -> int:
        sub = set()
        left = 0
        max_length = 0

        for i in range(len(s)):
            while s[i] in sub:
                sub.remove (s[left])
                left +=1

            sub.add (s[i])
            max_length = max(max_length, i -left +1)

        return max_length
        