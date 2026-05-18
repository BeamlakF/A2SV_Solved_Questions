def twoSum(self, nums, target):
        # Create a dictionary to store the number and its index
        num_map = {}
        
        # Loop through the list
        for i, num in enumerate(nums):
            complement = target - num  # Calculate complement
            
            # Check if complement is already in the dictionary
            if complement in num_map:
                return [num_map[complement], i]  # Return the indices of the two numbers
            
            # Store the current number and its index
            num_map[num] = i
        
        # If no solution is found, we would return an empty list, though this should never happen in this problem.
        return []