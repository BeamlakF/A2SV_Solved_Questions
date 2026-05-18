def __init__(self, nums):
        self.nums = nums        

def sumRange(self, left: int, right: int) -> int:
    prefix_sum = 0
    for i in range(left, right +1):
        prefix_sum += self.nums[i]
    return prefix_sum
