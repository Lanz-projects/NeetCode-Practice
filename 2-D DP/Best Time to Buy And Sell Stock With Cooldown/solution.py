class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # State: Buying or Selling?
        # If Buy: i + 1
        # If Sell: i + 2 (needed for a cooldown day)

        dp = {} # key= (i, buying) val= max_profit

        def dfs(i, buying):
            if i >= len(prices):
                return 0
            if (i, buying) in dp:
                return dp[(i, buying)]
            
            cooldown = dfs(i + 2, not buying)
            if buying:
                buy = dfs(i + 1, not buying) - prices[i]
                dp[(i,buying)] = max(buy, cooldown)
            else:
                sell = dfs(i + 2, not buying) + prices[i]
                dp[(i,buying)] = max(sell, cooldown)
            return dp[(i,buying)]
        
        return dfs(0, True)