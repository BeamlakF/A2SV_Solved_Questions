def maxArea(self, height: list[int]) -> int:
        i = 0
        j = len(height) - 1
        result = 0

        while i < j:
            result = max(result, (j - i) * min(height[i], height[j]))# Because the water is limited by the shorter heigh, I will take the minimum
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1

        return result
