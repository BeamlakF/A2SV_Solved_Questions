def dailyTemperatures(self, temp):
        stack = []
        t = len(temp)
        result = [0] * t

        for i in range(t):
            while stack and temp[i] > temp[stack[-1]]:
                prev = stack.pop()
                result[prev] = i - prev
            
            stack.append(i)

        return result