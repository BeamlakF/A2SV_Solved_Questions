def findMaxAverage(self, nums, k: int) -> float:
        curr_sum = 0
        max_sum = float('-inf')
        
        left = 0
        for right in range(len(nums)):
            curr_sum += nums[right]
            if right-left +1 == k:
                max_sum = max(curr_sum, max_sum)
                curr_sum -= nums[left]
                left +=1
        
        return max_sum/k