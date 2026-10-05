# Best Time to Buy and Sell Stock
# status: solo | retry: -
# note: -

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        pr = 0


        while r < len(prices):
            if prices[r] > prices[l]:
                pr = max(pr, prices[r] - prices[l])
                r += 1
            else: 
                l = r
                r = l + 1
        
        return pr
