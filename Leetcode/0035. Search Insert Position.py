def searchInsert(self, nums, target: int) -> int:
        n = len(nums)
        l = 0
        r = n-1
        if nums[0]>= target:
            return 0

        elif nums[r] < target:
            return r +1

        while l <=r:
            mid = (l+r)//2
            if target == nums[mid]:
                return mid

            elif nums[mid]< target and nums[mid +1]>target:
                return mid +1

            elif nums[mid]<target:
                l = mid +1
            

            else:
                r = mid -1
                


        