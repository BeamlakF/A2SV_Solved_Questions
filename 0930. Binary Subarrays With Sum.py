def numSubarraysWithSum(self, nums, goal: int) -> int:
        # if sum of sub array is equal to goal, then return the sub arra, but how do I come back and forth...is this more sliding window question-removing an indice that has 0 value(that won't affect the sum if I remove it or not) that a prefix sum
        # But still I would have 2 pointers, misefu ena miteby=u and then track the sums they create
        # since what I am returning is an integer, and the progrss sheet says- hashmap(I have to have to number of sub-arrays that give me the sum tracked)

        prefix_sum = 0
        count = 0
        prefix_map = {0:1}

        for num in nums:
            prefix_sum +=num
            need = prefix_sum -goal

            if need in prefix_map:
                count += prefix_map[need]
            prefix_map[prefix_sum] = prefix_map.get(prefix_sum, 0) +1
        
        return count
        