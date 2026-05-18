class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        maxline = deque()
        minline = deque()
        left = 0
        ans = 0
        
        for right in range(len(nums)):
            num = nums[right]

            while maxline and maxline[-1]<num:
                maxline.pop()
            maxline.append(num)

            while minline and minline[-1]>num:
                minline.pop()
            minline.append(num)

            while maxline[0] - minline[0] > limit:
                if maxline[0] == nums[left]:
                    maxline.popleft()

                if minline[0] == nums[left]:
                    minline.popleft()
                left +=1
            ans = max(ans, right - left + 1)
    
        return ans

        