class Solution:
    def validTree(self, n: int, edges):
      if not n:
        return True

      adj = { i:[] for i in range(n) }
      for n1, n2 in edges:
        adj[n1].append(n2)
        adj[n2].append(n1)
      
      visit = set()
      def dfs(i, prev):
        if i in visit:
          return False
        visit.add(i)
        
        for j in adj[i]:
          if j == prev:
            continue
          if not dfs(j, i):
            return False
        return True
      return dfs(0, -1) and n == len(visit)
    
tests = [
    # 1. Valid tree
    (5, [[0,1],[0,2],[0,3],[3,4]]),

    # 2. Contains a cycle → not a tree
    (5, [[0,1],[1,2],[2,3],[3,1],[3,4]]),

    # 3. Disconnected graph → not a tree
    (5, [[0,1],[2,3]]),

    # 4. Single node, no edges → valid tree
    (1, []),

    # 5. Two nodes, one edge → valid tree
    (2, [[0,1]]),

    # 6. Multiple components even if no cycles → not a tree
    (4, [[0,1],[2,3]]),

    # 7. Edge case: n = 0
    (0, [])
]

sol = Solution()

for i, (n, edges) in enumerate(tests, 1):
    print(f"Test {i}: validTree({n}, {edges}) = {sol.validTree(n, edges)}")