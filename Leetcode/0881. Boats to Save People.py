def numRescueBoats(self, people, limit: int) -> int:
        boats = 0
        peoplesort = sorted(people)
        p = len(peoplesort)
        right = p -1
        left = 0
        while left <= right:
            if peoplesort[left] + peoplesort[right] <= limit:
                left += 1

            right -= 1 # Iknowww...because we sorted it we decrease the heaviest one and give one boat to them
            boats += 1

        return boats

        