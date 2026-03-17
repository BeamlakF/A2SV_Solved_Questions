def runningSum(self, nums):
        prefix_sum = 0
        running= []
        for i in range(len(nums)):
            prefix_sum += nums[i]
            running.append(prefix_sum)


        return running