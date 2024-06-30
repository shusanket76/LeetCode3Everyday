class Solution:
    def splitString(self, s: str) -> bool:
        def dfs(prev, a):
            if len(a)==0 and prev!=s:
                return True

            for x in range(0,len(a)):
                curr = a[:x+1]
                if (len(a)==1 or int(curr)!=0 or curr==a) and (int(prev)==-1 or int(prev)>int(curr)) and (prev==-1 or int(prev)-int(curr)==1):
                    b = dfs(curr, a[x+1:]) 
                    if b is True:
                        return True

            return False
                

        
        return dfs(-1, s)
                

        
        return dfs(-1, s)
        