from collections import deque

def longestSubarray(self, nums, limit):
        max_d = deque()
        min_d = deque()
        
        left = 0
        res = 0
        
        for right in range(len(nums)):
            # Maintain max deque
            while max_d and nums[right] > max_d[-1]:
                max_d.pop()
            max_d.append(nums[right])
            
            # Maintain min deque
            while min_d and nums[right] < min_d[-1]:
                min_d.pop()
            min_d.append(nums[right])
            
            # Shrink window if invalid
            while max_d[0] - min_d[0] > limit:
                if nums[left] == max_d[0]:
                    max_d.popleft()
                if nums[left] == min_d[0]:
                    min_d.popleft()
                left += 1
            
            res = max(res, right - left + 1)
        
        return res