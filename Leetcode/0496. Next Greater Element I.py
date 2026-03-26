class Solution:
    def nextGreaterElement(self, nums1, nums2):
        # Create an empty stack (monotonic decreasing stack)
        stack = []

        # Create a hashmap (dictionary) to store {num : nextGreater}
        next_greater = {}

        # Loop through nums2 from left to right
        for num in nums2:

            # While stack is not empty AND current num is greater than stack top
            while stack and num > stack[-1]:
                # Pop the top (it found its next greater)
                smaller_value = stack.pop()

                # Map the popped value to current num
                next_greater[smaller_value] = num

            # Push the current num onto the stack
            stack.append(num)

        # For remaining elements in stack, no next greater exists → map to -1
        while stack:
            next_greater[stack.pop()] = -1

        # Build the result for nums1 using the hashmap
        result = [next_greater[num] for num in nums1]

        return result
