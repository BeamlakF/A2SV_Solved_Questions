def findDuplicates(self, nums):
        count = {}
        for num in nums:
            if num not in count:
                count[num] = 0
            count[num] += 1

            result = []
            for num in count:
                if count[num] == 2:
                    result.append(num)
        return result

# TLE for the above solution

def findDuplicates(self, nums):
        result = []

        for num in nums:
            index = abs(num) - 1

            if nums[index] < 0:
                result.append(abs(num))
            else:
                nums[index] *= -1

        return result