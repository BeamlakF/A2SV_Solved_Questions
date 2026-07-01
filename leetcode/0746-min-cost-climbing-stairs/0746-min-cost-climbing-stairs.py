class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        stack = cost[0:2]
        if len(cost) < 3:
            return min(cost)
        
        n = len(cost) - 2; idx = 2
        while(n - 2 >= -1):
            stack.append(cost[idx] + min(stack[-1], stack[-2]))
            n -= 1; idx += 1

        return min(stack[-1], stack[-2])