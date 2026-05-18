def smallerNumbersThanCurrent(self, nums):
        count =[]
        
        n = len(nums)
        for i in range(0, n):
            count_num = 0
            for j in range(0,n ):
                if nums[j]<nums[i]:
                    count_num +=1
            count.append(count_num)
        return count
                    

        
