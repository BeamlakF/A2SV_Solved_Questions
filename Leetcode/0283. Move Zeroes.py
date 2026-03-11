def moveZeroes(self, nums) -> None:
    
        hold = 0
        lookup = 0

        while lookup < len(nums):
            if nums[lookup] != 0:
                nums[lookup], nums[hold] = nums[hold], nums[lookup]
                hold += 1
            lookup += 1

