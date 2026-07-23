class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        dp = {}

        def dfs(i, j):
            if j == len(t):
                return 1
            if i == len(s):
                return 0
            if (i,j) in dp:
                return dp[(i,j)]
            if len(s) - i < len(t) - j:
                return 0
            
            if s[i] == t[j]:
                dp[(i,j)] = dfs(i + 1, j + 1) + dfs(i + 1, j)
            else:
                dp[(i,j)] = dfs(i + 1, j)
            return dp[(i,j)]
        return dfs(0,0)