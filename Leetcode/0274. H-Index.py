def hIndex(self, citations) -> int:
        citasort = sorted(citations)
        n = len(citations)

        for i in range(n):
            if citasort[i] >= n - i:
                return n-i

        return 0

        