def findRadius(self, houses, heaters) -> int:
        heaters.sort()

        def closestdist(h):
            left = 0
            right = len(heaters) - 1

            while left <= right:
                mid = (left + right) // 2
                if heaters[mid] < h:
                    left = mid + 1
                else:
                    right = mid - 1

            dist1 = float('inf')
            dist2 = float('inf')

            if left < len(heaters):
                dist1 = abs(heaters[left] - h)
            
            if right >= 0:
                dist2 = abs(heaters[right] - h)
            
            return min(dist1, dist2)

        res = 0
        for house in houses:
            res = max(res, closestdist(house))

        return res