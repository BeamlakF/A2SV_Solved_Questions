def productExceptSelf(self, nums):
        prod = 1
        zeroes = 0
        result = []

    
        for num in nums:
            if num != 0:
                prod *= num
            else:
                zeroes += 1
                        
        if zeroes > 1:
            return [0] * len(nums)
        
        for num in nums:
            if num != 0:
                if zeroes == 1:
                    result.append(0)
                else:
                    result.append(prod // num)
            else:
                result.append(prod)
        
        return result