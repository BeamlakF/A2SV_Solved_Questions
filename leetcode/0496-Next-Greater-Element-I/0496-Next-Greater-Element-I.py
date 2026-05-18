class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        next_elt = {}

        for num in nums2:
            while stack and num >stack[-1]:
                smaller = stack.pop()
                next_elt[smaller] = num

            stack.append(num)

        while stack:
            next_elt[stack.pop()] = -1

        return [next_elt[x] for x in nums1]