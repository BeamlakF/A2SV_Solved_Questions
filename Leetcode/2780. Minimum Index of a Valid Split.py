def minimumIndex(self, nums) -> int:
        n = len(nums)
        freq = {}
        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
         
        for key in freq:
            if freq[key] * 2 > n:
                dominant = key
                count = freq[key]

        left_count = 0
        for i in range(n-1):
            if nums[i] == dominant:
                left_count += 1
                left_length = i + 1
                right_length = n - left_length
                right_count = count - left_count
                if left_count * 2 > left_length and right_count * 2 > right_length:
                    return i
        return -1