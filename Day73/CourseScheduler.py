class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courseorder = {n:[] for n in range(numCourses)}
        for x in prerequisites:
            if x[0] in courseorder:
                courseorder[x[0]].append(x[1])

        ispossible = {}
        
        def dfs(start):
            if start in ispossible:
                return ispossible[start]
            ispossible[start] = False
            for x in courseorder[start]:
                a = dfs(x)
                if a is False:
                    return False
            ispossible[start] = True
            return True
    
        for x in courseorder:
            if dfs(x) is False:
                return False
        return True
        

        
        