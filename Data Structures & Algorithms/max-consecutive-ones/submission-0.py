class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        big = 0
        i = 0
        for c in nums:
            if c == 1:
                i += 1
            elif c == 0:
                big = max(big, i)
                i = 0
        return max(big, i)

                