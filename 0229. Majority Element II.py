def majorityElement(self, nums):
        n = len(nums)
        seen = {}

        for num in nums:
            seen[num] = seen.get(num, 0) + 1

        result = []
        limit = n // 3

        for num in seen:
            if seen[num] > limit:
                result.append(num)

        return result


    