def strStr(self, haystack: str, needle: str) -> int:
        n = len(needle)
        h = len(haystack)

        if n == 0:
            return 0

        for i in range(h - n + 1):
            for j in range(n):
                if haystack[i + j] != needle[j]:
                    break
            else:
                return i

        return -1