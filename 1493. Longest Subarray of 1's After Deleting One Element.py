def longestSubarray(self, nums) -> int:
        max_len = 0
        left = 0
        count = 0
        for i in range (len(nums) -1):
            if nums[i] == 0:
                count +=1

            while count>1:
                if nums[left] == 0:
                    count -=1
                left +=1
            max_len = max(max_len, i - left)
                

        return max_len


        