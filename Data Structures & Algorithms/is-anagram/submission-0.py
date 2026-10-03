from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        l1 = Counter(list(s))
        l2 = Counter(list(t))
        if l1 == l2:
            return True
        else:
            return False 
        