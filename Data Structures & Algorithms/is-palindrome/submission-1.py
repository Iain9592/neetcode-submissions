class Solution:
    def isPalindrome(self, s: str) -> bool:
        d = ''
        for i in s:
            if i.isalnum():
                d += i.lower()
        l = 0
        r = len(d) - 1
        while r - l > 0:
            if d[l] == d[r]:
                l += 1
                r -= 1
            else:
                return False
        return True
