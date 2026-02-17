def containsDuplicate(self, nums):
        num_map = set()  
        
        for num in nums:
            if num in num_map:  
                return True
            num_map.add(num)  
        
        return False