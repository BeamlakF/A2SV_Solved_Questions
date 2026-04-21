from collections import defaultdict
from typing import List

def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        
        def atMostK(a, k):
            freq = defaultdict(int)
            l = 0
            distinct = 0
            count = 0

            for r in range(len(a)):
                # expand window
                if freq[a[r]] == 0:
                    distinct += 1
                freq[a[r]] += 1

                # shrink if too many distinct
                while distinct > k:
                    freq[a[l]] -= 1
                    if freq[a[l]] == 0:
                        distinct -= 1
                    l += 1

                # count valid subarrays ending at r
                count += (r - l + 1)

            return count

        return atMostK(nums, k) - atMostK(nums, k - 1)