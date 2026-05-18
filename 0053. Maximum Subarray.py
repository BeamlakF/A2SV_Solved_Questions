def maxSubArray(self, nums) -> int:
        maxSum = float('-inf')
        current = 0
        
        for num in nums:
            current += num
            
          
            if current > maxSum:
                maxSum = current
            
            if current < 0:
                current = 0
        
        return maxSum
        