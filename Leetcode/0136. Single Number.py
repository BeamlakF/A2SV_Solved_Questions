def singleNumber(self, nums) -> int:
        result = 0
        for num in nums:
            result ^= num  # XOR
        return result