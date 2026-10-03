class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        big = 0
        slow = 0
        for fast in range(len(prices)):
            diff = prices[fast] - prices[slow]
            big = max(big, diff)
            if prices[fast] < prices[slow]:
                slow = fast
        return big