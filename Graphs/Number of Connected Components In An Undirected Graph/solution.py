class Solution:
    def countComponents(self, n: int, edges):
        par = [i for i in range(n)]
        rank = [1] * n

        def find(n1):
            res = n1

            while res != par[res]:
                par[res] = par[par[res]]
                res = par[res]

            return res

        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
        
            if p1 == p2:
                return 0
        
            if rank[p1] > rank[p2]:
                par[p2] = p1
                rank[p1] += rank[p2]
            else:
                par[p1] = p2
                rank[p2] += rank[p1]
        
            return 1


        res = n

        for n1, n2 in edges:
            res -= union(n1, n2)

        return res
      
tests = [
    # 1. Fully connected graph → 1 component
    (5, [[0,1],[1,2],[2,3],[3,4]]),

    # 2. Two components → {0,1,2} and {3,4}
    (5, [[0,1],[1,2],[3,4]]),

    # 3. Four components → {0,1}, {2,3}, {4}, {5}
    (6, [[0,1],[2,3]]),

    # 4. No edges → n components → 4 components
    (4, []),

    # 5. Single node → 1 component
    (1, []),

    # 6. Random structure with cycles → still 1 component
    # All nodes become connected through edges
    (5, [[0,1],[1,2],[2,0],[3,4],[2,3]]),

    # 7. Larger disconnected example → 4 components
    # {0,1}, {2,3}, {4,5}, {6}
    (7, [[0,1],[2,3],[4,5]]),
]


sol = Solution()

for i, (n, edges) in enumerate(tests, 1):
    print(f"Test {i}: countComponents({n}, {edges}) = {sol.countComponents(n, edges)}")