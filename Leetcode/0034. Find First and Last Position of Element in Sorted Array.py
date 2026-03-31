def searchRange(self, nums, target):
        n = len(nums)
        def firstOccur():
            ans = -1
            left = 0
            right = n -1
            while left <= right:
                mid = (left+ right)//2

                if target == nums[mid]:
                    ans = mid
                    right = mid -1
                elif nums[mid] > target:
                    right = mid -1

                elif nums[mid] <target:
                    left = mid +1

            return ans

        def LastOccur():
            ans = -1
            left = 0
            right = n -1
            while left <= right:
                mid = (left+ right)//2

                if target == nums[mid]:
                    ans = mid
                    left = mid +1

                elif nums[mid] < target:
                    left = mid +1

                elif nums[mid] >target:
                    right = mid -1
            return ans

        return [firstOccur(), LastOccur()]


