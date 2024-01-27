class Solution:
    def partition(self, s: str):
        res = []
        def checkpalindrome(word):
            l = 0 
            r = len(word)-1
            while l<=r:
                if word[l]!=word[r]:
                    return False
                l+=1
                r-=1
            return True
        def dfs(s,curr):
            if len(curr)!=0 and checkpalindrome(curr[-1]) is False:
                return False
            if len(s)==0:
                res.append(curr[:])
                return 
 
            for x in range(len(s)):

                curr.append(s[0:x+1])
                dfs(s[x+1:], curr)
                curr.pop()


            
            
        dfs(s,[])
        return res
        