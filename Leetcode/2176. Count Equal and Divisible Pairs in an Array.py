def countPairs(self, nums, k: int) -> int:
        n = len(nums)
        count = 0
        for i in range(0, n):
            for j in range(i + 1, n):
                if nums[i] == nums[j] and (i * j) % k == 0:
                    count = count + 1
        return count