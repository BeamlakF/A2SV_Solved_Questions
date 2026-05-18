class Solution:
    def isValid(self, s: str) -> bool:
        seen = {")": "(", "]":"[", "}":"{"}
        stack = []
        for i in s:
            if i in "([{":
                stack.append(i)
            elif i in ")]}":
                if not stack:
                    return False
                top = stack.pop() #to see the last open and then we remove it and copare it to the expected opening as below
                if seen [i] != top:
                    return False

        if len(stack)==0: 
            return True #then all is matched
        else:
            return False