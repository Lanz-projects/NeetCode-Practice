class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        nums = [1] + nums + [1]
        n = len(nums)

        dp = [[0] * n for _ in range(n)]

        def dfs(l, r):
            if l > r:
                return 0
            if dp[l][r] != 0:
                return dp[l][r]

            best = 0
            for i in range(l, r + 1):
                coins = nums[l - 1] * nums[i] * nums[r + 1]
                coins += dfs(l, i - 1) + dfs(i + 1, r)
                best = max(best, coins)

            dp[l][r] = best
            return best

        return dfs(1, n - 2)