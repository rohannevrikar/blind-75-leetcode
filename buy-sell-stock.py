class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        maxProfit = 0

        # giving time out error for 12 test cases. not the best approach
        # for i in range(len(prices)-1):
        #     otherList = prices[i+1:]
            
        #     if(max(otherList) > prices[i] and (max(otherList) - prices[i]) > profit):
        #         profit = max(otherList) - prices[i]

        # two pointers approach, so that only one iteration is required
        left, right = 0,1

        while(right < len(prices)):
            if(prices[right] > prices[left]):
                profit = prices[right] - prices[left]
                maxProfit = max(profit, maxProfit)
            else:
                left=right
            right+=1
        return maxProfit
        
