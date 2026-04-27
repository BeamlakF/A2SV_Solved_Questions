from collections import defaultdict

def subarraysDivByK(self, nums, k):
        count = defaultdict(int)
        count[0] = 1
        
        prefix = 0
        res = 0
        
        for num in nums:
            prefix += num
            rem = prefix % k
            
            if rem < 0:
                rem += k
            
            res += count[rem]
            count[rem] += 1
        
        return res

# The TLE way:
        count = 0
        for i in range(len(nums)):
            total = 0
            for j in range(i, len(nums)):
                total += nums[j]
                if total % k == 0:
                    count += 1

        return count