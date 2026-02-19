from functools import cmp_to_key

def largestNumber(self, nums) -> str:
        nums = list(map(str, nums))
        
        def compare(a, b):
            if a + b > b + a:
                return -1  # a should come before b
            elif a + b < b + a:
                return 1   # b should come before a
            else:
                return 0   # they are equal in order
        
        nums.sort(key=cmp_to_key(compare))
        
        largest = "".join(nums)
        
        return "0" if largest[0] == "0" else largest
