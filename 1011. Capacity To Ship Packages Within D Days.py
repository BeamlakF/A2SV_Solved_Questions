def shipWithinDays(self, weights, days: int) -> int:
        maxWei = -1
        total = 0
        for wei in weights:
            maxWei = max(maxWei, wei)
            total += wei

        l = maxWei
        r = total

        while l<r:
            mid = (l +r)//2
            day = 1
            curr = 0

            for wei in weights:
                if curr + wei > mid:
                    day +=1
                    curr =0
                curr += wei

            if day > days:
                l = mid +1

            else:
                r = mid
        return l