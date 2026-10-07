class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        lst = []
        dummy = sorted(nums)
        for left in range(len(nums)):
            right = len(nums) - 1
            mid = left + 1
            while mid < right:
                if dummy[left] + dummy[mid] + dummy[right] < 0:
                    mid += 1
                elif dummy[left] + dummy[mid] + dummy[right] > 0:
                    right -= 1
                else:
                    if [dummy[left], dummy[mid], dummy[right]] not in lst:
                        lst.append([dummy[left], dummy[mid], dummy[right]])
                        mid += 1
                    else:
                        mid += 1
        return lst
            