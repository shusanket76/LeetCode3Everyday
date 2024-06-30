class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        res = [1]
        hasmap={n:[] for n in range(len(bombs))}
        def calcdistance(p1, p2):
            xcord = (p2[0]-p1[0])**2
            ycord = (p2[1]-p1[1])**2
            su = xcord+ycord
            return (su)**(1/2)


        for x in range(len(bombs)):
            for y in range(len(bombs)):
                if x==y:
                    continue
                dis = calcdistance(bombs[x], bombs[y])
                if dis<=bombs[x][2]:
                    hasmap[x].append(y)
       
        print(hasmap)
        def dfs(x, s):
            s.add(x)
            for y in hasmap[x]:
                if y not in s:
                    dfs(y,s)
            return s
            
        for x in hasmap:
            res[0] = max(res[0],len(dfs(x, set())))
        # print(hasmap2)
        return res[0]