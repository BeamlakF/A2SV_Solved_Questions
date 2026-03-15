from typing import List

def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        look_up = {0: -1}
        prefix_sum = 0

        for i in range(len(nums)):
            prefix_sum += nums[i]
            check = prefix_sum % k

            if check in look_up:
                if i - look_up[check] > 1:
                    return True
            else:
                look_up[check] = i

        return False