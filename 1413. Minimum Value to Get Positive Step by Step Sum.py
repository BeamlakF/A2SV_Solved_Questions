def minStartValue(self, nums):
        prefix_sum = 0
        min_prefix = 0
        for n in nums:
            prefix_sum += n
            min_prefix = min(min_prefix, prefix_sum)
        return 1 - min_prefix