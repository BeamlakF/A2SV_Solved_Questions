def removeStars(self, s: str) -> str:
        #iterate through the string, then if you find a star, pop it and pop the elemnet from its left.
        stack = []
        for i in s:
            if i!= "*":
                stack.append(i)
            else:
                stack.pop()

        return "".join(stack)

        