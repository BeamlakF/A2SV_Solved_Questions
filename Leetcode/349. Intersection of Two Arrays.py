def intersection(self, nums1, nums2):
        nums_1 = set(nums1)
        nums_2 = set(nums2)
        output =[]

        for i in nums_1:
            if i in nums_2 and i not in output:
                output.append(i)
        
        return output

        