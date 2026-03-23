def maxSumRangeQuery(self, nums, requests) -> int:
        n = len(nums)
        freq = [0] * (n + 1)
        res = 0

        

        for l, r in requests:
            freq[l] += 1
            if r + 1 < len(freq):
                freq[r + 1] -= 1

        Formula = 10**9 + 7

        for i in range(1, n):
            freq[i] += freq[i - 1]

        freq = freq[:n]  

        nums.sort()
        freq.sort()
        

        for i in range(n):
            res += nums[i] * freq[i]
            res %= Formula

        return res

        