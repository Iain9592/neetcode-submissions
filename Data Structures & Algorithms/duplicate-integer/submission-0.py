from collections import Counter
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        number = Counter(nums)
        for i in nums:
            if number[i] > 1:
                return True
        return False