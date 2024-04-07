class Solution:
    def minTime(self, n: int, edges, hasApple) -> int:
        hasmap = {}
        edges.sort(key=lambda x: x[0])

        def adjacentpaths():
            for x in edges:
                if x[0] in hasmap:
                    hasmap[x[0]].append(x[1])
                else:
                    hasmap[x[0]] = [x[1]]
                if x[1] in hasmap:
                    hasmap[x[1]].append(x[0])
                else:
                    hasmap[x[1]] = [x[0]]

        adjacentpaths()

        def dfs(hasmap, startpos, reset):
            reset.add(startpos)
            count = 0
            for x in hasmap[startpos]:
                if x not in reset:
                    count += dfs(hasmap, x, reset)
            if count > 0 or hasApple[startpos] == True:
                return count + 2
            else:
                return count + 0

        if len(edges) == 0:
            return 0
        b = dfs(hasmap, edges[0][0], set())
        return max(0, b - 2)
