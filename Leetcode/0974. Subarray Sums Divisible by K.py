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