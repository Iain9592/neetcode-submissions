class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        i = 1
        dummy = []
        peak = len(arr)
        while i < peak:
            dummy.append(max(arr[i:]))
            i += 1
        dummy.append(-1)
        return dummy