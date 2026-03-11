def missingNumber(self, nums):
    n = len(nums)
    output = 0
    for i in range(n + 1):
        output ^= i
    for num in nums:
        output ^= num
    return output
