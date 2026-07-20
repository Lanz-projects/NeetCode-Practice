class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        preMap = { i:[] for i in range(numCourses)}
        for crs, pre in prerequisites:
          preMap[crs].append(pre)
        
        output = []
        visit, cycle = set(), set()
        def dfs(crs):
          if crs in cycle:
            return False
          if crs in visit:
            return True
          cycle.add(crs)
          for pre in preMap[crs]:
            if not dfs(pre): return False
          cycle.remove(crs)
          visit.add(crs)
          output.append(crs)
          return True
        for crs in range(numCourses):
          if not dfs(crs): return []
        return output