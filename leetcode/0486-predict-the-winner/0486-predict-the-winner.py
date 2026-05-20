class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        def p(l,r):
            if l ==r:
                return nums [l]

            left = nums[l] - p(l+1, r)
            right = nums[r] - p(l, r -1)

            return max(left, right)

        return p(0, len(nums)-1) >= 0